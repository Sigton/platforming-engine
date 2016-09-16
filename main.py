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

    clock = pygame.time.Clock()

    # Set the caption and icon
    pygame.display.set_caption("Platforming Engine")
    icon = spritesheet.SpriteSheet("resources.icon.ico").get_image(0,0,32,32)
    pygame.display.set_icon(icon)

    ''' RUN MENU HERE '''

    # Create the player

    global player, activeSpriteList

    player = p.Player()

    activeSpriteList = pygame.sprite.Group()

    # Create the level list
    levelList = []
    levelList.append(level.Level_01(player, True))
    
