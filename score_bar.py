import pygame


class ScoreBar:
    def __init__(self, window):
        self._WIN = window
        self._COLOR = (87, 64, 53)
        self._BG_COLOR = (135, 147, 154)
        self._DEFAULT_WIDTH = window.get_width() // 2
        self._THICKNESS = 10

        self._score = 0
        self._width = self._DEFAULT_WIDTH

    def get_score(self):
        return self._score

    def is_winning(self):
        return self._width > self._DEFAULT_WIDTH

    def is_empty(self):
        return self._width <= 0

    def increase_score(self):
        if self._width < self._WIN.get_width():
            self._score += 1

    def decrease_score(self):
        self._score -= 1

    def draw(self, window):
        self._width = self._DEFAULT_WIDTH + self._score * 50
        pygame.draw.rect(window, self._BG_COLOR, (0, 0, window.get_width(), self._THICKNESS))
        pygame.draw.rect(window, self._COLOR, (0, 0, self._width, self._THICKNESS))
