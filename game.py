import pygame

from game_objects.player import Player
from paths import Paths
import debug


class Game():

    def __init__(self, screen):
        self.screen = screen
        self.player = Player()
        self.paths = Paths()

        #self.office_image = pygame.image.load("graphics/PixelOffice.png").convert_alpha()
        self.office_background = pygame.image.load("graphics/office_background.png").convert_alpha()
        self.office_image = pygame.image.load("graphics/office_building.png").convert_alpha()
        self.office_image = pygame.transform.scale2x(self.office_image)

        NUMBER_WIDTH = 8
        NUMBER_HEIGHT = 12
        all_number_images = pygame.image.load("graphics/clock_numbers_2x.png").convert_alpha()
        self.number_images = []
        for digit in range(10):

            self.number_images.append(pygame.Surface((NUMBER_WIDTH, NUMBER_HEIGHT), pygame.SRCALPHA))
            self.number_images[digit].blit(source=all_number_images,
                                dest=(0, 0),
                                area=(0 + digit * 8, # left of character on sheet position
                                      0, # top of character head on sheet position
                                      NUMBER_WIDTH,
                                      NUMBER_HEIGHT))

        self.time = {
            "hour": 6,
            "minute": 59,
            "second": 0
        }

    def update_time(self):
        # Increment the second by 1. We are running at 60FPS so 1 real second will be 1 game minute
        self.time["second"] += 1

        # If the seconds passed 60, increase the minute
        if self.time["second"] == 60:
            self.time["second"] = 0
            self.time["minute"] += 1

            # Increment the hour for 60 minutes
            if self.time["minute"] == 60:
                self.time["minute"] = 0
                self.time["hour"] += 1

                # Reset the hour from 12 to 1
                if self.time["hour"] == 13:
                    self.time["hour"] = 1

    def update(self):
        self.player.update()

        self.update_time()

    def draw_clock(self):

        CLOCK_POS_X = 222
        CLOCK_POS_Y = 80
        NUMBER_WIDTH = 8
        COLON_WIDTH = 4

        first_digit = self.time["hour"] // 10
        self.screen.blit(self.number_images[first_digit],
                         self.number_images[first_digit].get_rect().move(CLOCK_POS_X + NUMBER_WIDTH * 0,
                                                                         CLOCK_POS_Y))
        second_digit = self.time["hour"] % 10
        self.screen.blit(self.number_images[second_digit],
                         self.number_images[second_digit].get_rect().move(CLOCK_POS_X + NUMBER_WIDTH * 1,
                                                                          CLOCK_POS_Y))
        third_digit = self.time["minute"] // 10
        self.screen.blit(self.number_images[third_digit],
                         self.number_images[third_digit].get_rect().move(CLOCK_POS_X + COLON_WIDTH + NUMBER_WIDTH * 2,
                                                                         CLOCK_POS_Y))
        fourth_digit = self.time["minute"] % 10
        self.screen.blit(self.number_images[fourth_digit],
                         self.number_images[fourth_digit].get_rect().move(CLOCK_POS_X + COLON_WIDTH + NUMBER_WIDTH * 3,
                                                                          CLOCK_POS_Y))

    def draw(self):
        self.screen.fill("purple")  # Fill the display with a solid color

        self.screen.blit(self.office_background,
                         self.office_background.get_rect())

        self.screen.blit(self.office_image,
                         self.office_image.get_rect().move(60, 30))
                         
        self.player.draw(self.screen)

        self.draw_clock()

        if debug.SHOW_PATHS:
            self.paths.draw(self.screen)
