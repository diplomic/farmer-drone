/********************* 
 * Farmer-Drone Test *
 *********************/

// init psychoJS:
var psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'farmer-drone';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(introRoutineBegin);
flowScheduler.add(introRoutineEachFrame);
flowScheduler.add(introRoutineEnd);
flowScheduler.add(generate_trialsRoutineBegin);
flowScheduler.add(generate_trialsRoutineEachFrame);
flowScheduler.add(generate_trialsRoutineEnd);
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin, trialsLoopScheduler);
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({expName, expInfo});

var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '3.2.4';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0/Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0/60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}

var introClock;
var select_input_prompt;
var polygon;
var generate_trialsClock;
var reset_mouse_posClock;
var trialClock;
var stimuli_picture;
var mouse;
var maskClock;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "intro"
  introClock = new util.Clock();
  select_input_prompt = new visual.TextStim({
    win: psychoJS.window,
    name: 'select_input_prompt',
    text: 'Please select the device you will be using to control the mouse',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.2], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  polygon = new visual.ShapeStim ({
    win: psychoJS.window, name: 'polygon', 
    vertices: [[-[0.5, 0.5][0]/2.0, 0], [+[0.5, 0.5][0]/2.0, 0]],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -2, interpolate: true,
  });
  
  // Initialize components for Routine "generate_trials"
  generate_trialsClock = new util.Clock();
  // Initialize components for Routine "reset_mouse_pos"
  reset_mouse_posClock = new util.Clock();
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  stimuli_picture = new visual.ImageStim({
    win : psychoJS.window,
    name : 'stimuli_picture', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  mouse = new core.Mouse({
    win: psychoJS.window,
  });
  mouse.mouseClock = new util.Clock();
  // Initialize components for Routine "mask"
  maskClock = new util.Clock();
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

var t;
var frameN;
var introComponents;
function introRoutineBegin() {
  //------Prepare to start Routine 'intro'-------
  t = 0;
  introClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  // keep track of which components have finished
  introComponents = [];
  introComponents.push(select_input_prompt);
  introComponents.push(polygon);
  
  introComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

var frameRemains;
var continueRoutine;
function introRoutineEachFrame() {
  //------Loop for each frame of Routine 'intro'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = introClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *select_input_prompt* updates
  if (t >= 0.0 && select_input_prompt.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    select_input_prompt.tStart = t;  // (not accounting for frame time here)
    select_input_prompt.frameNStart = frameN;  // exact frame index
    select_input_prompt.setAutoDraw(true);
  }

  
  // *polygon* updates
  if (t >= 0.0 && polygon.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    polygon.tStart = t;  // (not accounting for frame time here)
    polygon.frameNStart = frameN;  // exact frame index
    polygon.setAutoDraw(true);
  }

  frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (polygon.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    polygon.setAutoDraw(false);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  introComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function introRoutineEnd() {
  //------Ending Routine 'intro'-------
  introComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  // the Routine "intro" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var generate_trialsComponents;
function generate_trialsRoutineBegin() {
  //------Prepare to start Routine 'generate_trials'-------
  t = 0;
  generate_trialsClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  // keep track of which components have finished
  generate_trialsComponents = [];
  
  generate_trialsComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function generate_trialsRoutineEachFrame() {
  //------Loop for each frame of Routine 'generate_trials'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = generate_trialsClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  generate_trialsComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function generate_trialsRoutineEnd() {
  //------Ending Routine 'generate_trials'-------
  generate_trialsComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  // the Routine "generate_trials" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var trials;
var currentLoop;
var trialIterator;
function trialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'experiment.xlsx',
    seed: undefined, name: 'trials'});
  psychoJS.experiment.addLoop(trials); // add the loop to the experiment
  currentLoop = trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = trials[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisTrial = result.value;
    thisScheduler.add(importConditions(trials));
    thisScheduler.add(reset_mouse_posRoutineBegin);
    thisScheduler.add(reset_mouse_posRoutineEachFrame);
    thisScheduler.add(reset_mouse_posRoutineEnd);
    thisScheduler.add(trialRoutineBegin);
    thisScheduler.add(trialRoutineEachFrame);
    thisScheduler.add(trialRoutineEnd);
    thisScheduler.add(maskRoutineBegin);
    thisScheduler.add(maskRoutineEachFrame);
    thisScheduler.add(maskRoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : true}));
  }

  return Scheduler.Event.NEXT;
}


function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}

var reset_mouse_posComponents;
function reset_mouse_posRoutineBegin() {
  //------Prepare to start Routine 'reset_mouse_pos'-------
  t = 0;
  reset_mouse_posClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  // keep track of which components have finished
  reset_mouse_posComponents = [];
  
  reset_mouse_posComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function reset_mouse_posRoutineEachFrame() {
  //------Loop for each frame of Routine 'reset_mouse_pos'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = reset_mouse_posClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  reset_mouse_posComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function reset_mouse_posRoutineEnd() {
  //------Ending Routine 'reset_mouse_pos'-------
  reset_mouse_posComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  // the Routine "reset_mouse_pos" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var gotValidClick;
var trialComponents;
function trialRoutineBegin() {
  //------Prepare to start Routine 'trial'-------
  t = 0;
  trialClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  stimuli_picture.setPos([x_coord, y_coord]);
  stimuli_picture.setSize([size, size]);
  stimuli_picture.setImage(type);
  // setup some python lists for storing info about the mouse
  // current position of the mouse:
  mouse.x = [];
  mouse.y = [];
  mouse.leftButton = [];
  mouse.midButton = [];
  mouse.rightButton = [];
  mouse.time = [];
  mouse.clicked_name = [];
  mouse.clicked_position = [];
  gotValidClick = false; // until a click is received
  mouse.mouseClock.reset();
  // keep track of which components have finished
  trialComponents = [];
  trialComponents.push(stimuli_picture);
  trialComponents.push(mouse);
  
  trialComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

var prevButtonState;
function trialRoutineEachFrame() {
  //------Loop for each frame of Routine 'trial'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = trialClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *stimuli_picture* updates
  if (t >= 0.0 && stimuli_picture.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    stimuli_picture.tStart = t;  // (not accounting for frame time here)
    stimuli_picture.frameNStart = frameN;  // exact frame index
    stimuli_picture.setAutoDraw(true);
  }

  frameRemains = 0.0 + duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (stimuli_picture.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    stimuli_picture.setAutoDraw(false);
  }
  // *mouse* updates
  if (t >= 0.0 && mouse.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    mouse.tStart = t;  // (not accounting for frame time here)
    mouse.frameNStart = frameN;  // exact frame index
    mouse.status = PsychoJS.Status.STARTED;
    prevButtonState = mouse.getPressed();  // if button is down already this ISN'T a new click
    }
  frameRemains = 0.0 + duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (mouse.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    mouse.status = PsychoJS.Status.FINISHED;
  }
  if (mouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
    let buttons = mouse.getPressed();
    const xys = mouse.getPos();
    mouse.x.push(xys[0]);
    mouse.y.push(xys[1]);
    mouse.leftButton.push(buttons[0]);
    mouse.midButton.push(buttons[1]);
    mouse.rightButton.push(buttons[2]);
    mouse.time.push(mouse.mouseClock.getTime());
    // check if the mouse was inside our 'clickable' objects
    gotValidClick = false;
    for (const obj of [stimuli_picture]) {
      if (obj.contains(mouse)) {
        gotValidClick = true;
        mouse.clicked_name.push(obj.name)
        mouse.clicked_position.push(obj.position)
      }
    }
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  trialComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function trialRoutineEnd() {
  //------Ending Routine 'trial'-------
  trialComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  // store data for thisExp (ExperimentHandler)
  psychoJS.experiment.addData('mouse.x', mouse.x);
  psychoJS.experiment.addData('mouse.y', mouse.y);
  psychoJS.experiment.addData('mouse.leftButton', mouse.leftButton);
  psychoJS.experiment.addData('mouse.midButton', mouse.midButton);
  psychoJS.experiment.addData('mouse.rightButton', mouse.rightButton);
  psychoJS.experiment.addData('mouse.time', mouse.time);
  psychoJS.experiment.addData('mouse.clicked_name', mouse.clicked_name);
  psychoJS.experiment.addData('mouse.clicked_position', mouse.clicked_position);
  
  // the Routine "trial" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var maskComponents;
function maskRoutineBegin() {
  //------Prepare to start Routine 'mask'-------
  t = 0;
  maskClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  // keep track of which components have finished
  maskComponents = [];
  
  maskComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function maskRoutineEachFrame() {
  //------Loop for each frame of Routine 'mask'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = maskClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  maskComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function maskRoutineEnd() {
  //------Ending Routine 'mask'-------
  maskComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  // the Routine "mask" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}


function endLoopIteration({thisScheduler, isTrials=true}) {
  // ------Prepare for next entry------
  return function () {
    // ------Check if user ended loop early------
    if (currentLoop.finished) {
      // Check for and save orphaned data
      if (Object.keys(psychoJS.experiment._thisEntry).length > 0) {
        psychoJS.experiment.nextEntry();
      }
      thisScheduler.stop();
    } else if (isTrials) {
      psychoJS.experiment.nextEntry();
    }
  return Scheduler.Event.NEXT;
  };
}


function importConditions(loop) {
  const trialIndex = loop.getTrialIndex();
  return function () {
    loop.setTrialIndex(trialIndex);
    psychoJS.importAttributes(loop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (Object.keys(psychoJS.experiment._thisEntry).length > 0) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});

  return Scheduler.Event.QUIT;
}
