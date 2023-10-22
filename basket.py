import pygame
import os


__author__ = 'Eric-Nicolas'


class Basket(pygame.sprite.Sprite):
    def __init__(self, window):
        super().__init__()
        self._WIN_WIDTH = window.get_width()
        self._IMG = pygame.transform.scale(
            pygame.image.load(os.path.join('assets', 'img', 'basket.png')),
            (100, 100)
        )
        self.rect = self._IMG.get_rect()
        self.rect.x = (self._WIN_WIDTH - self._IMG.get_width()) // 2
        self.rect.y = window.get_height() - self._IMG.get_height() - 75
        self._x_change = 0
        self._SPEED = 5
        self._hitbox = (self.rect.x, self.rect.y + self._IMG.get_height() // 2, self._IMG.get_width(), self._IMG.get_height() // 2)
        self.rect = pygame.Rect(self._hitbox)

    def idle(self):
        self._x_change = 0

    def move_left(self):
        if self.rect.x > 0:
            self._x_change = -self._SPEED
        else:
            self.idle()

    def move_right(self):
        if self.rect.x < self._WIN_WIDTH - self._IMG.get_width():
            self._x_change = self._SPEED
        else:
            self.idle()

    def update(self):
        self.rect.x += self._x_change

    def draw(self, window):
        window.blit(self._IMG, (self.rect.x, self.rect.y - self._IMG.get_height() // 2))
