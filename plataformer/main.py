# Imagens do player baseadas no Arks
# https://arks.itch.io/dino-characters



import pygame

# constant variables
SCREEN_SIZE = [700, 500]
CIAN = (111, 92, 250)
PINK = (250, 92, 132)
# init
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Jogo do Fabrício")
clock = pygame.time.Clock()

#player
player_image = pygame.image.load('Assets/student0.png')
player_x = 300

#plataforms


plataforms = [
    #mid
    pygame.Rect(100, 300, 400, 50),
    #letf
    pygame.Rect(100, 250, 50, 50),
    #right
    pygame.Rect(450, 250, 50, 50)
]
running = True
while running:
# game loop

    #------
    # INPUT
    #------

    #check for quit
    for event in pygame.event.get():
        print(event)
        if event.type == 256: # ou event.type == pygame.quit
            running = False

    new_player_x = player_x
    #player input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        new_player_x -= 2
    if keys[pygame.K_d]:
        new_player_x += 2

    #horizontal movement
    new_player_rect = pygame.Rect(new_player_x, 200, 72, 72)
    x_colision = False

    #... check against every plataform
    for p in plataforms:
        if p.colliderect(new_player_rect):
            x_colision = True
            break

    if x_colision == False:
        player_x = new_player_x

    # update

    # draw

    #background
    screen.fill(CIAN)

    #plataforms
    for p in plataforms:
        pygame.draw.rect(screen, (PINK), p)
    #player
    screen.blit(player_image, (player_x, 200))

    #present screen
    pygame.display.flip()

    clock.tick(60)

# quit
pygame.quit()