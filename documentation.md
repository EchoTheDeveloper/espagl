# ES-PAGL Documentation

## THIS USES PYGAME AND JUST ADDS SOME FUNCTIONS FOR PYGAME. IF YOU USE THIS IN YOUR PROJECT LINK THIS GITHUB PAGE
ES-PAGL (Echo's Super Python Amazing Graphics Library) is a Python library for simplified graphics rendering using Pygame. This library provides easy-to-use functions for initializing a graphics window, drawing text, and basic shapes.

## Usage

### Initialization

To start using ES-PAGL, initialize the library and create a graphics window.

```
import pygame
from espagl import ESPAGL, Vector2, Shape

# Initialize ES-PAGL
espagl = ESPAGL()

# Start the game window
espagl.start_game("My Game", Vector2(800, 600))
```

### Drawing Text

Use the `write_text` method to draw text on the graphics window.

```
# Draw text on the screen
espagl.write_text("Hello, World!", Vector2(300, 200), (0, 255, 0))
```

### Drawing Shapes

Draw different shapes like squares and circles using the `draw_shape` method.

```
# Draw a square at a specific position
espagl.draw_shape(Shape.SQUARE, Vector2(400, 300), (0, 0, 255))

# Draw a circle at another position
espagl.draw_shape(Shape.CIRCLE, Vector2(500, 400), (255, 0, 0))
```

### Updating and Closing

Update the screen to display changes and close the game properly.

```
# Update the screen to display changes
espagl.update_screen()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Close the game
espagl.close_game()
```

## API Reference

### `ESPAGL` Class

#### `start_game(window_name, size, icon=None)`

Initialize the graphics window.

- `window_name`: Name of the game window.
- `size`: Vector2 object representing the window size.
- `icon`: Optional icon for the window.

```
#### `write_text(text, position, color=(255, 255, 255))`

Draw text on the screen.

- `text`: Text to be displayed.
- `position`: Vector2 object representing the text position.
- `color`: RGB tuple representing the text color.
```

```
#### `draw_shape(shape_type, position, color)`

Draw a shape on the screen.

- `shape_type`: Enum value (e.g., `Shape.SQUARE`, `Shape.CIRCLE`).
- `position`: Vector2 object representing the shape's position.
- `color`: RGB tuple representing the shape's color.
```

```
#### `update_screen()`

Update the display to show changes.
```

```
#### `close_game()`

Quit and clean up the pygame instance.
```

### `Vector2` Class

Represents a 2D vector with `x` and `y` components.

### `Shape` Enum

Enum class representing different shape types (`SQUARE`, `CIRCLE`, etc.).

## Examples
# Hello World:

```# main.py

from espagl import ESPAGL, Vector2

# Initialize ESPAGL
espagl = ESPAGL()

# Start the game window
espagl.start_game("Hello World!", Vector2(800, 400))

# Draw "Hello World!" text at the center of the screen
espagl.write_text("Hello World!", Vector2(300, 180), (0, 255, 0))

# Update the screen to display changes
espagl.update_screen()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Close the game
espagl.close_game()
```

# Draw a square
```# main.py
import pygame
from espagl import ESPAGL, Vector2, Shape

# Initialize ESPAGL
espagl = ESPAGL()

# Start the game window
espagl.start_game("Drawing a Square", Vector2(800, 600))

# Draw a red square at the center of the screen
center_position = Vector2(350, 250)  # Position of the top-left corner of the square
square_color = (255, 0, 0)  # Red color
espagl.draw_shape(Shape.SQUARE, center_position, square_color)

# Update the screen to display changes
espagl.update_screen()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Close the game
espagl.close_game()

```
