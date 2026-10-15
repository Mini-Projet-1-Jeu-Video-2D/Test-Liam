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
player_pos_instant = [0, 0]
player_size = [25, 25]

player_2 = pygame.Surface((25,25))
player_2.fill("#0000FF")
player_pos_2 = [1885, 585]
player_pos_2_instant = [0, 0]
player_size_2 = [25, 25]

traînées_player = {}

traînée_q = pygame.Surface((5,5))
traînée_q.fill("#F5FF00")
traînée_q_pos = [player_pos[0], player_pos[1] + 10]
traînée_q_size = [5, 5]

traînée_d = pygame.Surface((5,5))
traînée_d.fill("#F5FF00")
traînée_d_pos = [player_pos[0], player_pos[1] + 10]
traînée_d_size = [5, 5]

traînée_z = pygame.Surface((5,5))
traînée_z.fill("#F5FF00")
traînée_z_pos = [player_pos[0] + 10, player_pos[1]]
traînée_z_size = [5, 5]

traînée_s = pygame.Surface((5,5))
traînée_s.fill("#F5FF00")
traînée_s_pos = [player_pos[0] + 10, player_pos[1]]
traînée_s_size = [5, 5]

traînée_left = pygame.Surface((5,5))
traînée_left.fill("#F5FF00")
traînée_left_pos = [player_pos_2[0], player_pos_2[1] + 10]
traînée_left_size = [5, 5]

traînée_right = pygame.Surface((5,5))
traînée_right.fill("#F5FF00")
traînée_right_pos = [player_pos_2[0], player_pos_2[1] + 10]
traînée_right_size = [5, 5]

traînée_up = pygame.Surface((5,5))
traînée_up.fill("#F5FF00")
traînée_up_pos = [player_pos_2[0] + 10, player_pos_2[1]]
traînée_up_size = [5, 5]

