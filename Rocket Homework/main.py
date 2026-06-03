import pygame

pygame.init()
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("dark blue")
pygame.display.update()

spaceship_img = pygame.image.load("images/spaceship.png")
rocket_img = pygame.image.load("images/rocket.png")
starysky_img = pygame.image.load("images/starysky.jpg")


rocket_x =  WIDTH // 2
rocket_y = int(HEIGHT/ 2)
keys_pressed = [False,False,False,False]
spaceship_x =  WIDTH // 8
spaceship_y = int(HEIGHT/ 4)
keys_pressedwasd = [False,False,False,False]


while True:
    screen.blit(starysky_img,(0,0))     
    screen.blit(rocket_img,(rocket_x,rocket_y))
    screen.blit(spaceship_img,(spaceship_x,spaceship_y))
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
            if event.key == pygame.K_LEFT:
                keys_pressed[2] = True
            if event.key == pygame.K_RIGHT:
                keys_pressed[3] = True
            if event.key == pygame.K_w:
                keys_pressedwasd[0] = True
            if event.key == pygame.K_s:
                keys_pressedwasd[1] = True
            if event.key == pygame.K_a:
                keys_pressedwasd[2] = True
            if event.key == pygame.K_d: 
                keys_pressedwasd[3] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                keys_pressed[0] = False
            if event.key == pygame.K_DOWN:
                keys_pressed[1] = False
            if event.key == pygame.K_LEFT:
                keys_pressed[2] = False
            if event.key == pygame.K_RIGHT:
                keys_pressed[3] = False
            if event.key == pygame.K_w:
                keys_pressedwasd[0] = False
            if event.key == pygame.K_s:
                keys_pressedwasd[1] = False
            if event.key == pygame.K_a:
                keys_pressedwasd[2] = False
            if event.key == pygame.K_d:
                keys_pressedwasd[3] = False
    #moving upwards
    if keys_pressed[0] == True:
        if rocket_y >= 0:
            rocket_y -= 2
    if keys_pressedwasd[0] == True:
        if spaceship_y >= 0:
            spaceship_y -= 2

    # moving downwards
    if keys_pressed[1] == True:
        if rocket_y <= HEIGHT-100:
            rocket_y += 2
    if keys_pressedwasd[1] == True:
        if spaceship_y <= HEIGHT-100:
            spaceship_y += 2

    #moving right
    if keys_pressed[3] == True:
        if rocket_x <= WIDTH-100:
            rocket_x += 2
    if keys_pressedwasd[3] == True:
        if spaceship_x <= WIDTH-100:
            spaceship_x += 2
    
    #moving left
    if keys_pressed[2] == True:
        if rocket_x >= 0:
            rocket_x -= 2
    if keys_pressedwasd[2] == True:
        if spaceship_x >= 0:
            spaceship_x -= 2
