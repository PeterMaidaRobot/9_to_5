from game_objects.player import Player


class Game():

    def __init__(self, screen):
        self.screen = screen
        self.player = Player()


    def update(self):
        self.player.update()


    def draw(self):
        self.screen.fill("purple")  # Fill the display with a solid color

        self.player.draw(self.screen)
