import pygame
import math

class Tower:
    def __init__(self, tower_type, x, y):
        self.tower_type = tower_type
        self.x = x
        self.y = y
        if tower_type == "short":
            self.range = 100
            self.damage = 10
            self.color = (0, 255, 0)
        elif tower_type == "medium":
            self.range = 200
            self.damage = 20
            self.color = (255, 255, 0)
        elif tower_type == "long":
            self.range = 300
            self.damage = 30
            self.color = (255, 0, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), 20)
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.range, 1)

    def in_range(self, enemy):
        distance = math.sqrt((self.x - enemy.x) ** 2 + (self.y - enemy.y) ** 2)
        return distance <= self.range
