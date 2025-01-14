from psychopy import visual, event, core
import os, random, configparser
from numpy import pi, sin, cos
import xlsxwriter

MAX_RAD = 1
CENTER_X = 0
CENTER_Y = 0
PERCENT_GO = 89
NO_OF_TRIALS = 330
PRESENTATION_TIME = 900
MASK_TIME = 225
NO_OF_ANGLES = 8
NO_OF_DIST = 3
OUTLINE = False
ASSIST = False
TIMEOUT = False
STIMULI_SIZE = .1
STIMULUS_ORDER = []


#master coordination method of generating the random list of trials
def generate_trials(angles, dist, split):
    global STIMULUS_ORDER

    #generating the unique set of stimuli
    unique_go_set = []
    unique_no_go_set = []
    for i in angles:
        for j in dist:
            unique_go_set.append([i,j,1])
            unique_no_go_set.append([i,j,0])

    #number of items in the unique set of stimuli
    unique_trials = len(unique_go_set)

    # deciding how many times we can run each set of trials, and then the remaining
    # trials will be randomly decided
    go_even = split[0] // unique_trials
    go_extras = split[0] % unique_trials
    no_go_even = split[1] // unique_trials
    no_go_extras = split[1] % unique_trials

    go_set = generate_sets(unique_go_set, go_even, go_extras)
    no_go_set = generate_sets(unique_no_go_set, no_go_even, no_go_extras)

    #combining the go_set and no_go_set into one list
    ordered_set = []
    for i in go_set:
        ordered_set.append(i)
    for i in no_go_set:
        ordered_set.append(i)

    #randomizing the set
    print(ordered_set)
    random.shuffle(ordered_set)
    print(ordered_set)
    STIMULUS_ORDER = ordered_set[:]
    return ordered_set


def generate_sets(unique_set, even, extras):
    # for the go trials
    # duplicate unique set go_sets number of times to ensure each stimuli is presented equally as many times as possible
    set = []
    i = 0
    while i < even:
        for j in unique_set:
            set.append(j)
        i += 1

    # for the go trials
    # randomly pulls the remainder of trials from possible locations, removing them once pulled so they cannot be used again
    i = 0
    temp_set = unique_set[:]
    while i < extras:
        choice = random.choice(temp_set)
        set.append(choice)
        temp_set.remove(choice)
        i += 1
    return set


#generates the number of go/nogo stimuli will be needed based on the percent given and number of trials
def generate_split(trials, perc_go):
    if not trials > 0 or not perc_go > 0:
        return None

    num_go = round(trials * (perc_go / 100))
    num_no_go = trials - num_go
    return [num_go, num_no_go]


#generates even distances for stimuli based on the number of distances in the config
def generate_dist(dist):
    if not dist > 0:
        return None
    dist = dist + 1
    measures = []
    curr_meas = 0
    meas_width = float('%.3f'%(1 / dist))
    i = 0
    while i < dist:
        measures.append(round(curr_meas, 6))
        curr_meas += meas_width
        i += 1
    return measures


#generates even angles in degrees based on number of angles given in config
def generate_angles(angles):
    if not angles > 0:
        return None
    degrees = []
    curr_deg = 0
    deg_width = int(360 / angles)
    i = 0
    while i < angles:
        degrees.append(curr_deg)
        curr_deg += deg_width
        i += 1
    return degrees


#converts degrees and radii into square coordinates to be used on the screen
def circle(degrees, radius):
    global CENTER_X
    global CENTER_Y
    global MAX_RAD

    mid_x = CENTER_X
    mid_y = CENTER_Y

    if not(radius < MAX_RAD):
        return None

    if radius == 0:
        #avoids weird math when doing calculations with zero
        return [0, 0]

    radians = degrees * (pi / 180)

    x_crd = mid_x + (radius * (cos(radians)))
    y_crd = mid_y + (radius * (sin(radians)))

    return [round(x_crd / 2, 6), round(y_crd / 2, 6)]


#read in the config file
def read_config():
    global PERCENT_GO
    global NO_OF_TRIALS
    global PRESENTATION_TIME
    global MASK_TIME
    global NO_OF_ANGLES
    global NO_OF_DIST
    global OUTLINE
    global ASSIST
    global TIMEOUT
    global STIMULI_SIZE

    if not os.path.exists('config.ini'):
        print("Warning: No config file exists, using program defaults")
        return None

    config = configparser.ConfigParser()
    config.read("config.ini")


    #assign config values to global variables
    PERCENT_GO = int(config['Config']['Percent Go'])
    NO_OF_TRIALS = int(config['Config']['Number of Trials'])
    PRESENTATION_TIME = int(config['Config']['Presentation Time'])
    MASK_TIME = int(config['Config']['Mask Time'])
    NO_OF_ANGLES = int(config['Config']['Number of Angles'])
    NO_OF_DIST = int(config['Config']['Number of Distances'])
    STIMULI_SIZE = float(config['Config']['Size of Stimuli'])
    OUTLINE = config['Config']['Outline'] == 'True'
    ASSIST = config['Config']['Assist'] == 'True'
    TIMEOUT = config['Config']['Timeout or Action'] == 'Timeout'


    #bound check the variables received from the config
    if not PERCENT_GO > 0:
        print("Invalid value for Percent Go: " + str(PERCENT_GO))
        exit()
    elif not NO_OF_TRIALS > 0:
        print("Invalid value for Number of Trials: " + str(NO_OF_TRIALS))
        exit()
    elif not NO_OF_ANGLES > 0:
        print("Invalid value for Number of Angles: " + str(NO_OF_ANGLES))
        exit()
    elif not NO_OF_DIST > 0:
        print("Invalid value for Number of Distances: " + str(NO_OF_DIST))
        exit()
    elif not PRESENTATION_TIME > 0:
        print("Invalid value for Presentation Time: " + str(PRESENTATION_TIME))
        exit()
    elif not MASK_TIME > 0:
        print("Invalid value for Mask Time: " + str(MASK_TIME))
        exit()



