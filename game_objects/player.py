import pygame
import constants

MOVE_SPEED = 4

class Player():

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
        self.pos = pygame.Vector2(0, 0)
        self.height = 23
        self.width = 15

        all_images = pygame.image.load("graphics/PixelOfficeAssets.png").convert_alpha()
        # Create a smaller blank surface, and blit the part we want onto it.
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.image.blit(source=all_images,
                        dest=(0, 0),
                        area=(2, # left of character on sheet position
                              104, # top of character head on sheet position
                              all_images.get_rect().width,
                              all_images.get_rect().height))
        self.image = pygame.transform.scale2x(self.image)
        self.height *= 2
        self.width *= 2

    def update_position(self):

        pressed_keys = pygame.key.get_pressed()

        # Determine movement vector
        move_vector = pygame.Vector2(0, 0)
        for m in (constants.MOVE_MAP[key] for key in constants.MOVE_MAP if pressed_keys[key]):
            move_vector += m

        # Normalize movement vector if necessary. Then apply speed to movement vector
        if move_vector.length() > 1:
            move_vector = move_vector.normalize()
        move_vector *= MOVE_SPEED

        # Update the player position
        self.pos += move_vector

        # Assure we aren't out of the screen's bounds
        self.pos.x = max(0, self.pos.x)
        self.pos.x = min(constants.SCREEN_WIDTH - self.width, self.pos.x)
        self.pos.y = max(0, self.pos.y)
        self.pos.y = min(constants.SCREEN_HEIGHT - self.height, self.pos.y)


    def update(self):
        self.update_position()


    def draw(self, screen):
        # Update the draw position to be the float precision position value
        screen.blit(self.image, self.pos)
