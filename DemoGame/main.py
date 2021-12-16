import pygame
import os
from images import *
from classes import *
import random

pygame.init()

WIDTH, HEIGHT = 1080, 608
FPS = 60
WHITE = (255, 255, 255)
VEL = 5
BULLET_VEL = 11
MAX_BULLETS = 3

PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
targeting = False

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Smoke')
pygame.display.set_icon(icon)
pygame.display.set_gamma(200, 255, 0)

player_hit = pygame.USEREVENT + 1


def draw_window(green, player_bullet, enemies):
    # screen.fill(WHITE)
    screen.blit(background, (0, 0))

    for bullet in player_bullet:
        screen.blit(bullet_image, bullet)

    for enemy in enemies:
        screen.blit(enemy_image, enemy)

    screen.blit(space_ship, (green.x, green.y))
    pygame.display.update()


def player_movement(keys_pressed, green):
    if keys_pressed[pygame.K_d] and green.x + PLAYER_WIDTH < WIDTH:  # höger
        green.x = green.x + VEL
    if keys_pressed[pygame.K_w] and green.y > 0:  # upp
        green.y = green.y - VEL
    if keys_pressed[pygame.K_a] and green.x > 0:  # vänster
        green.x = green.x - VEL
    if keys_pressed[pygame.K_s] and green.y + PLAYER_HEIGHT < HEIGHT:  # ner
        green.y = green.y + VEL


# def border_collision(green):
#    if green.y < 0:
#        green.y = 0
#    if green.y + PLAYER_HEIGHT >= HEIGHT:
#        green.y = HEIGHT - green.height
#    if green.x < 0:
#        green.x = 0
#    if green.x + PLAYER_WIDTH >= WIDTH:
#        green.x = WIDTH - green.width


def enemy_movement(enemy_count, player):
    global targeting
    targeting = False
    for enemy in enemy_count:
        if enemy.rect.x < WIDTH - 350 and targeting == False:  # när fienden har färdats en viss längd kommer
            playerX = player.x
            playerY = player.y
            Targeting = True  # hittar lutningen mellan spelaren och fienden

        if targeting == True:
            enemy.x = player.x
            enemy.y = player.y

        else:
            enemy.rect.x -= enemy.vel


def handle_bullets(player_bullets, green):
    for bullet in player_bullets:
        bullet.rect.x += bullet.vel

        if green.colliderect(bullet):
            pygame.event.post(pygame.event.Event(player_hit))
            player_bullets.remove(bullet)
        if bullet.rect.x + bullet.width >= WIDTH or bullet.rect.x < 0:
            bullet.vel *= (-1)

        # if bullet.rect.x>WIDTH:
        # player_bullets.remove(bullet)


def main():
    green = pygame.Rect(200, 300, PLAYER_WIDTH, PLAYER_HEIGHT)
    player_bullets = []
    player_health = 3



    clock = pygame.time.Clock()
    RUNNING = True

    enemies_alive = []

    while RUNNING:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e and len(player_bullets) < MAX_BULLETS:
                    bullet = entity(screen, green.x + green.width, green.y + green.height // 2 - 3, 8, 6, 10,
                                    bullet_image)
                    player_bullets.append(bullet)
                if event.key == pygame.K_q:
                    enemy = Hostiles(screen, WIDTH - 60, random.randint(0, HEIGHT), 50, 50, 3, enemy_image)
                    enemies_alive.append(enemy)
            if event.type == player_hit:
                player_health = -1

        keys_pressed = pygame.key.get_pressed()
        player_movement(keys_pressed, green)
        enemy_movement(enemies_alive, green)
        handle_bullets(player_bullets, green)
        # border_collision(green)
        draw_window(green, player_bullets, enemies_alive)


if __name__ == '__main__':
    main()
