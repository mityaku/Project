import pygame

def draw_grid(screen):
    for x in range(0, 800, 40):
        pygame.draw.line(screen, (255, 255, 255), (x, 0), (x, 600))
    for y in range(0, 600, 40):
        pygame.draw.line(screen, (255, 255, 255), (0, y), (800, y))
