import pygame
from pygame.locals import *

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
        self.clock = pygame.time.Clock()  # Clock to control frame rate
        self.inputs = {}  # Dictionary to map input names to pygame key constants

    def start_game(self, window_name, size):
        self.screen = pygame.display.set_mode((size.x, size.y))
        pygame.display.set_caption(window_name)

    def draw_shape(self, shape_type, position, color, *args):
        if shape_type == Shape.SQUARE:
            pygame.draw.rect(self.screen, color, (position.x, position.y, 100, 100))  # Draw a square (100x100)
        elif shape_type == Shape.CIRCLE:
            pygame.draw.circle(self.screen, color, (position.x, position.y), 50)  # Draw a circle (radius 50)

    def write_text(self, text, position, color=(255, 255, 255)):
        font = pygame.font.Font(None, 36)  # Load a default font with size 36
        text_surface = font.render(text, True, color)  # Render the text onto a surface
        text_rect = text_surface.get_rect(center=(position.x, position.y))  # Get the rectangle containing the text
        self.screen.blit(text_surface, text_rect)  # Draw the text surface onto the screen

    def update_screen(self):
        pygame.display.flip()
        self.clock.tick(60)  # Limit frame rate to 60 FPS

    def close_game(self):
        pygame.quit()

    def add_input(self, name, keys):
        # Map the input name to a list of pygame key constants
        self.inputs[name] = [getattr(pygame, key) for key in keys]

    def get_input(self):
        keys = pygame.key.get_pressed()
        for name, key_list in self.inputs.items():
            if any(keys[key] for key in key_list):
                return name
        return None
