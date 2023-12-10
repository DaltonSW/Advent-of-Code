import pygame
import sys
import os
from collections import deque

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH, WINDOW_HEIGHT = 1100, 1100
SPRITE_SIZE = 8
BACKGROUND_COLOR = (0, 0, 0)
BOUNDARY_COLOR = (255, 0, 0, 255)

# Create the window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE | pygame.SCALED)
pygame.display.set_caption("Text File Visualizer")

# Load the text file
def load_text_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# Load sprites
def load_sprites():
    sprites = {}
    for char in ['-', '|', 'J', 'L', '7', 'F', '&', '%']:  # Add more characters if needed
        spriteChar = 'vert' if char == '|' else char
        path = os.path.join('sprites', f'{spriteChar}.png')
        if os.path.exists(path):
            sprite = pygame.image.load(path)
            sprite = pygame.transform.scale(sprite, (SPRITE_SIZE, SPRITE_SIZE))
            sprites[char] = sprite
        else:
            print(f"Warning: Sprite for '{char}' not found.")
    return sprites

# Main function
def main(filename):
    running = True
    text = load_text_file(filename)
    sprites = load_sprites()

    textRows = text.split('\n')
    drawn = False

    added = 0
    removed = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                target_color = window.get_at((mouse_x, mouse_y))
                if target_color != BACKGROUND_COLOR and target_color != (255, 0, 197):
                    if event.button == 1:
                        newColor = (0, 255, 0)
                        added += 1
                    else:
                        newColor = (0, 0, 0)
                        removed += 1
                    print(f"Added: {added} - Removed: {removed}")
                    flood_fill(window, mouse_x, mouse_y, newColor, BOUNDARY_COLOR)  # Neon green

        if not drawn:
            window.fill(BACKGROUND_COLOR)

            x, y = 0, 0
            for row in textRows:
                for char in row:
                    # if char == '\n':
                    #     x = 0
                    #     y += SPRITE_SIZE
                    #     continue
                    if char == '.':
                        # Skip rendering for periods ('.')
                        x += 1
                        if x * SPRITE_SIZE >= WINDOW_WIDTH:
                            x = 0
                            y += SPRITE_SIZE
                        continue

                    sprite = sprites.get(char.upper())  # Get the sprite for the character
                    if sprite:
                        #print(x, y)
                        window.blit(sprite, (x * SPRITE_SIZE, y))
                    # else:
                    #     # If no sprite found for the character, leave the space blank or add a placeholder
                    #     black_rect = pygame.Surface((SPRITE_SIZE, SPRITE_SIZE))
                    #     black_rect.fill((0, 0, 0))  # Black color
                    #     window.blit(black_rect, (x * SPRITE_SIZE, y * SPRITE_SIZE))

                    x += 1
                    if x * SPRITE_SIZE >= WINDOW_WIDTH:
                        x = 0
                        y += 1
                x = 0
                y += SPRITE_SIZE
                drawn = True

        pygame.display.flip()
        #running = False

    #input()
    pygame.quit()
    sys.exit()

import pygame
from collections import deque

def flood_fill(surface, x, y, new_color, boundary_color):
    target_color = surface.get_at((x, y))
    if target_color == new_color or target_color == boundary_color:
        return

    surface.lock()  # Lock the surface for direct pixel access

    w, h = surface.get_width(), surface.get_height()
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()

        if surface.get_at((x, y)) != target_color:
            continue

        # Find the extent of the line to fill
        west, east = x, x
        while west > 0 and surface.get_at((west - 1, y)) == target_color:
            west -= 1
        while east < w - 1 and surface.get_at((east + 1, y)) == target_color:
            east += 1

        # Fill the line and add north/south neighbors
        for nx in range(west, east + 1):
            surface.set_at((nx, y), new_color)
            if y > 0 and surface.get_at((nx, y - 1)) == target_color:
                queue.append((nx, y - 1))
            if y < h - 1 and surface.get_at((nx, y + 1)) == target_color:
                queue.append((nx, y + 1))

    surface.unlock()

# Usage example
# boundary_color = (r, g, b)  # The color of your maze walls
# flood_fill(screen, mouse_x, mouse_y, (0, 255, 0), boundary_color)

# Run the program
if __name__ == "__main__":
    main("Regexing.txt")
