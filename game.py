from game_objects.player import Player
import pygame


class Game():

    def __init__(self, screen):
        self.screen = screen
        self.player = Player()

        self.office_image = pygame.image.load("graphics/PixelOffice.png").convert_alpha()


    def update(self):
        self.player.update()


    def draw(self):
        self.screen.fill("purple")  # Fill the display with a solid color

        self.screen.blit(self.office_image,
                         self.office_image.get_rect())
                         
        self.player.draw(self.screen)
