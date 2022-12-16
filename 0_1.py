import os
import sys

import pygame

size = width, height = 400, 300

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Мой пример 2")

# image = pygame.Surface([100, 100])
# image.fill(pygame.Color("red"))

def load_image(name, colorkey=None):
   fullname = os.path.join('data', name)
   # если файл не существует, то выходим
   if not os.path.isfile(fullname):
       print(f"Файл с изображением '{fullname}' не найден")
       sys.exit()
   image = pygame.image.load(fullname)
   return image


image = load_image("bomb.png")
image_edited = pygame.transform.scale(image, (200, 200))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(pygame.Color("white"))
    #screen.blit(image, (10, 10))
    screen.blit(image, (10, 10))
    screen.blit(image_edited, (20, 20))
    pygame.display.flip()

pygame.quit()