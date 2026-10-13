import time
import pygame
from pygame.locals import (KEYDOWN, QUIT, K_ESCAPE, K_LEFT, K_RIGHT, K_UP, K_DOWN, K_q, K_d, K_z, K_s)
pygame.init()

screen = pygame.display.set_mode((1920, 1080))
screen_size = [1920, 1080]
violet = (37, 10, 105)

clock = pygame.time.Clock()

running = True

grid = pygame.Surface((1900, 970))
grid.fill("#0B041F")
grid_pos = [10, 100]
grid_size = [1900, 970]

player = pygame.Surface((25,25))
player.fill("#CF2F11")
player_pos = [11, 585]
player_size = [25, 25]

player_2 = pygame.Surface((25,25))
player_2.fill("#0000FF")
player_pos_2 = [1885, 585]
player_size_2 = [25, 25]

traînée_x_1 = pygame.Surface((25,5))
traînée_x_1.fill("#F5FF00")
traînée_x_1_pos = [player_pos[0], player_pos[1] + 10]
traînée_x_1_size = [25, 5]

traînée_y_1 = pygame.Surface((5,25))
traînée_y_1.fill("#F5FF00")
traînée_y_1_pos = [player_pos[0] + 10, player_pos[1]]
traînée_y_1_size = [5, 25]

traînée_x_2 = pygame.Surface((25,5))
traînée_x_2.fill("#F5FF00")
traînée_x_2_pos = [player_pos_2[0], player_pos_2[1] + 10]
traînée_x_2_size = [25, 5]

traînée_y_2 = pygame.Surface((5,25))
traînée_y_2.fill("#F5FF00")
traînée_y_2_pos = [player_pos_2[0] + 10, player_pos_2[1]]
traînée_y_2_size = [5, 25]


executing_lightcycle_movement_left = False
executing_lightcycle_movement_right = False
executing_lightcycle_movement_up = False
executing_lightcycle_movement_down = False

executing_lightcycle_movement_q = False
executing_lightcycle_movement_d = False
executing_lightcycle_movement_z = False
executing_lightcycle_movement_s = False


def lightcycle_movement_negative(player_pos, grid_pos, running) :
    if player_pos <= grid_pos :
        running = False
    else :
        player_pos -= 5

    return player_pos, running

def lightcycle_movement_positive(player_pos, screen_size, grid_size, player_size, running) :
    if player_pos >= (screen_size - grid_size) + (grid_size - player_size - 10) :
        running = False
    else :
        player_pos += 5

    return player_pos, running

def traînées(executing, executing_2, traînée, traînée_pos) :
    if executing or executing_2:
        screen.blit(traînée, traînée_pos)

time.sleep(1)

executing_lightcycle_movement_left = True
executing_lightcycle_movement_d = True


