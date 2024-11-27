import pygame

import constants
import paths

MOVE_SPEED = 4

class Worker():

    def __init__(self):
        '''
        I believe self.pos is the player position in float precision, and
        self.rect.topleft is the player position integer precision.
        in the draw() function,
        screen.blit(self.image, self.rect.topleft) seems glitchier than
        screen.blit(self.image, self.pos)
        I removed
        self.rect = self.image.blit(source=all_images, ...) to not have to position schemes.
        '''
        self.pos = pygame.Vector2(640, 140)
        self.height = 23
        self.width = 17

        all_images = pygame.image.load("graphics/PixelOfficeAssets.png").convert_alpha()
        # Create a smaller blank surface, and blit the part we want onto it.
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.image.blit(source=all_images,
                        dest=(0, 0),
                        area=(22, # left of character on sheet position
                              132, # top of character head on sheet position
                              all_images.get_rect().width,
                              all_images.get_rect().height))
        self.image = pygame.transform.scale2x(self.image)
        self.height *= 2
        self.width *= 2

        self.node = paths.Destinations.ENTRANCE
        self.path_to_follow = []

    def move_to(self, target):
        self.path_to_follow = paths.get_path(self.node, target)

    def update(self):
        # Check if we still have movement left in this path to follow
        if len(self.path_to_follow) > 0:

            # If we hit the node in the path, remove it and move to the next one.
            if self.pos.x == self.path_to_follow[0].x and self.pos.y == self.path_to_follow[0].y:
                self.node = self.path_to_follow[0]
                self.path_to_follow = self.path_to_follow[1:]

            # If we still haven't reached our destination, update the position
            if len(self.path_to_follow) > 0:
                velocity = pygame.Vector2(self.path_to_follow[0].x - self.pos.x,
                                          self.path_to_follow[0].y - self.pos.y)
                velocity = velocity.normalize()
                self.pos += velocity

    def draw(self, screen):
        # Update the draw position to be the float precision position value
        screen.blit(self.image, self.pos)
