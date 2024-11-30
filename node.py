import pygame
import debug


class Node:

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.neighbors = []
        self.weight_dict = {}

    def add_edge(self, neighbor_node):
        self.neighbors.append(neighbor_node)
        self.weight_dict[neighbor_node] = abs(self.x - neighbor_node.x) + abs(self.y - neighbor_node.y)

    def draw(self, surface):
        # Draw node circle
        pygame.draw.circle(surface,
                           (255, 0, 0),
                           (self.x, self.y),
                           10)

        # Draw node name
        new_font = pygame.font.SysFont(pygame.font.get_default_font(), 18)
        text = new_font.render(self.name, False, (0, 0, 0))
        surface.blit(text, (self.x, self.y))

        for neighbor in self.neighbors:
            # Draw Edge
            pygame.draw.line(surface,
                             (0, 255, 0),
                             (self.x, self.y),
                             (neighbor.x, neighbor.y),
                             5)
            if debug.SHOW_PATH_WEIGHTS:
                # Draw weight
                text = new_font.render(str(self.weight_dict[neighbor]), False, (0, 0, 0))
                surface.blit(text, ((self.x+neighbor.x) / 2, (self.y+neighbor.y) / 2))

