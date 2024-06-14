import pygame
import sys
from game import start_game

def main_menu(screen):
    font = pygame.font.SysFont(None, 55)
    clock = pygame.time.Clock()

    while True:
        screen.fill((0, 0, 0))
        title = font.render("Tower Defense Game", True, (255, 255, 255))
        screen.blit(title, (200, 100))

        play_button = font.render("Play", True, (255, 255, 255))
        screen.blit(play_button, (350, 300))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 350 <= event.pos[0] <= 450 and 300 <= event.pos[1] <= 350:
                    start_game(screen)

        pygame.display.flip()
        clock.tick(60)
