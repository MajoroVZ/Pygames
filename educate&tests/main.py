import pygame
import time
from random import randint
pygame.init()  # Инициализация игры
screen = pygame.display.set_mode((600, 300))  # flags=pygame.NOFRAME  инициальзация размера экрана
pygame.display.set_caption("Pygame-test")

icon = pygame.image.load('images/icon-1.png')
pygame.display.set_icon(icon)  # подгрузка иконки

running = True
while running:
    background_color = (114, 156, 100)
    screen.fill(background_color)  # задний фон в виде ргб

    pygame.display.update()  # Бесконечное обновление дисплея

    for event in pygame.event.get():  # массив всех возможных событий
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                background_color = (
                    (background_color[0] * randint(1,100)) % 256, (background_color[0] * randint(1,100)) % 256, (background_color[0] * randint(1,100)) % 256)
                screen.fill(background_color)
                pygame.display.update()
                time.sleep(2)