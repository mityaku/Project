import pygame
import sys
from menu import main_menu

pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tower Defense Game")

def main():
    main_menu(screen)

if __name__ == "__main__":
    main()
