import pygame
import math

pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Space Invaders")

icon = pygame.image.load("space invaders 32x icon.png")
pygame.display.set_icon(icon)

game_over = False

player_obj = pygame.image.load("space ship.png")
player_obj_x = 368
player_obj_y = 480
player_obj_x_changer = 0

enemy_live = True
enemy_live_1 = True
enemy_live_2 = True
enemy_live_3 = True
enemy_live_4 = True
enemy_live_5 = True
enemy_live_6 = True
enemy_live_7 = True

enemy_obj = pygame.image.load("ufo.png")
enemy_obj_x = 368
enemy_obj_y = 50
enemy_obj_x_changer = 0.3
enemy_obj_y_changer = 40

enemy_obj_1 = pygame.image.load("ufo.png")
enemy_obj_x_1 = 268
enemy_obj_y_1 = 50
enemy_obj_x_changer_1 = 0.3

enemy_obj_2 = pygame.image.load("ufo.png")
enemy_obj_x_2 = 168
enemy_obj_y_2 = 50
enemy_obj_x_changer_2 = 0.3

enemy_obj_3 = pygame.image.load("ufo.png")
enemy_obj_x_3 = 68
enemy_obj_y_3 = 50
enemy_obj_x_changer_3 = 0.3

enemy_obj_4 = pygame.image.load("ufo.png")
enemy_obj_x_4 = 368
enemy_obj_y_4 = 100
enemy_obj_x_changer_4 = 0.3

enemy_obj_5 = pygame.image.load("ufo.png")
enemy_obj_x_5 = 268
enemy_obj_y_5 = 100
enemy_obj_x_changer_5 = 0.3

enemy_obj_6 = pygame.image.load("ufo.png")
enemy_obj_x_6 = 168
enemy_obj_y_6 = 100
enemy_obj_x_changer_6 = 0.3

enemy_obj_7 = pygame.image.load("ufo.png")
enemy_obj_x_7 = 68
enemy_obj_y_7 = 100
enemy_obj_x_changer_7 = 0.3

bullet_obj = pygame.image.load("bullet.png")
bullet_obj_x = 0
bullet_obj_y = 480
bullet_obj_y_changer = -1
bullet_state = "ready"

score = 0
font = pygame.font.Font("freesansbold.ttf", 32)
font_1 = pygame.font.Font("freesansbold.ttf", 64)
textX = 10
textY = 10

textX_1 = 200
textY_1 = 250

def show_score(x, y):
    score_font = font.render("score : " + str(score), True, (255,255,255))
    screen.blit(score_font,(x,y))

def game_over_def(x, y):
    global enemy_live
    global enemy_live_1
    global enemy_live_2
    global enemy_live_3
    global enemy_live_4
    global enemy_live_5
    global enemy_live_6
    global enemy_live_7
    game_over_font = font_1.render("GAME OVER", True, (255, 255, 255))
    screen.blit(game_over_font, (x, y))
    enemy_live = False
    enemy_live_1 = False
    enemy_live_2 = False
    enemy_live_3 = False
    enemy_live_4 = False
    enemy_live_5 = False
    enemy_live_6 = False
    enemy_live_7 = False

def player(x, y):
    screen.blit(player_obj,(x, y))

def enemy(x, y):
    screen.blit(enemy_obj,(x, y))

def enemy_1(x, y):
    screen.blit(enemy_obj_1,(x, y))

def enemy_2(x, y):
    screen.blit(enemy_obj_2,(x, y))

def enemy_3(x, y):
    screen.blit(enemy_obj_3,(x, y))

def enemy_4(x, y):
    screen.blit(enemy_obj_4,(x, y))

def enemy_5(x, y):
    screen.blit(enemy_obj_5,(x, y))

def enemy_6(x, y):
    screen.blit(enemy_obj_6,(x, y))

