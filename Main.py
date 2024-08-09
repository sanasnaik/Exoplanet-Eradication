# import pygame package 
import pygame, pyghelpers
from Constants import *
from IntroScene import *
from TutorialScene import *
from LevelOne import *

pygame.init()
window = pygame.display.set_mode((Constants.SCREENHEIGHT, Constants.SCREENWIDTH))

# instantiate scenes
scenesDict = {
               'LEVEL_ONE'    : LevelOne(window)}
#'INTRO_SCENE'   : IntroScene(window),
# 'TUTORIAL_SCENE': TutorialScene(window),

# create scene manager
oSceneMgr = pyghelpers.SceneMgr(scenesDict, Constants.FPS)
oSceneMgr.run()
