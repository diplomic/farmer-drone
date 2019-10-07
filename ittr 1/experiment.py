from psychopy import visual, event, monitors, core, gui, data
import numpy as np
import os, re, random, configparser, time
from numpy import pi, sin, cos, mod

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


def generate_trials(num_ang, angles, num_dist, dist, trials, split):
    global STIMULUS_ORDER

    experiment_set = []

    #generating the unique set of stimuli
    unique_go_set = [[0,0,1]]
    unique_no_go_set = [[0,0,0]]
    for i in angles:
        for j in dist:
            if j is not 0:
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

    ordered_set = []
    for i in go_set:
        ordered_set.append(i)
    for i in no_go_set:
        ordered_set.append(i)

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


def generate_split(trials, perc_go):
    if not trials > 0 or not perc_go > 0:
        return None

    num_go = round(trials * (perc_go / 100))
    num_no_go = trials - num_go
    return [num_go, num_no_go]


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


def circle(degrees, radius):
    global CENTER_X
    global CENTER_Y
    global MAX_RAD

    mid_x = CENTER_X
    mid_y = CENTER_Y

    if not(radius < MAX_RAD):
        return None

    radians = degrees * (pi / 180)

    x_crd = mid_x + (radius * (cos(radians)))
    y_crd = mid_y + (radius * (sin(radians)))

    return [x_crd / 2, y_crd / 2]


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


    #checking to make sure these are all good values that can be used i.e. non-zero, non-negative numbers
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


    print(angles)
    print(distances)
    print(trial_split)

    generate_trials(num_angles, angles, num_dist, distances, trials, trial_split)


def create_window():
    win = visual.Window(gammaErrorPolicy="ignore", units="height", fullscr=True, color=[0,0,0])
    return(win)


def create_stimuli(win):
    global STIMULI_SIZE
    size = STIMULI_SIZE
    gs = visual.ImageStim(win, image="images/go-stimuli.png", size=[size, size])
    ngs = visual.ImageStim(win, image="images/no-go-stimuli.png", size=[size, size])
    trg = visual.Polygon(win, edges=30, radius=size/2)
    bg = visual.ImageStim(win, image="images/background.jpg", size=[1, 1])
    mask = visual.ImageStim(win, image="images/mask.jpg", size=[1, 1])
    return [gs, ngs, trg, bg, mask]



def run_trial(trial, stimuli, win):
    global TIMEOUT
    to = TIMEOUT
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
    core.wait(secs=.9)
    mouse.isPressedIn(stimuli[2], buttons=[0])




    #show mask



def run_experiment():
    global STIMULUS_ORDER
    global TIMEOUT

    experiment_set = STIMULUS_ORDER[:]

    win = create_window()
    stimuli = create_stimuli(win)
    for trial in experiment_set:
        run_trial(trial, stimuli, win)



def main():
    create_experiment()
    run_experiment()


main()


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


