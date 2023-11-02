#!/usr/bin/env python3
from random import randint, choice
import sys
from asciimatics.effects import Cycle, Print, Stars
from asciimatics.renderers import SpeechBubble, FigletText, AbstractScreenPlayer
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.sprites import Arrow, Plot, Sam
from asciimatics.paths import Path
from asciimatics.exceptions import ResizeScreenError
from MoonSprite import Moon
from plainTextRenderer import PlainRender
import sys
import os
import numpy as np
from asciimatics.effects import Stars, Print
from asciimatics.particles import RingFirework, SerpentFirework, StarFirework, \
    PalmFirework

def fireworks(effects, screen, starttime):
    for _ in range(20):
        fireworks = [
            (PalmFirework, 25, 30),
            (PalmFirework, 25, 30),
            (StarFirework, 25, 35),
            (StarFirework, 25, 35),
            (StarFirework, 25, 35),
            (RingFirework, 20, 30),
            (SerpentFirework, 30, 35),
        ]
        firework, start, stop = choice(fireworks)
        effects.append(
            firework(screen,
                     randint(0, screen.width),
                     randint(screen.height // 4,screen.height // 3),
                     randint(start, stop),
                     start_frame=randint(starttime, starttime + 100)))

def _speak(screen, text, pos, start, end):
    return Print(
        screen,
        SpeechBubble(text, "R", uni=screen.unicode_aware),
        x=pos[0] + 4, y=pos[1] - 4,
        colour=Screen.COLOUR_CYAN,
        clear=True,
        start_frame=start,
        stop_frame=end)
    
def generateNStepsWithinMax(steps, start, stop):
    return np.linspace(start=start, stop=stop, num=steps)

def readInfiles():
    files = []
    for x in range(1, 11, 1):
        filename = str(x)
        with open(os.path.join(os.getcwd(), "cats/"+filename), 'r') as f:
            files.append(f.read())
    return files

def createCatFrames(effects, frame, screen):
    cy = screen.height - 13
    cx = screen.width - 43
    walktime = 20
    kisstime = 40
    
    #walk
    for cat in readInfiles()[:-3]:
        effects.append(
            Print(renderer=PlainRender(cat), y=cy, screen=screen, x=cx, start_frame=frame,stop_frame=frame+walktime, clear=True)
        )
        frame+=walktime
        
    # wait
    effects.append(
        Print(renderer=PlainRender(readInfiles()[-1]), y=cy, screen=screen, x=cx, start_frame=frame,stop_frame=frame+kisstime, clear=True)
        )
    frame = frame + kisstime
    
    # kiss
    effects.append(
        Print(renderer=PlainRender(readInfiles()[-2]), y=cy, screen=screen, x=cx, start_frame=frame,stop_frame=frame+kisstime, clear=True)
        )
    frame = frame + kisstime
    
    #wait
    effects.append(
        Print(renderer=PlainRender(readInfiles()[-1]), y=cy, screen=screen, x=cx, start_frame=frame,stop_frame=frame+300, clear=True)
        )
    
    return frame

def createMoonSprite(ttime, screen):
    time = 500
    center = [screen.width // 2, screen.height // 2]
    waitsteps = generateNStepsWithinMax(7, 0, time) 
    diststeps = generateNStepsWithinMax(8, (0, center[1]), (center[0], 0))[1:]
    
    path = Path()
    path.jump_to(0, center[1])
    
#    i = 0
#    for step in diststeps:
#        path.move_straight_to(int(step[0]), int(step[1]), 10)
#        path.wait(int(waitsteps[i]))
#        i+=1

    path.move_straight_to(center[0], 0, ttime - 100)
    path.wait(300)
   
    moon = Moon(screen=screen, path=path, start_frame=0)
    return moon


def demo(screen):
    scenes = []
    effects = [
        Stars(screen, (screen.width + screen.height) // 2)
    ]
    
    frame = 0
    animationTime = createCatFrames(effects, frame, screen)
    
    
    effects.append(createMoonSprite(animationTime, screen))
    
    cy = screen.height - 13
    cx = screen.width - 43
    msg1 = "Love you Oli."
    effects.append(_speak(screen, msg1, (cx-len(msg1)-2,cy+2),animationTime + 20, animationTime+80))
    msg2 = "I cant wait to spend.."
    effects.append(_speak(screen, msg2, (cx-len(msg2)-2,cy+2),animationTime + 80, animationTime+140))
    msg3 = "The rest of my life with you."
    effects.append(_speak(screen, msg3, (cx-len(msg3)-2,cy+2),animationTime + 140, animationTime+230))
    msg4 = "<3"
    effects.append(_speak(screen, msg4, (cx-len(msg4)-2,cy+2),animationTime + 230, animationTime+300))
    
    fireworks(effects, screen, animationTime + 100)
    
    #effects.append(Print(renderer=PlainRender([frame, animationTime]), y=1, screen=screen, x=1, start_frame=0,stop_frame=100, clear=True))
      
        
    scenes.append(Scene(effects))
    screen.play(scenes, stop_on_resize=True)


if __name__ == "__main__":
    while True:
        try:
            Screen.wrapper(demo)
            sys.exit(0)
        except ResizeScreenError:
            pass