traînée_down = pygame.Surface((5,5))
traînée_down.fill("#F5FF00")
traînée_down_pos = [player_pos_2[0] + 10, player_pos_2[1]]
traînée_down_size = [5, 5]


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
    
    if pressed_keys[K_q] and not pressed_keys[K_d] and not pressed_keys[K_z] and not pressed_keys[K_s] :
        if executing_lightcycle_movement_q == False or executing_lightcycle_movement_d == False :
            executing_lightcycle_movement_z = False
            executing_lightcycle_movement_s = False

            executing_lightcycle_movement_q = True
        else :
            running = False
    if executing_lightcycle_movement_q :
        player_pos[0], running = lightcycle_movement_negative(player_pos[0], grid_pos[0], running)
        player_pos_instant = [player_pos[0], player_pos[1]]
    #-------------------------------------------------------------------------------D---------------------------------------------------------------------------
    
    if pressed_keys[K_d] and not pressed_keys[K_q] and not pressed_keys[K_z] and not pressed_keys[K_s] :
        if executing_lightcycle_movement_q == False or executing_lightcycle_movement_d == False :
            executing_lightcycle_movement_z = False
            executing_lightcycle_movement_s = False

            executing_lightcycle_movement_d = True
        else :
            running = False
    if executing_lightcycle_movement_d :
        player_pos[0], running = lightcycle_movement_positive(player_pos[0], screen_size[0], grid_size[0], player_size[0], running)
        player_pos_instant = [player_pos[0], player_pos[1]]

    #-------------------------------------------------------------------------------Z---------------------------------------------------------------------------

    if pressed_keys[K_z] and not pressed_keys[K_q] and not pressed_keys[K_d] and not pressed_keys[K_s] :
        if executing_lightcycle_movement_z == False or executing_lightcycle_movement_s == False :
            executing_lightcycle_movement_q = False
            executing_lightcycle_movement_d = False

            executing_lightcycle_movement_z = True
        else :
            running = False
    if executing_lightcycle_movement_z :
        player_pos[1], running = lightcycle_movement_negative(player_pos[1], grid_pos[1], running)
        player_pos_instant = [player_pos[0], player_pos[1]]

    #-------------------------------------------------------------------------------S---------------------------------------------------------------------------
    
    if pressed_keys[K_s] and not pressed_keys[K_q] and not pressed_keys[K_d] and not pressed_keys[K_z] :
        if executing_lightcycle_movement_z == False or executing_lightcycle_movement_s == False :
            executing_lightcycle_movement_q = False
            executing_lightcycle_movement_d = False

            executing_lightcycle_movement_s = True
        else :
            running = False
    if executing_lightcycle_movement_s :
        player_pos[1], running = lightcycle_movement_positive(player_pos[1], screen_size[1], grid_size[1], player_size[1], running)
        player_pos_instant = [player_pos[0], player_pos[1]]


    #-----------------------------------------------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------Joueur 2------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------

    #-----------------------------------------------------------------------------LEFT--------------------------------------------------------------------------
    
    if pressed_keys[K_LEFT] and not pressed_keys[K_RIGHT] and not pressed_keys[K_UP] and not pressed_keys[K_DOWN] :
        if executing_lightcycle_movement_left == False or executing_lightcycle_movement_right == False :
            executing_lightcycle_movement_up = False
            executing_lightcycle_movement_down = False

            executing_lightcycle_movement_left = True
        else :
            running = False
    if executing_lightcycle_movement_left :
        player_pos_2[0], running = lightcycle_movement_negative(player_pos_2[0], grid_pos[0], running)
        player_pos_2_instant = [player_pos_2[0], player_pos_2[1]]

    #-----------------------------------------------------------------------------RIGHT-------------------------------------------------------------------------
    
    if pressed_keys[K_RIGHT] and not pressed_keys[K_LEFT] and not pressed_keys[K_UP] and not pressed_keys[K_DOWN] :
        if executing_lightcycle_movement_left == False or executing_lightcycle_movement_right == False :
            executing_lightcycle_movement_up = False
            executing_lightcycle_movement_down = False

            executing_lightcycle_movement_right = True
        else :
            running = False
    if executing_lightcycle_movement_right :
        player_pos_2[0], running = lightcycle_movement_positive(player_pos_2[0], screen_size[0], grid_size[0], player_size_2[0], running)
        player_pos_2_instant = [player_pos_2[0], player_pos_2[1]]

    #------------------------------------------------------------------------------UP---------------------------------------------------------------------------
    
    if pressed_keys[K_UP] and not pressed_keys[K_LEFT] and not pressed_keys[K_RIGHT] and not pressed_keys[K_DOWN] :
        if executing_lightcycle_movement_up == False or executing_lightcycle_movement_down == False :
            executing_lightcycle_movement_left = False
            executing_lightcycle_movement_right = False

            executing_lightcycle_movement_up = True
        else :
            running = False
    if executing_lightcycle_movement_up :
        player_pos_2[1], running = lightcycle_movement_negative(player_pos_2[1], grid_pos[1], running)
        player_pos_2_instant = [player_pos_2[0], player_pos_2[1]]

    #-----------------------------------------------------------------------------DOWN--------------------------------------------------------------------------
    
    if pressed_keys[K_DOWN] and not pressed_keys[K_LEFT] and not pressed_keys[K_RIGHT] and not pressed_keys[K_UP] :
        if executing_lightcycle_movement_up == False or executing_lightcycle_movement_down == False :
            executing_lightcycle_movement_left = False
            executing_lightcycle_movement_right = False

            executing_lightcycle_movement_down = True
        else :
            running = False
    if executing_lightcycle_movement_down :
        player_pos_2[1], running = lightcycle_movement_positive(player_pos_2[1], screen_size[1], grid_size[1], player_size_2[1], running)
        player_pos_2_instant = [player_pos_2[0], player_pos_2[1]]


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

    if executing_lightcycle_movement_q :
        traînée_q = pygame.Surface((player_pos_instant[0] - 10,5))
        traînée_q.fill("#F5FF00")
        traînée_q_size = [player_pos_instant[0] - 10,5]
        screen.blit(traînée_q, traînée_q_pos)
    
    if executing_lightcycle_movement_d :
        traînée_d = pygame.Surface((player_pos_instant[0] - 10,5))
        traînée_d.fill("#F5FF00")
        traînée_d_size = [player_pos_instant[0] - 10,5]
        screen.blit(traînée_d, traînée_d_pos)

    screen.blit(player, player_pos)
    screen.blit(player_2, player_pos_2)
    pygame.display.flip()
    clock.tick(60)

pygame.quit