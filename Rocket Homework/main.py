import pygame

pygame.init()
WIDTH = 600
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("dark blue")
pygame.display.update()

spaceship_img = pygame.image.load("images/spaceship.png")
rocket_img = pygame.image.load("images/rocket.png")
starysky_img = pygame.image.load("images/starysky.jpg")


rocket_x =  WIDTH // 2
rocket_y = int(HEIGHT/ 2)
keys_pressed = [False,False]
spaceship_x =  WIDTH // 3
spaceship_y = int(HEIGHT/ 3)
keys_pressed = [False,False]


while True:
    screen.blit(starysky_img,(0,0))     
    screen.blit(rocket_img,(rocket_x,rocket_y))
    screen.blit(spaceship_img,(rocket_x,rocket_y))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                keys_pressed[0] = True
            if event.key == pygame.K_DOWN:
                keys_pressed[1] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                keys_pressed[0] = False
            if event.key == pygame.K_DOWN:
                keys_pressed[1] = False
    if keys_pressed[0] == True:
        rocket_y -= 1
    if keys_pressed[1] == True:
        spaceship_y -= 1
   