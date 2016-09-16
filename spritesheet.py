'''
Python Platforming Engine
By Sigton

Makes making games a lot easier :P
'''

import pygame
from pygame.locals import *

import constants

class SpriteSheet(object):

    # Points to a sprite sheet image
    sprite_sheet = None

    def __init__(self, filename):

        ''' Constructor. Pass in file name of sprite sheet '''

        # Load the sprite sheet
        self.sprite_sheet = pygame.image.load(filename).convert()

    def get_image(self, x, y, width, height):

        ''' Grab a single image out of a larger spritesheet '''

        # Create a new blank image
        image = pygame.Surface([width,height]).convert()

        # Copy the sprite from the spritesheet
        image.blit(self.sprite_sheet, (0,0), (x, y, width, height))

        # Assuming white works for transparency
        image.set_colorkey(constants.WHITE)

        # Return the image
        return image
