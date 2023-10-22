import pygame
import os
import random




class Egg(pygame.sprite.Sprite):
    def __init__(self, window):
        super().__init__()
        self._WIN_WIDTH, self._WIN_HEIGHT = window.get_width(), window.get_height()
        self._IMG = pygame.transform.scale(
            pygame.image.load(os.path.join('assets', 'img', 'chocolate_egg.png')),
            (50, 50)
        )
        self.rect = self._IMG.get_rect()
        self.rect.x = random.randint(0, self._WIN_WIDTH - self._IMG.get_width())
        self.rect.y = 0
        self._speed = 2

    def go_top(self, score_bar):
        self.rect.y = 0
        self.rect.x = random.randint(0, self._WIN_WIDTH - self._IMG.get_width())
        if score_bar.is_winning() and score_bar.get_score() % 5 == 0:
            self._speed += 1

    def fall(self):
        self.rect.y += self._speed

    def has_fallen(self):
        return self.rect.y >= self._WIN_HEIGHT - self._IMG.get_height() - 75

    def draw(self, window):
        window.blit(self._IMG, self.rect)
