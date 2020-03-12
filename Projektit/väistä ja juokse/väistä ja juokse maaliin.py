import pygame
import math

pygame.init()

# create screen
screen = pygame.display.set_mode((800, 600))

# Game pics
pygame.display.set_caption("kekkero")
playerdog = pygame.image.load('kekeright.png')
bg = pygame.image.load('kartta.png')
playerpupu = pygame.image.load('pupuu.png')

# player1
playerx = 50
playery = 530
width = 64
height = 61
playerx_change = 0
playery_change = 0

# PLAYER2
player2x = 736
player2y = 530
player2width = 64
player2height = 61
player2x_change = 0
player2y_change = 0


# draw player to x, y
def player(playerx, playery):
    screen.blit(playerdog, (playerx, playery))


# draw player2 to x, y
def player2(player2x, player2y):
    screen.blit(playerpupu, (player2x, player2y))


# collision
def iscollision(player2x, player2y, playerx, playery):
    distance = math.hypot(player2x - playerx, player2y - playery)
    if distance < 50:
        return True
    else:
        return False


# draw background 0, 0
def background():
    screen.blit(bg, (0, 0,))


# main loop
run = True
while run:
    nopeus = pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # player 1 movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -5
            if event.key == pygame.K_RIGHT:
                playerx_change = 5
            if event.key == pygame.K_UP:
                playery_change = -5
            if event.key == pygame.K_DOWN:
                playery_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerx_change = 0
                playery_change = 0

        # player 2 movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player2x_change = -5
            if event.key == pygame.K_d:
                player2x_change = 5
            if event.key == pygame.K_w:
                player2y_change = -5
            if event.key == pygame.K_s:
                player2y_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_w or event.key == pygame.K_s:
                player2x_change = 0
                player2y_change = 0

    playerx += playerx_change
    playery += playery_change

    # player1 boundaries
    if playerx <= 0:
        playerx = 0
    elif playerx >= 736:
        playerx = 736
    if playery <= 420:
        playery = 420
    elif playery >= 530:
        playery = 530

    # player2 boundaries

    player2x += player2x_change
    player2y += player2y_change

    if player2x <= 0:
        player2x = 0
    elif player2x >= 736:
        player2x = 736
    if player2y <= 420:
        player2y = 420
    elif player2y >= 530:
        player2y = 530

    #  if collision player 1 and 2
    collision = iscollision(player2x, player2y, playerx, playery)
    if collision:
        player2x = 600
    if collision:
        playerx = 300

    background()
    player(playerx, playery)
    player2(player2x, player2y)
    pygame.display.update()

pygame.quit()
