import pygame

size = width, height = 400, 300

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Мой пример")

image = pygame.Surface([100, 100])
image.fill(pygame.Color("red"))
#screen.blit(image, (10, 10))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(pygame.Color("white"))
    screen.blit(image, (10, 10))
    pygame.display.flip()

pygame.quit()