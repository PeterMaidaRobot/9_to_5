from game_objects.player import Player
import pygame


class Game():

    def __init__(self, screen):
        self.screen = screen
        self.player = Player()

        #self.office_image = pygame.image.load("graphics/PixelOffice.png").convert_alpha()
        self.office_background = pygame.image.load("graphics/office_background.png").convert_alpha()
        self.office_image = pygame.image.load("graphics/office_building.png").convert_alpha()
        self.office_image = pygame.transform.scale2x(self.office_image)

    def update(self):
        self.player.update()


    def draw(self):
        self.screen.fill("purple")  # Fill the display with a solid color

        self.screen.blit(self.office_background,
                         self.office_background.get_rect())

        self.screen.blit(self.office_image,
                         self.office_image.get_rect().move(60, 30))
                         
        self.player.draw(self.screen)