def enemy_7(x, y):
    screen.blit(enemy_obj_7,(x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_obj,(x + 16, y + 10))

def touching(enemy_x, enemy_y, bullet_x, bullet_y) :
    distance = math.sqrt(math.pow(enemy_x - bullet_x, 2) + math.pow(enemy_y - bullet_y, 2))
    if distance < 32 :
        return True
    else :
        return False

runing = True
while runing :
    screen.fill((47, 40, 54))

    if ((enemy_obj_y >= 440) and (enemy_live == True)) :
        game_over = True

    if ((enemy_obj_y_1 >= 440) and (enemy_live_1 == True)) :
        game_over = True

    if ((enemy_obj_y_2 >= 440) and (enemy_live_2 == True)) :
        game_over = True

    if ((enemy_obj_y_3 >= 440) and (enemy_live_3 == True)) :
        game_over = True

    if ((enemy_obj_y_4 >= 440) and (enemy_live_4 == True)) :
        game_over = True

    if ((enemy_obj_y_5 >= 440) and (enemy_live_5 == True)) :
        game_over = True

    if ((enemy_obj_y_6 >= 440) and (enemy_live_6 == True)) :
        game_over = True

    if ((enemy_obj_y_7 >= 440) and (enemy_live_7 == True)) :
        game_over = True

    if game_over == True :
        game_over_def(textX_1,textY_1)

    player(player_obj_x, player_obj_y)
    if enemy_live :
        enemy(enemy_obj_x, enemy_obj_y)
    if enemy_live_1 :
        enemy_1(enemy_obj_x_1, enemy_obj_y_1)
    if enemy_live_2 :
        enemy_2(enemy_obj_x_2, enemy_obj_y_2)
    if enemy_live_3 :
        enemy_3(enemy_obj_x_3, enemy_obj_y_3)
    if enemy_live_4 :
        enemy_4(enemy_obj_x_4, enemy_obj_y_4)
    if enemy_live_5 :
        enemy_5(enemy_obj_x_5, enemy_obj_y_5)
    if enemy_live_6 :
        enemy_6(enemy_obj_x_6, enemy_obj_y_6)
    if enemy_live_7 :
        enemy_7(enemy_obj_x_7, enemy_obj_y_7)

    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            runing = False
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_LEFT :
                player_obj_x_changer = -0.75
            if event.key == pygame.K_RIGHT:
                player_obj_x_changer = 0.75
            if event.key == pygame.K_SPACE :
                if bullet_state == "ready" :
                    bullet_obj_x = player_obj_x
                    fire_bullet(player_obj_x, bullet_obj_y)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                player_obj_x_changer = 0

    player_obj_x += player_obj_x_changer
    if enemy_live :
        enemy_obj_x += enemy_obj_x_changer
    if enemy_live_1 :
        enemy_obj_x_1 += enemy_obj_x_changer_1
    if enemy_live_2 :
        enemy_obj_x_2 += enemy_obj_x_changer_2
    if enemy_live_3 :
        enemy_obj_x_3 += enemy_obj_x_changer_3
    if enemy_live_4 :
        enemy_obj_x_4 += enemy_obj_x_changer_4
    if enemy_live_5 :
        enemy_obj_x_5 += enemy_obj_x_changer_5
    if enemy_live_6 :
        enemy_obj_x_6 += enemy_obj_x_changer_6
    if enemy_live_7 :
        enemy_obj_x_7 += enemy_obj_x_changer_7

    show_score(textX,textY)

    if player_obj_x <= 0 :
        player_obj_x = 0
    if player_obj_x >= 736 :
        player_obj_x = 736

    if enemy_obj_x <= 0 :
        enemy_obj_x = 0
        enemy_obj_x_changer = 0.3
        enemy_obj_x_changer_1 = 0.3
        enemy_obj_x_changer_2 = 0.3
        enemy_obj_x_changer_3 = 0.3
        enemy_obj_x_changer_4 = 0.3
        enemy_obj_x_changer_5 = 0.3
        enemy_obj_x_changer_6 = 0.3
        enemy_obj_x_changer_7 = 0.3
        enemy_obj_y += enemy_obj_y_changer
        enemy_obj_y_1 += enemy_obj_y_changer
        enemy_obj_y_2 += enemy_obj_y_changer
        enemy_obj_y_3 += enemy_obj_y_changer
        enemy_obj_y_4 += enemy_obj_y_changer
        enemy_obj_y_5 += enemy_obj_y_changer
        enemy_obj_y_6 += enemy_obj_y_changer
        enemy_obj_y_7 += enemy_obj_y_changer
    if enemy_obj_x >= 736 :
        enemy_obj_x = 736
        enemy_obj_x_changer = -0.3
        enemy_obj_x_changer_1 = -0.3
        enemy_obj_x_changer_2 = -0.3
        enemy_obj_x_changer_3 = -0.3
        enemy_obj_x_changer_4 = -0.3
        enemy_obj_x_changer_5 = -0.3
        enemy_obj_x_changer_6 = -0.3
        enemy_obj_x_changer_7 = -0.3
        enemy_obj_y += enemy_obj_y_changer
        enemy_obj_y_1 += enemy_obj_y_changer
        enemy_obj_y_2 += enemy_obj_y_changer
        enemy_obj_y_3 += enemy_obj_y_changer
        enemy_obj_y_4 += enemy_obj_y_changer
        enemy_obj_y_5 += enemy_obj_y_changer
        enemy_obj_y_6 += enemy_obj_y_changer
        enemy_obj_y_7 += enemy_obj_y_changer

    if enemy_obj_x_1 <= 0 :
        enemy_obj_x_1 = 0
        enemy_obj_x_changer = 0.3
        enemy_obj_x_changer_1 = 0.3
        enemy_obj_x_changer_2 = 0.3
        enemy_obj_x_changer_3 = 0.3
        enemy_obj_x_changer_4 = 0.3
        enemy_obj_x_changer_5 = 0.3
        enemy_obj_x_changer_6 = 0.3
        enemy_obj_x_changer_7 = 0.3
        enemy_obj_y += enemy_obj_y_changer
        enemy_obj_y_1 += enemy_obj_y_changer
        enemy_obj_y_2 += enemy_obj_y_changer
        enemy_obj_y_3 += enemy_obj_y_changer
        enemy_obj_y_4 += enemy_obj_y_changer
        enemy_obj_y_5 += enemy_obj_y_changer
        enemy_obj_y_6 += enemy_obj_y_changer
        enemy_obj_y_7 += enemy_obj_y_changer
    if enemy_obj_x_1 >= 736 :
        enemy_obj_x_1 = 736
        enemy_obj_x_changer = -0.3
        enemy_obj_x_changer_1 = -0.3
        enemy_obj_x_changer_2 = -0.3
        enemy_obj_x_changer_3 = -0.3
        enemy_obj_x_changer_4 = -0.3
        enemy_obj_x_changer_5 = -0.3
        enemy_obj_x_changer_6 = -0.3
        enemy_obj_x_changer_7 = -0.3
        enemy_obj_y += enemy_obj_y_changer
        enemy_obj_y_1 += enemy_obj_y_changer
        enemy_obj_y_2 += enemy_obj_y_changer
        enemy_obj_y_3 += enemy_obj_y_changer
        enemy_obj_y_4 += enemy_obj_y_changer
        enemy_obj_y_5 += enemy_obj_y_changer
        enemy_obj_y_6 += enemy_obj_y_changer
        enemy_obj_y_7 += enemy_obj_y_changer

    if enemy_obj_x_2 <= 0 :
        enemy_obj_x_2 = 0
        enemy_obj_x_changer = 0.3
        enemy_obj_x_changer_1 = 0.3
        enemy_obj_x_changer_2 = 0.3
        enemy_obj_x_changer_3 = 0.3
        enemy_obj_x_changer_4 = 0.3
        enemy_obj_x_changer_5 = 0.3
        enemy_obj_x_changer_6 = 0.3
        enemy_obj_x_changer_7 = 0.3
        enemy_obj_y += enemy_obj_y_changer
        enemy_obj_y_1 += enemy_obj_y_changer
        enemy_obj_y_2 += enemy_obj_y_changer
        enemy_obj_y_3 += enemy_obj_y_changer
        enemy_obj_y_4 += enemy_obj_y_changer
        enemy_obj_y_5 += enemy_obj_y_changer
        enemy_obj_y_6 += enemy_obj_y_changer
        enemy_obj_y_7 += enemy_obj_y_changer
    if enemy_obj_x_2 >= 736 :
        enemy_obj_x_2 = 736
        enemy_obj_x_changer = -0.3
        enemy_obj_x_changer_1 = -0.3
        enemy_obj_x_changer_2 = -0.3
        enemy_obj_x_changer_3 = -0.3
        enemy_obj_x_changer_4 = -0.3
        enemy_obj_x_changer_5 = -0.3
        enemy_obj_x_changer_6 = -0.3
        enemy_obj_x_changer_7 = -0.3
        enemy_obj_y += enemy_obj_y_changer
        enemy_obj_y_1 += enemy_obj_y_changer
        enemy_obj_y_2 += enemy_obj_y_changer
        enemy_obj_y_3 += enemy_obj_y_changer
        enemy_obj_y_4 += enemy_obj_y_changer
        enemy_obj_y_5 += enemy_obj_y_changer
        enemy_obj_y_6 += enemy_obj_y_changer
        enemy_obj_y_7 += enemy_obj_y_changer

    if enemy_obj_x_3 <= 0 :
        enemy_obj_x_3 = 0
        enemy_obj_x_changer = 0.3
        enemy_obj_x_changer_1 = 0.3
        enemy_obj_x_changer_2 = 0.3
        enemy_obj_x_changer_3 = 0.3
        enemy_obj_x_changer_4 = 0.3
        enemy_obj_x_changer_5 = 0.3
        enemy_obj_x_changer_6 = 0.3
        enemy_obj_x_changer_7 = 0.3
        enemy_obj_y += enemy_obj_y_changer
        enemy_obj_y_1 += enemy_obj_y_changer
        enemy_obj_y_2 += enemy_obj_y_changer
        enemy_obj_y_3 += enemy_obj_y_changer
        enemy_obj_y_4 += enemy_obj_y_changer
        enemy_obj_y_5 += enemy_obj_y_changer
        enemy_obj_y_6 += enemy_obj_y_changer
        enemy_obj_y_7 += enemy_obj_y_changer
    if enemy_obj_x_3 >= 736 :
        enemy_obj_x_3 = 736
        enemy_obj_x_changer = -0.3
        enemy_obj_x_changer_1 = -0.3
        enemy_obj_x_changer_2 = -0.3
        enemy_obj_x_changer_3 = -0.3
        enemy_obj_x_changer_4 = -0.3
        enemy_obj_x_changer_5 = -0.3
        enemy_obj_x_changer_6 = -0.3
        enemy_obj_x_changer_7 = -0.3
        enemy_obj_y += enemy_obj_y_changer
        enemy_obj_y_1 += enemy_obj_y_changer
        enemy_obj_y_2 += enemy_obj_y_changer
        enemy_obj_y_3 += enemy_obj_y_changer
        enemy_obj_y_4 += enemy_obj_y_changer
        enemy_obj_y_5 += enemy_obj_y_changer
        enemy_obj_y_6 += enemy_obj_y_changer
        enemy_obj_y_7 += enemy_obj_y_changer

    if enemy_obj_x_4 <= 0 :
        enemy_obj_x_4 = 0
        enemy_obj_x_changer = 0.3
        enemy_obj_x_changer_1 = 0.3
        enemy_obj_x_changer_2 = 0.3
        enemy_obj_x_changer_3 = 0.3
        enemy_obj_x_changer_4 = 0.3
        enemy_obj_x_changer_5 = 0.3
        enemy_obj_x_changer_6 = 0.3
        enemy_obj_x_changer_7 = 0.3
        enemy_obj_y += enemy_obj_y_changer
        enemy_obj_y_1 += enemy_obj_y_changer
        enemy_obj_y_2 += enemy_obj_y_changer
        enemy_obj_y_3 += enemy_obj_y_changer
        enemy_obj_y_4 += enemy_obj_y_changer
        enemy_obj_y_5 += enemy_obj_y_changer
        enemy_obj_y_6 += enemy_obj_y_changer
        enemy_obj_y_7 += enemy_obj_y_changer
    if enemy_obj_x_4 >= 736 :
        enemy_obj_x_4 = 736
        enemy_obj_x_changer = -0.3
        enemy_obj_x_changer_1 = -0.3
        enemy_obj_x_changer_2 = -0.3
        enemy_obj_x_changer_3 = -0.3
        enemy_obj_x_changer_4 = -0.3
        enemy_obj_x_changer_5 = -0.3
        enemy_obj_x_changer_6 = -0.3
        enemy_obj_x_changer_7 = -0.3
        enemy_obj_y += enemy_obj_y_changer
        enemy_obj_y_1 += enemy_obj_y_changer
        enemy_obj_y_2 += enemy_obj_y_changer
        enemy_obj_y_3 += enemy_obj_y_changer
        enemy_obj_y_4 += enemy_obj_y_changer
        enemy_obj_y_5 += enemy_obj_y_changer
        enemy_obj_y_6 += enemy_obj_y_changer
        enemy_obj_y_7 += enemy_obj_y_changer

    if enemy_obj_x_5 <= 0 :
        enemy_obj_x_5 = 0
        enemy_obj_x_changer = 0.3
        enemy_obj_x_changer_1 = 0.3
        enemy_obj_x_changer_2 = 0.3
        enemy_obj_x_changer_3 = 0.3
        enemy_obj_x_changer_4 = 0.3
        enemy_obj_x_changer_5 = 0.3
        enemy_obj_x_changer_6 = 0.3
        enemy_obj_x_changer_7 = 0.3
        enemy_obj_y += enemy_obj_y_changer
        enemy_obj_y_1 += enemy_obj_y_changer
        enemy_obj_y_2 += enemy_obj_y_changer
        enemy_obj_y_3 += enemy_obj_y_changer
        enemy_obj_y_4 += enemy_obj_y_changer
        enemy_obj_y_5 += enemy_obj_y_changer
        enemy_obj_y_6 += enemy_obj_y_changer
        enemy_obj_y_7 += enemy_obj_y_changer
    if enemy_obj_x_5 >= 736 :
        enemy_obj_x_5 = 736
        enemy_obj_x_changer = -0.3
        enemy_obj_x_changer_1 = -0.3
        enemy_obj_x_changer_2 = -0.3
        enemy_obj_x_changer_3 = -0.3
        enemy_obj_x_changer_4 = -0.3
        enemy_obj_x_changer_5 = -0.3
        enemy_obj_x_changer_6 = -0.3
        enemy_obj_x_changer_7 = -0.3
        enemy_obj_y += enemy_obj_y_changer
        enemy_obj_y_1 += enemy_obj_y_changer
        enemy_obj_y_2 += enemy_obj_y_changer
        enemy_obj_y_3 += enemy_obj_y_changer
        enemy_obj_y_4 += enemy_obj_y_changer
        enemy_obj_y_5 += enemy_obj_y_changer
        enemy_obj_y_6 += enemy_obj_y_changer
        enemy_obj_y_7 += enemy_obj_y_changer

    if enemy_obj_x_6 <= 0 :
        enemy_obj_x_6 = 0
        enemy_obj_x_changer = 0.3
        enemy_obj_x_changer_1 = 0.3
        enemy_obj_x_changer_2 = 0.3
        enemy_obj_x_changer_3 = 0.3
        enemy_obj_x_changer_4 = 0.3
        enemy_obj_x_changer_5 = 0.3
        enemy_obj_x_changer_6 = 0.3
        enemy_obj_x_changer_7 = 0.3
        enemy_obj_y += enemy_obj_y_changer
        enemy_obj_y_1 += enemy_obj_y_changer
        enemy_obj_y_2 += enemy_obj_y_changer
        enemy_obj_y_3 += enemy_obj_y_changer
        enemy_obj_y_4 += enemy_obj_y_changer
        enemy_obj_y_5 += enemy_obj_y_changer
        enemy_obj_y_6 += enemy_obj_y_changer
        enemy_obj_y_7 += enemy_obj_y_changer
    if enemy_obj_x_6 >= 736 :
        enemy_obj_x_6 = 736
        enemy_obj_x_changer = -0.3
        enemy_obj_x_changer_1 = -0.3
        enemy_obj_x_changer_2 = -0.3
        enemy_obj_x_changer_3 = -0.3
        enemy_obj_x_changer_4 = -0.3
        enemy_obj_x_changer_5 = -0.3
        enemy_obj_x_changer_6 = -0.3
        enemy_obj_x_changer_7 = -0.3
        enemy_obj_y += enemy_obj_y_changer
        enemy_obj_y_1 += enemy_obj_y_changer
        enemy_obj_y_2 += enemy_obj_y_changer
        enemy_obj_y_3 += enemy_obj_y_changer
        enemy_obj_y_4 += enemy_obj_y_changer
        enemy_obj_y_5 += enemy_obj_y_changer
        enemy_obj_y_6 += enemy_obj_y_changer
        enemy_obj_y_7 += enemy_obj_y_changer

        if enemy_obj_x_7 <= 0:
            enemy_obj_x_7 = 0
            enemy_obj_x_changer = 0.3
            enemy_obj_x_changer_1 = 0.3
            enemy_obj_x_changer_2 = 0.3
            enemy_obj_x_changer_3 = 0.3
            enemy_obj_x_changer_4 = 0.3
            enemy_obj_x_changer_5 = 0.3
            enemy_obj_x_changer_6 = 0.3
            enemy_obj_x_changer_7 = 0.3
            enemy_obj_y += enemy_obj_y_changer
            enemy_obj_y_1 += enemy_obj_y_changer
            enemy_obj_y_2 += enemy_obj_y_changer
            enemy_obj_y_3 += enemy_obj_y_changer
            enemy_obj_y_4 += enemy_obj_y_changer
            enemy_obj_y_5 += enemy_obj_y_changer
            enemy_obj_y_6 += enemy_obj_y_changer
            enemy_obj_y_7 += enemy_obj_y_changer
        if enemy_obj_x_7 >= 736:
            enemy_obj_x_7 = 736
            enemy_obj_x_changer = -0.3
            enemy_obj_x_changer_1 = -0.3
            enemy_obj_x_changer_2 = -0.3
            enemy_obj_x_changer_3 = -0.3
            enemy_obj_x_changer_4 = -0.3
            enemy_obj_x_changer_5 = -0.3
            enemy_obj_x_changer_6 = -0.3
            enemy_obj_x_changer_7 = -0.3
            enemy_obj_y += enemy_obj_y_changer
            enemy_obj_y_1 += enemy_obj_y_changer
            enemy_obj_y_2 += enemy_obj_y_changer
            enemy_obj_y_3 += enemy_obj_y_changer
            enemy_obj_y_4 += enemy_obj_y_changer
            enemy_obj_y_5 += enemy_obj_y_changer
            enemy_obj_y_6 += enemy_obj_y_changer
            enemy_obj_y_7 += enemy_obj_y_changer

    if bullet_obj_y  <= 0 :
        bullet_obj_y = 480
        bullet_state = "ready"

    if bullet_state == "fire" :
        fire_bullet(bullet_obj_x, bullet_obj_y)
        bullet_obj_y += bullet_obj_y_changer

    Collision = touching(enemy_obj_x, enemy_obj_y, bullet_obj_x, bullet_obj_y)
    if Collision :
        if enemy_live == True :
            if bullet_state == "fire" :
                bullet_obj_y = 480
                bullet_state = "ready"
                score += 10
                enemy_live = False

    Collision = touching(enemy_obj_x_1, enemy_obj_y_1, bullet_obj_x, bullet_obj_y)
    if Collision:
        if enemy_live_1 == True:
            if bullet_state == "fire":
                bullet_obj_y = 480
                bullet_state = "ready"
                score += 10
                enemy_live_1 = False

    Collision = touching(enemy_obj_x_2, enemy_obj_y_2, bullet_obj_x, bullet_obj_y)
    if Collision:
        if enemy_live_2 == True:
            if bullet_state == "fire":
                bullet_obj_y = 480
                bullet_state = "ready"
                score += 10
                enemy_live_2 = False

    Collision = touching(enemy_obj_x_3, enemy_obj_y_3, bullet_obj_x, bullet_obj_y)
    if Collision:
        if enemy_live_3 == True:
            if bullet_state == "fire":
                bullet_obj_y = 480
                bullet_state = "ready"
                score += 10
                enemy_live_3 = False

    Collision = touching(enemy_obj_x_4, enemy_obj_y_4, bullet_obj_x, bullet_obj_y)
    if Collision:
        if enemy_live_4 == True:
            if bullet_state == "fire":
                bullet_obj_y = 480
                bullet_state = "ready"
                score += 10
                enemy_live_4 = False

    Collision = touching(enemy_obj_x_5, enemy_obj_y_5, bullet_obj_x, bullet_obj_y)
    if Collision:
        if enemy_live_5 == True:
            if bullet_state == "fire":
                bullet_obj_y = 480
                bullet_state = "ready"
                score += 10
                enemy_live_5 = False

    Collision = touching(enemy_obj_x_6, enemy_obj_y_6, bullet_obj_x, bullet_obj_y)
    if Collision:
        if enemy_live_6 == True:
            if bullet_state == "fire":
                bullet_obj_y = 480
                bullet_state = "ready"
                score += 10
                enemy_live_6 = False

    Collision = touching(enemy_obj_x_7, enemy_obj_y_7, bullet_obj_x, bullet_obj_y)
    if Collision:
        if enemy_live_7 == True:
            if bullet_state == "fire":
                bullet_obj_y = 480
                bullet_state = "ready"
                score += 10
                enemy_live_7 = False

    pygame.display.update()
