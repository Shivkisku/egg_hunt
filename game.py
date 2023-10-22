import pygame
import os
from basket import Basket
from egg import Egg
from score_bar import ScoreBar


__author__ = 'Eric-Nicolas'


class Game:
    def __init__(self):
        pygame.init()

        ICON_IMG = pygame.transform.scale(
            pygame.image.load(os.path.join('assets', 'img', 'chocolate.png')),
            (32, 32)
        )
        self._BACKGROUND_IMG = pygame.image.load(os.path.join('assets', 'img', 'background.jpg'))
        self._GROUND_IMG = pygame.image.load(os.path.join('assets', 'img', 'ground.png'))

        self._PICKED_EGG_SOUND = pygame.mixer.Sound(os.path.join('assets', 'sfx', 'picked_egg.wav'))
        self._LOST_EGG_SOUND = pygame.mixer.Sound(os.path.join('assets', 'sfx', 'lost_egg.wav'))
        self._GAME_OVER_SOUND = pygame.mixer.Sound(os.path.join('assets', 'sfx', 'game_over.wav'))

        self._WIDTH, self._HEIGHT = 800, 480
        self._WIN = pygame.display.set_mode((self._WIDTH, self._HEIGHT))

        pygame.display.set_caption("Egg Hunt")
        pygame.display.set_icon(ICON_IMG)

        self._BLACK = (0, 0, 0)
        self._WHITE = (255, 255, 255)

        self._FONT = pygame.font.Font(None, 60)

        self._CLOCK = pygame.time.Clock()
        self._FPS = 60

        self._basket = Basket(self._WIN)
        self._egg = Egg(self._WIN)
        self._score_bar = ScoreBar(self._WIN)

    def update(self):
        if not self._score_bar.is_empty():
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_q] or keys_pressed[pygame.K_LEFT]:
                self._basket.move_left()
            elif keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:
                self._basket.move_right()
            elif keys_pressed[pygame.K_ESCAPE]:
                pygame.quit()
                quit()
            else:
                self._basket.idle()

            self._basket.update()
            self._egg.fall()

            # Collision
            if pygame.sprite.collide_rect(self._basket, self._egg):
                self._egg.go_top(self._score_bar)
                self._score_bar.increase_score()
                self._PICKED_EGG_SOUND.play()
            elif self._egg.has_fallen():
                self._egg.go_top(self._score_bar)
                self._score_bar.decrease_score()
                self._LOST_EGG_SOUND.play()

    def draw_background(self):
        self._WIN.fill(self._WHITE)
        self._WIN.blit(self._BACKGROUND_IMG, (0, 0))
        self._WIN.blit(self._GROUND_IMG, (0, 0))

    def draw_entities(self):
        self._basket.draw(self._WIN)
        self._egg.draw(self._WIN)
        self._score_bar.draw(self._WIN)

    def run(self):
        timer = 0
        is_running = True

        while is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.update()
            self.draw_background()

            if not self._score_bar.is_empty():
                self.draw_entities()
            else:
                # Show game over for 2 seconds
                self.game_over()
                timer += 1
                if timer == 1:
                    self._GAME_OVER_SOUND.play()
                if timer > self._FPS // 2:
                    is_running = False

            pygame.display.update()
            self._CLOCK.tick(self._FPS)

    def game_over(self):
        label = self._FONT.render("Game Over", True, self._BLACK)
        self._WIN.blit(label, (
            (self._WIDTH - label.get_width()) // 2,
            (self._HEIGHT - label.get_height()) // 2
        ))
