'''
Python Programming Engine
By Sigton

Makes making games easy :P
'''

import pygame
from pygame.locals import *

import constants, spritesheet

###--- PUT TILES DATA DEFINITIONS HERE ---###

'''
Data for tiles goes in the following format:

TILE_NAME = (tile_image_x, tile_image_y, tile_image_width, tile_image_height)

If you have a tile with multiple frames then set it like this:

TILE_NAME = (
             (tile_image_x, tile_image_y, tile_image_width, tile_image_height),
             (tile_image_x, tile_image_y, tile_image_width, tile_image_height)
            )

Default file for tile images is resouces/terrain.png, change as required.

'''

platforms = () # Tuple of all defined platforms

class Platform(pygame.sprite.Sprite):
    ''' A tile displayed on screen '''

    def __init__(self, spriteSheetData):
        ''' Constructor '''

        # Call the parents constructor
        pygame.sprite.Sprite.__init__(self)

        spriteSheet = spritesheet.SpriteSheet("resouces/terrain.png")

        # Take the image from the spritesheet
        self.image = spriteSheet.get_image(spriteSheetData[0],
                                           spriteSheetData[1],
                                           spriteSheetData[2],
                                           spriteSheetData[3])

        self.rect = self.image.get_rect()

class AnimatedPlatform(pygame.sprite.Sprite):

    def __init__(self, spriteSheetData):
        ''' Constructor '''

        # Call the parents constructor
        pygame.sprite.Sprite.__init__(self)

        spriteSheet = spritesheet.SpriteSheet("resources/terrain.png")

        self.images = []

        # Take the image for each sprite from the spritesheet
        # and add it to the list of frames

        for sprite in spriteSheetData:
            newImage = spriteSheet.get_image(sprite[0],
                                             sprite[1],
                                             sprite[2],
                                             sprite[3])
            self.images.append(newImage)

        self.image = self.images[0]
        self.rect = self.image.get_rect()

        # A timer var for the animation

        self.tick = 0
        self.costume = 0

    def update(self):

        self.tick += 1

        if self.tick % 10 == 0:
            self.costume = (self.costume + 1) % len(self.images)
            self.image = self.images[costume]
