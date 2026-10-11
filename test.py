import pygame
from pygame.locals import (KEYDOWN, QUIT, K_ESCAPE, K_LEFT, K_RIGHT, K_UP, K_DOWN, K_q, K_d, K_z, K_s)
pygame.init()

screen = pygame.display.set_mode((1700, 900), pygame.FULLSCREEN)
screen_size = [1700, 900]
violet = (37, 10, 105)

clock = pygame.time.Clock()

running = True

grid = pygame.Surface((1740, 880))
grid.fill("#0B041F")
grid_pos = [10, 100]
grid_size = [1740, 880]

player = pygame.Surface((25,25))
player.fill("#0000FF")
player_pos = [11, 540]
player_size = [25, 25]

player_2 = pygame.Surface((25,25))
player_2.fill("#CF2F11")
player_pos_2 = [1724, 540]
player_size_2 = [25, 25]


executing_lightcycle_movement_left = False
executing_lightcycle_movement_right = False
executing_lightcycle_movement_up = False
executing_lightcycle_movement_down = False

executing_lightcycle_movement_q = False
executing_lightcycle_movement_d = False
executing_lightcycle_movement_z = False
executing_lightcycle_movement_s = False


def lightcycle_movement_negative(player_pos, grid_pos, executing) :
    if player_pos <= grid_pos :
        player_pos = grid_pos
    else :
        player_pos -= 5

    executing = True
    return executing

def lightcycle_movement_positive(player_pos, screen_size, grid_size, player_size, adjustment, executing) :
    if player_pos >= (screen_size - grid_size) + (grid_size - player_size + adjustment) :
        player_pos = (screen_size - grid_size) + (grid_size - player_size + adjustment)
    else :
        player_pos += 5

    executing = True
    return executing



while running :
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

    lightcycle_movement_positive(player_pos[0], screen_size[0], grid_size[0], player_size[0], 50, executing_lightcycle_movement_right)
    if executing_lightcycle_movement_right :
        lightcycle_movement_positive(player_pos[0], screen_size[0], grid_size[0], player_size[0], 50, executing_lightcycle_movement_right)

    #-----------------------------------------------------------------------------LEFT--------------------------------------------------------------------------
    
    if pressed_keys[K_LEFT] :
        if executing_lightcycle_movement_left == False or executing_lightcycle_movement_right == False :
            executing_lightcycle_movement_up = False
            executing_lightcycle_movement_down = False

            lightcycle_movement_negative(player_pos[0], grid_pos[0], executing_lightcycle_movement_left)
    if executing_lightcycle_movement_left :
        lightcycle_movement_negative(player_pos[0], grid_pos[0], executing_lightcycle_movement_left)

    #-----------------------------------------------------------------------------RIGHT-------------------------------------------------------------------------
    
    if pressed_keys[K_RIGHT] :
        if executing_lightcycle_movement_left == False or executing_lightcycle_movement_right == False :
            executing_lightcycle_movement_up = False
            executing_lightcycle_movement_down = False

            lightcycle_movement_positive(player_pos[0], screen_size[0], grid_size[0], player_size[0], 50, executing_lightcycle_movement_right)
    if executing_lightcycle_movement_right :
        lightcycle_movement_positive(player_pos[0], screen_size[0], grid_size[0], player_size[0], 50, executing_lightcycle_movement_right)

    #------------------------------------------------------------------------------UP---------------------------------------------------------------------------
    
    if pressed_keys[K_UP] :
        if executing_lightcycle_movement_up == False or executing_lightcycle_movement_down == False :
            executing_lightcycle_movement_left = False
            executing_lightcycle_movement_right = False

            lightcycle_movement_negative(player_pos[1], grid_pos[1], executing_lightcycle_movement_up)
    if executing_lightcycle_movement_up :
        lightcycle_movement_negative(player_pos[1], grid_pos[1], executing_lightcycle_movement_up)

    #-----------------------------------------------------------------------------DOWN--------------------------------------------------------------------------
    
    if pressed_keys[K_DOWN] :
        if executing_lightcycle_movement_up == False or executing_lightcycle_movement_down == False :
            executing_lightcycle_movement_left = False
            executing_lightcycle_movement_right = False

            lightcycle_movement_positive(player_pos[1], screen_size[1], grid_size[1], player_size[1], 80, executing_lightcycle_movement_down)
    if executing_lightcycle_movement_down :
        lightcycle_movement_positive(player_pos[1], screen_size[1], grid_size[1], player_size[1], 80, executing_lightcycle_movement_down)

    #-----------------------------------------------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------Joueur 2------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------

    lightcycle_movement_negative(player_pos_2[0], grid_pos[0], executing_lightcycle_movement_q)
    if executing_lightcycle_movement_q :
        lightcycle_movement_negative(player_pos_2[0], grid_pos[0], executing_lightcycle_movement_q)

    #-------------------------------------------------------------------------------Q---------------------------------------------------------------------------
    
    if pressed_keys[K_q] :
        if player_pos_2[0] <= grid_pos[0] :
            player_pos_2[0] = grid_pos[0]
        else :
            player_pos_2[0] -= 5

    #-------------------------------------------------------------------------------D---------------------------------------------------------------------------
    
    if pressed_keys[K_d] :
        if player_pos_2[0] >= (screen_size[0] - grid_size[0]) + (grid_size[0] - player_size_2[0] + 50) :
            player_pos_2[0] = (screen_size[0] - grid_size[0]) + (grid_size[0] - player_size_2[0] + 50)
        else :
            player_pos_2[0] += 5

    #-------------------------------------------------------------------------------Z---------------------------------------------------------------------------

    if pressed_keys[K_z] :
        if player_pos_2[1] <= grid_pos[1] :
            player_pos_2[1] = grid_pos[1]
        else :
            player_pos_2[1] -= 5

    #-------------------------------------------------------------------------------S---------------------------------------------------------------------------
    
    if pressed_keys[K_s] :
        if player_pos_2[1] >= (screen_size[1] - grid_size[1]) + (grid_size[1] - player_size_2[1] + 80) :
            player_pos_2[1] = (screen_size[1] - grid_size[1]) + (grid_size[1] - player_size_2[1] + 80)
        else :
            player_pos_2[1] += 5



    if player_pos[0] + player_size[0] == player_pos_2 and player_pos[1] == player_pos_2[1] :
        running = False
    if player_pos[0] == player_pos_2[0] + player_size_2[0] and player_pos[1] == player_pos_2[1] :
        running = False
    
    
    screen.fill(violet)
    screen.blit(grid, grid_pos)
    screen.blit(player, player_pos)
    screen.blit(player_2, player_pos_2)
    pygame.display.flip()
    clock.tick(60)

pygame.quit