'''
Python Platforming Engine
By Sigton

Makes making games a lot easier :P
'''

import pygame
from pygame.locals import *

import constants, spritesheet, platforms, level
import player as p

import sys

def main():

    '''
    MAIN PROGRAM
    '''

    # Init the mixer, then pygame itself

    pygame.mixer.pre_init(22050, -16, 1, 512)
    pygame.mixer.init()
    pygame.init()

    # Set the display size

    global gameDisplay, clock

    gameDisplay = pygame.display.set_mode(constants.SIZE)

    # Used to manage how fast the screen updates