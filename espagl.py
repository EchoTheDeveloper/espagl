# espagl.py

import pygame

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Shape:
    SQUARE = 'square'
    CIRCLE = 'circle'
    POLYGON = 'polygon'

class ESPAGL:
    def __init__(self):
        pygame.init()
        self.screen = None

    def start_game(self, window_name, size):
        self.screen = pygame.display.set_mode((size.x, size.y))
        pygame.display.set_caption(window_name)

    def draw_shape(self, shape_type, position, color, *args):
        if shape_type == Shape.SQUARE:
            pygame.draw.rect(self.screen, color, (position.x, position.y, 100, 100))  # Draw a square (100x100)
        elif shape_type == Shape.CIRCLE:
            pygame.draw.circle(self.screen, color, (position.x, position.y), 50)  # Draw a circle (radius 50)

    def update_screen(self):
        pygame.display.flip()

    def close_game(self):
        pygame.quit()
