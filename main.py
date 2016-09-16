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

    # Set the current level
    currentLevelNo = 0
    currentLevel = levelList[currentLevelNo]

    player.level = currentLevel

    currentLevel.player = player

    player.rect.x = 150
    player.rect.y = 400
    activeSpriteList.add(player)

    # Variables to control the player

    run = 0
    jump = False
    fullscreen = 0

    # Loop until the user clicks the close button
    gameExit = False

    # ---------- Main Program Loop ----------
    while not gameExit:
        for event in pygame.event.get(): # User did something
            if event.type == QUIT: # If user clicked close
                gameExit = True

            elif event.type == KEYDOWN:
                if event.key == constants.K_ESCAPE:
                    gameExit == True

                if event.key == K_LEFT or K_a:
                    run = -1
                elif event.key == K_RIGHT or K_d:
                    run = 1
                elif event.key == K_UP or event.key == K_w:
                    jump = True

                elif event.key == constants.K_FULLSCREEN:
                    fullscreen = 1 - fullscreen

                    if fullscreen == 1:
                        gameDisplay = pygame.display.set_mode((constants.SIZE), FULLSCREEN)
                    else:
                        gameDisplay = pygame.display.set_mode((constants.SIZE))

            elif event.type == KEYUP:
                if (event.key == K_LEFT or event.key == K_a) and player.xv < 0:
                    run = 0
                elif (event.key == K_RIGHT or event.key == K_d) and player.xv > 0:
                    run = 0
                elif event.key == K_UP or event.key == K_w:
                    jump = False















































                
            