while running :
    screen.fill(violet)
    screen.blit(grid, grid_pos)

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
                running = False
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_ESCAPE :
                running = False


    pressed_keys = pygame.key.get_pressed()

    #-----------------------------------------------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------Joueur 1------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------

    #-------------------------------------------------------------------------------Q---------------------------------------------------------------------------
    
    if pressed_keys[K_q] :
        if executing_lightcycle_movement_q == False or executing_lightcycle_movement_d == False :
            executing_lightcycle_movement_z = False
            executing_lightcycle_movement_s = False

            executing_lightcycle_movement_q = True
        else :
            running = False
    if executing_lightcycle_movement_q :
        player_pos[0], running = lightcycle_movement_negative(player_pos[0], grid_pos[0], running)
    #-------------------------------------------------------------------------------D---------------------------------------------------------------------------
    
    if pressed_keys[K_d] :
        if executing_lightcycle_movement_q == False or executing_lightcycle_movement_d == False :
            executing_lightcycle_movement_z = False
            executing_lightcycle_movement_s = False

            executing_lightcycle_movement_d = True
        else :
            running = False
    if executing_lightcycle_movement_d :
        player_pos[0], running = lightcycle_movement_positive(player_pos[0], screen_size[0], grid_size[0], player_size[0], running)

    #-------------------------------------------------------------------------------Z---------------------------------------------------------------------------

    if pressed_keys[K_z] :
        if executing_lightcycle_movement_z == False or executing_lightcycle_movement_s == False :
            executing_lightcycle_movement_q = False
            executing_lightcycle_movement_d = False

            executing_lightcycle_movement_z = True
        else :
            running = False
    if executing_lightcycle_movement_z :
        player_pos[1], running = lightcycle_movement_negative(player_pos[1], grid_pos[1], running)

    #-------------------------------------------------------------------------------S---------------------------------------------------------------------------
    
    if pressed_keys[K_s] :
        if executing_lightcycle_movement_z == False or executing_lightcycle_movement_s == False :
            executing_lightcycle_movement_q = False
            executing_lightcycle_movement_d = False

            executing_lightcycle_movement_s = True
        else :
            running = False
    if executing_lightcycle_movement_s :
        player_pos[1], running = lightcycle_movement_positive(player_pos[1], screen_size[1], grid_size[1], player_size[1], running)


    #-----------------------------------------------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------Joueur 2------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------

    #-----------------------------------------------------------------------------LEFT--------------------------------------------------------------------------
    
    if pressed_keys[K_LEFT] :
        if executing_lightcycle_movement_left == False or executing_lightcycle_movement_right == False :
            executing_lightcycle_movement_up = False
            executing_lightcycle_movement_down = False

            executing_lightcycle_movement_left = True
        else :
            running = False
    if executing_lightcycle_movement_left :
        player_pos_2[0], running = lightcycle_movement_negative(player_pos_2[0], grid_pos[0], running)

    #-----------------------------------------------------------------------------RIGHT-------------------------------------------------------------------------
    
    if pressed_keys[K_RIGHT] :
        if executing_lightcycle_movement_left == False or executing_lightcycle_movement_right == False :
            executing_lightcycle_movement_up = False
            executing_lightcycle_movement_down = False

            executing_lightcycle_movement_right = True
        else :
            running = False
    if executing_lightcycle_movement_right :
        player_pos_2[0], running = lightcycle_movement_positive(player_pos_2[0], screen_size[0], grid_size[0], player_size_2[0], running)

    #------------------------------------------------------------------------------UP---------------------------------------------------------------------------
    
    if pressed_keys[K_UP] :
        if executing_lightcycle_movement_up == False or executing_lightcycle_movement_down == False :
            executing_lightcycle_movement_left = False
            executing_lightcycle_movement_right = False

            executing_lightcycle_movement_up = True
        else :
            running = False
    if executing_lightcycle_movement_up :
        player_pos_2[1], running = lightcycle_movement_negative(player_pos_2[1], grid_pos[1], running)

    #-----------------------------------------------------------------------------DOWN--------------------------------------------------------------------------
    
    if pressed_keys[K_DOWN] :
        if executing_lightcycle_movement_up == False or executing_lightcycle_movement_down == False :
            executing_lightcycle_movement_left = False
            executing_lightcycle_movement_right = False

            executing_lightcycle_movement_down = True
        else :
            running = False
    if executing_lightcycle_movement_down :
        player_pos_2[1], running = lightcycle_movement_positive(player_pos_2[1], screen_size[1], grid_size[1], player_size_2[1], running)


    #-----------------------------------------------------------------------------------------------------------------------------------------------------------
    #--------------------------------------------------------------------COLLISIONS JOUEURS---------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------

    if executing_lightcycle_movement_d and executing_lightcycle_movement_left :
        if player_pos[0] >= player_pos_2[0] - player_size_2[0] and player_pos[1] >= player_pos_2[1] and player_pos[1] <= player_pos_2[1] + player_size_2[1] :
                running = False
    
    if executing_lightcycle_movement_q and executing_lightcycle_movement_right :
        if player_pos_2[0] >= player_pos[0] + player_size[0] and player_pos_2[1] >= player_pos[1] and player_pos_2[1] <= player_pos[1] + player_size[1] :
            running = False
    
    if executing_lightcycle_movement_s and executing_lightcycle_movement_up :
        if player_pos[1] >= player_pos_2[1] + player_size_2[1] and player_pos[0] >= player_pos_2[0] and player_pos[0] <= player_pos_2[0] + player_size_2[0] :
            running = False
    
    if executing_lightcycle_movement_z and executing_lightcycle_movement_down :
        if player_pos_2[1] >= player_pos[1] + player_size[1] and player_pos_2[0] >= player_pos[0] and player_pos_2[0] <= player_pos[0] + player_size[0] :
            running = False


    #-----------------------------------------------------------------------------------------------------------------------------------------------------------
    #------------------------------------------------------------------------TRAINEES---------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------

    traînées(executing_lightcycle_movement_left, executing_lightcycle_movement_right, traînée_x_1, traînée_x_1_pos)
    traînées(executing_lightcycle_movement_up, executing_lightcycle_movement_down, traînée_y_1, traînée_y_1_pos)
    traînées(executing_lightcycle_movement_q, executing_lightcycle_movement_d, traînée_x_2, traînée_x_2_pos)
    traînées(executing_lightcycle_movement_z, executing_lightcycle_movement_s, traînée_y_2, traînée_y_2_pos)


    screen.blit(player, player_pos)
    screen.blit(player_2, player_pos_2)
    pygame.display.flip()
    clock.tick(60)

pygame.quit