#master method for coordinating the generation of the experiment based on config values
def create_experiment():
    global PERCENT_GO
    global NO_OF_TRIALS
    global PRESENTATION_TIME
    global MASK_TIME
    global NO_OF_ANGLES
    global NO_OF_DIST
    global OUTLINE
    global ASSIST
    global STIMULUS_ORDER

    read_config()

    go = PERCENT_GO
    trials = NO_OF_TRIALS
    num_angles = NO_OF_ANGLES
    num_dist = NO_OF_DIST

    angles = generate_angles(num_angles)
    distances = generate_dist(num_dist)
    trial_split = generate_split(trials, go)


    print(str(len(angles)) + " angles")
    print(angles)
    print(str(len(distances)) + " distances")
    print(distances)
    print(trial_split)

    generate_trials(angles, distances, trial_split)


#creates the visual window: to be removed
def create_window():
    win = visual.Window(gammaErrorPolicy="ignore", units="height", fullscr=True, color=[0,0,0])
    return(win)


#returns an array of initialized visual elements so they dont have to be initialized multiple times
def create_stimuli(win):
    global STIMULI_SIZE
    size = STIMULI_SIZE
    gs = visual.ImageStim(win, image="images/go-stimuli.png", size=[size, size])
    ngs = visual.ImageStim(win, image="images/no-go-stimuli.png", size=[size, size])
    trg = visual.Polygon(win, edges=30, radius=size/2)
    bg = visual.ImageStim(win, image="images/background.jpg", size=[1, 1])
    mask = visual.ImageStim(win, image="images/mask.jpg", size=[1, 1])
    return [gs, ngs, trg, bg, mask]



#controls the actual run of the experiment, displaying stimuli based on the stimuli array
def run_trial(trial, stimuli, win):
    global TIMEOUT
    global PRESENTATION_TIME
    global MASK_TIME
    mt = MASK_TIME
    to = TIMEOUT
    pt = PRESENTATION_TIME
    mouse = event.Mouse(newPos=[0, 0], win=win)
    #stimuli[3].draw()
    if trial[2] is 1:
        pos = circle(trial[0], trial[1])
        stimuli[0].setPos(pos)
        stimuli[2].setPos(pos)
        stimuli[0].draw(win=win)
        stimuli[2].draw(win=win)
    else:
        pos = circle(trial[0], trial[1])
        stimuli[1].setPos(pos)
        stimuli[2].setPos(pos)
        stimuli[1].draw(win=win)
        stimuli[2].draw(win=win)
    win.flip()
    core.wait(secs=(pt/1000))
    stimuli[4].draw(win=win)
    win.flip()
    core.wait(secs=(mt/1000))
    mouse.isPressedIn(stimuli[2], buttons=[0])


#master method for displaying visual elements: to be removed
def run_experiment():
    global STIMULUS_ORDER
    global TIMEOUT

    experiment_set = STIMULUS_ORDER[:]

    win = create_window()
    stimuli = create_stimuli(win)
    for trial in experiment_set:
        run_trial(trial, stimuli, win)

def write_to_excel():
    workbook = xlsxwriter.Workbook('experiment.xlsx')
    worksheet = workbook.add_worksheet()

    row = 1
    col = 0

    worksheet.write(0, 0, "x_coord")
    worksheet.write(0, 1, "y_coord")
    worksheet.write(0, 2, "angle")
    worksheet.write(0, 3, "distance")
    worksheet.write(0, 4, "type")
    worksheet.write(0, 5, "size")
    worksheet.write(0, 6, "duration")
    worksheet.write(0, 7, "mask")

    print(PRESENTATION_TIME)
    print(MASK_TIME)


    for angle, distance, type in (STIMULUS_ORDER):
        coords = circle(angle, distance)
        worksheet.write(row, col, coords[0])
        worksheet.write(row, col + 1, coords[1])
        worksheet.write(row, col + 2, angle)
        worksheet.write(row, col + 3, distance)
        if type == 0:
            worksheet.write(row, col + 4, "images/no-go-stimuli.png")
        else:
            worksheet.write(row, col + 4, "images/go-stimuli.png")
        worksheet.write(row, col + 5, STIMULI_SIZE)
        worksheet.write(row, col + 6, PRESENTATION_TIME/1000)
        worksheet.write(row, col + 7, MASK_TIME/1000)
        row += 1

    workbook.close()





#main method for running all functions
def main():
    create_experiment()
    write_to_excel()
    #run_experiment()


#what actually gets run when you run this file
main()




#please ignore below, legacy code testing the drawing of visual elements


# win = visual.Window(gammaErrorPolicy="ignore", units="height",monitor="Asus", fullscr=True)
#
# img = visual.ImageStim(win, image="images/go-stimuli.png", size=[.1,.1])
# trg = visual.Polygon(win, edges=30, radius=.1, pos=circle(radius=0, degrees=0))
# trg2 = visual.Polygon(win, edges=30, radius=45, pos=[0,0])
#
#
# mouse = event.Mouse(newPos=[0,0], win=win)
#
#
# img.draw()
# trg.draw()
# win.flip()
# end = False
# while(not end):
#     if(mouse.isPressedIn(trg, buttons=[0]) or len(event.getKeys(keyList=['esc'])) is 1):
#         end = True
#


