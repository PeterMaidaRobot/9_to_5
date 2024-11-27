import pygame
from game import Game
import constants
import paths



def play_game():

    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT),
                                     pygame.FULLSCREEN | pygame.SCALED)

    pygame.display.set_caption("9 to 5")

    clock = pygame.time.Clock()

    game = Game(screen)

    paths.init_paths()

    while True:

        # Process player inputs.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

        # Do logical updates here.
        game.update()

        # Render the graphics here.
        game.draw()

        pygame.display.flip()  # Refresh on-screen display
        clock.tick(60)         # wait until next frame (at 60 FPS)



if __name__ == "__main__":
    play_game()
