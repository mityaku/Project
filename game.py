import pygame
import sys
from towers import Tower
from enemies import Enemy
from utils import draw_grid

def start_game(screen):
    clock = pygame.time.Clock()
    running = True
    selected_tower = None

    towers = []
    enemies = [Enemy(0, 200)]
    spawn_timer = 0

    while running:
        screen.fill((0, 0, 0))
        draw_grid(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    x, y = event.pos
                    if selected_tower:
                        towers.append(Tower(selected_tower, x, y))
                        selected_tower = None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    selected_tower = "short"
                if event.key == pygame.K_2:
                    selected_tower = "medium"
                if event.key == pygame.K_3:
                    selected_tower = "long"

        for tower in towers:
            tower.draw(screen)
            for enemy in enemies:
                if tower.in_range(enemy):
                    enemy.take_damage(tower.damage)

        for enemy in enemies[:]:
            enemy.move()
            enemy.draw(screen)
            if enemy.is_dead():
                enemies.remove(enemy)

        spawn_timer += 1
        if spawn_timer >= 120:  # Spawn a new enemy every 2 seconds
            enemies.append(Enemy(0, 200))
            spawn_timer = 0

        pygame.display.flip()
        clock.tick(60)
