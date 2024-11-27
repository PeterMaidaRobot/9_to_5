import pygame
from enum import Enum


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720



MOVE_MAP = {pygame.K_a: pygame.Vector2(-1, 0),
            pygame.K_d: pygame.Vector2(1, 0),
            pygame.K_w: pygame.Vector2(0, -1),
            pygame.K_s: pygame.Vector2(0, 1),
            pygame.K_LEFT: pygame.Vector2(-1, 0),
            pygame.K_RIGHT: pygame.Vector2(1, 0),
            pygame.K_UP: pygame.Vector2(0, -1),
            pygame.K_DOWN: pygame.Vector2(0, 1)
            }


class Directions(Enum):
    LEFT = 0
    RIGHT = 1
