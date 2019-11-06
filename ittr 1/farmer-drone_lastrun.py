#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on Wed Nov  6 17:39:18 2019
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'farmer_ drone'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/steve/Documents/farmer-drone/ittr 1/farmer-drone_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "intro"
introClock = core.Clock()
rating = visual.RatingScale(win=win, name='rating', marker='triangle', size=1.0, pos=[0.0, -0.4], choices=['Trackpad', 'Mouse', 'Trackball', 'Other'], tickHeight=-1)
select_input_prompt = visual.TextStim(win=win, name='select_input_prompt',
    text='Please select the device you will be using to control the mouse',
    font='Arial',
    pos=(0, .2), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
polygon = visual.Line(
    win=win, name='polygon',
    start=(-(0.5, 0.5)[0]/2.0, 0), end=(+(0.5, 0.5)[0]/2.0, 0),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)

# Initialize components for Routine "generate_trials"
generate_trialsClock = core.Clock()

# Initialize components for Routine "reset_mouse_pos"
reset_mouse_posClock = core.Clock()
mouse = event.Mouse(newPos=[0, 0])

# Initialize components for Routine "trial"
trialClock = core.Clock()
stimuli_picture = visual.ImageStim(
    win=win,
    name='stimuli_picture', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# Initialize components for Routine "mask"
maskClock = core.Clock()
noise = visual.NoiseStim(
    win=win, name='noise',units='height', 
    noiseImage=None, mask=None,
    ori=0, pos=(0, 0), size=2, sf=None,
    phase=0.0,
    color=[1,1,1], colorSpace='rgb',     opacity=1, blendmode='avg', contrast=1.0,
    texRes=128, filter=None,
    noiseType='Binary', noiseElementSize=0.0625, 
    noiseBaseSf=8.0, noiseBW=1,
    noiseBWO=30, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=0.0)
noise.buildNoise()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "intro"-------
# update component parameters for each repeat
rating.reset()
# keep track of which components have finished
introComponents = [rating, select_input_prompt, polygon]
for thisComponent in introComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "intro"-------
while continueRoutine:
    # get current time
    t = introClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *rating* updates
    if rating.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rating.frameNStart = frameN  # exact frame index
        rating.tStart = t  # local t and not account for scr refresh
        rating.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rating, 'tStartRefresh')  # time at next scr refresh
        rating.setAutoDraw(True)
    continueRoutine &= rating.noResponse  # a response ends the trial
    
    # *select_input_prompt* updates
    if select_input_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        select_input_prompt.frameNStart = frameN  # exact frame index
        select_input_prompt.tStart = t  # local t and not account for scr refresh
        select_input_prompt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(select_input_prompt, 'tStartRefresh')  # time at next scr refresh
        select_input_prompt.setAutoDraw(True)
    
    # *polygon* updates
    if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon.frameNStart = frameN  # exact frame index
        polygon.tStart = t  # local t and not account for scr refresh
        polygon.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
        polygon.setAutoDraw(True)
    if polygon.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polygon.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            polygon.tStop = t  # not accounting for scr refresh
            polygon.frameNStop = frameN  # exact frame index
            win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
            polygon.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "intro"-------
for thisComponent in introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('rating.response', rating.getRating())
thisExp.addData('rating.rt', rating.getRT())
thisExp.nextEntry()
# the Routine "intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "generate_trials"-------
# update component parameters for each repeat
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



# keep track of which components have finished
generate_trialsComponents = []
for thisComponent in generate_trialsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
generate_trialsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "generate_trials"-------
while continueRoutine:
    # get current time
    t = generate_trialsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=generate_trialsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in generate_trialsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "generate_trials"-------
for thisComponent in generate_trialsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "generate_trials" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('experiment.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "reset_mouse_pos"-------
    # update component parameters for each repeat
    mouse = event.Mouse(newPos=[0, 0])
    # keep track of which components have finished
    reset_mouse_posComponents = []
    for thisComponent in reset_mouse_posComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    reset_mouse_posClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "reset_mouse_pos"-------
    while continueRoutine:
        # get current time
        t = reset_mouse_posClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=reset_mouse_posClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in reset_mouse_posComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "reset_mouse_pos"-------
    for thisComponent in reset_mouse_posComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "reset_mouse_pos" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "trial"-------
    # update component parameters for each repeat
    stimuli_picture.setPos((x_coord, y_coord))
    stimuli_picture.setSize((size, size))
    stimuli_picture.setImage(type)
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    mouse.clicked_name = []
    mouse.clicked_position = []
    gotValidClick = False  # until a click is received
    mouse.mouseClock.reset()
    # keep track of which components have finished
    trialComponents = [stimuli_picture, mouse]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stimuli_picture* updates
        if stimuli_picture.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stimuli_picture.frameNStart = frameN  # exact frame index
            stimuli_picture.tStart = t  # local t and not account for scr refresh
            stimuli_picture.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimuli_picture, 'tStartRefresh')  # time at next scr refresh
            stimuli_picture.setAutoDraw(True)
        if stimuli_picture.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stimuli_picture.tStartRefresh + duration-frameTolerance:
                # keep track of stop time/frame for later
                stimuli_picture.tStop = t  # not accounting for scr refresh
                stimuli_picture.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stimuli_picture, 'tStopRefresh')  # time at next scr refresh
                stimuli_picture.setAutoDraw(False)
        # *mouse* updates
        if mouse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            mouse.status = STARTED
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse.tStartRefresh + duration-frameTolerance:
                # keep track of stop time/frame for later
                mouse.tStop = t  # not accounting for scr refresh
                mouse.frameNStop = frameN  # exact frame index
                win.timeOnFlip(mouse, 'tStopRefresh')  # time at next scr refresh
                mouse.status = FINISHED
        if mouse.status == STARTED:  # only update if started and not finished!
            x, y = mouse.getPos()
            mouse.x.append(x)
            mouse.y.append(y)
            buttons = mouse.getPressed()
            mouse.leftButton.append(buttons[0])
            mouse.midButton.append(buttons[1])
            mouse.rightButton.append(buttons[2])
            mouse.time.append(mouse.mouseClock.getTime())
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('stimuli_picture.started', stimuli_picture.tStartRefresh)
    trials.addData('stimuli_picture.stopped', stimuli_picture.tStopRefresh)
    # store data for trials (TrialHandler)
    trials.addData('mouse.x', mouse.x)
    trials.addData('mouse.y', mouse.y)
    trials.addData('mouse.leftButton', mouse.leftButton)
    trials.addData('mouse.midButton', mouse.midButton)
    trials.addData('mouse.rightButton', mouse.rightButton)
    trials.addData('mouse.time', mouse.time)
    trials.addData('mouse.clicked_name', mouse.clicked_name)
    trials.addData('mouse.clicked_position', mouse.clicked_position)
    trials.addData('mouse.started', mouse.tStartRefresh)
    trials.addData('mouse.stopped', mouse.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "mask"-------
    # update component parameters for each repeat
    # keep track of which components have finished
    maskComponents = [noise]
    for thisComponent in maskComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    maskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "mask"-------
    while continueRoutine:
        # get current time
        t = maskClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=maskClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *noise* updates
        if noise.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            noise.frameNStart = frameN  # exact frame index
            noise.tStart = t  # local t and not account for scr refresh
            noise.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(noise, 'tStartRefresh')  # time at next scr refresh
            noise.setAutoDraw(True)
        if noise.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > noise.tStartRefresh + mask-frameTolerance:
                # keep track of stop time/frame for later
                noise.tStop = t  # not accounting for scr refresh
                noise.frameNStop = frameN  # exact frame index
                win.timeOnFlip(noise, 'tStopRefresh')  # time at next scr refresh
                noise.setAutoDraw(False)
        if noise.status == STARTED:
            if noise._needBuild:
                noise.buildNoise()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in maskComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "mask"-------
    for thisComponent in maskComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('noise.started', noise.tStartRefresh)
    trials.addData('noise.stopped', noise.tStopRefresh)
    # the Routine "mask" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
