import pygame
import constants

MOVE_SPEED = 5

class Player():

    def __init__(self):
        self.pos = pygame.Vector2(0, 0)
        self.height = 50
        self.width = 30

    def update_position(self):

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_a]:
            self.pos.x = self.pos.x - MOVE_SPEED
        elif pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]:
            self.pos.x = self.pos.x + MOVE_SPEED

        if pressed_keys[pygame.K_DOWN] or pressed_keys[pygame.K_s]:
            self.pos.y = self.pos.y + MOVE_SPEED
        elif pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_w]:
            self.pos.y = self.pos.y - MOVE_SPEED

        self.pos.x = max(0, self.pos.x)
        self.pos.x = min(constants.SCREEN_WIDTH - self.width, self.pos.x)
        self.pos.y = max(0, self.pos.y)
        self.pos.y = min(constants.SCREEN_HEIGHT - self.height, self.pos.y)


    def update(self):
        self.update_position()


    def draw(self, screen):
        pygame.draw.rect(surface=screen,
                         color=(255, 0, 0),
                         rect=pygame.Rect(self.pos.x,
                                             self.pos.y,
                                             self.width,
                                             self.height))
