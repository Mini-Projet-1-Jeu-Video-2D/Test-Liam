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

traînées = {
    "type_x": 5,
    "type_y": 5,
    "color": "#F5FF00",
    "pos_x": player_pos[0],
    "pos_y": player_pos[1],
    "size_x": 5,
    "size_y": 5
}

t_q = ()
t_q_pos = []
t_q_size = []

t_d = ()
t_d_pos = []
t_d_size = []

t_z = ()
t_z_pos = []
t_z_size = []

t_s = ()
t_s_pos = []
t_s_size = []

t_left = ()
t_left_pos = []
t_left_size = []

t_right = ()
t_right_pos = []
t_right_size = []

t_up = ()
t_up_pos = []
t_up_size = []

t_down = ()
t_down_pos = []
t_down_size = []

traînées_finales = []
traînées_finales_pos = []



executing_lightcycle_movement_q = False
executing_lightcycle_movement_d = True
executing_lightcycle_movement_z = False
executing_lightcycle_movement_s = False

executing_lightcycle_movement_left = True
executing_lightcycle_movement_right = False
executing_lightcycle_movement_up = False
executing_lightcycle_movement_down = False


end_of_création_traînée_q = False
end_of_création_traînée_d = False
end_of_création_traînée_z = False
end_of_création_traînée_s = False

end_of_création_traînée_left = False
end_of_création_traînée_right = False
end_of_création_traînée_up = False
end_of_création_traînée_down = False



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


def création_traînée_GAUCHE(executing, traînées, player_pos_instant_0, player_pos_0, player_pos_1, end_of_création_traînée, traînées_finales, traînées_finales_pos) :
    if executing :
        traînée = traînées.copy()
        traînée = {
            "type_x": player_pos_instant_0 + 15 - player_pos_0 + 10,
            "type_y": 5,
            "color": "#F5FF00",
            "pos_x": player_pos_0 + 10,
            "pos_y": player_pos_1 + 10,
            "size_x": (player_pos_instant_0 + 15) - (player_pos_0 + 10),
            "size_y": 5
        }

        t = pygame.Surface((traînée["type_x"], traînée["type_y"]))
        t_pos = [traînée["pos_x"], traînée["pos_y"]]
        t_size = [traînée["size_x"], traînée["size_y"]]

    if end_of_création_traînée :
        traînées_finales.append(t)
        traînées_finales_pos.append(t_pos)

    return t, t_pos, t_size, traînées_finales, traînées_finales_pos

def création_traînée_DROITE(executing, traînées, player_pos_instant_0, player_pos_instant_1, player_pos_0, end_of_création_traînée, traînées_finales, traînées_finales_pos) :
    if executing :
        traînée = traînées.copy()
        traînée = {
            "type_x": player_pos_0 + 15 - player_pos_instant_0 + 10,
            "type_y": 5,
            "color": "#F5FF00",
            "pos_x": player_pos_instant_0,
            "pos_y": player_pos_instant_1 + 10,
            "size_x": (player_pos_0 + 15) - (player_pos_instant_0 + 10),
            "size_y": 5
        }

        t = pygame.Surface((traînée["type_x"], traînée["type_y"]))
        t_pos = [traînée["pos_x"], traînée["pos_y"]]
        t_size = [traînée["size_x"], traînée["size_y"]]

    if end_of_création_traînée :
        traînées_finales.append(t)
        traînées_finales_pos.append(t_pos)

    return t, t_pos, t_size, traînées_finales, traînées_finales_pos

def création_traînées_HAUT(executing, traînées, player_pos_instant_1, player_pos_1, player_pos_0, end_of_création_traînée, traînées_finales, traînées_finales_pos) :
    if executing :
        traînée = traînées.copy()
        traînée = {
            "type_x": 5,
            "type_y": player_pos_instant_1 + 15 - player_pos_1 + 10,
            "color": "#F5FF00",
            "pos_x": player_pos_0 + 10,
            "pos_y": player_pos_1 + 10,
            "size_x": (player_pos_instant_1 + 15) - (player_pos_1 + 10),
            "size_y": 5
        }

        t = pygame.Surface((traînée["type_x"], traînée["type_y"]))
        t_pos = [traînée["pos_x"], traînée["pos_y"]]
        t_size = [traînée["size_x"], traînée["size_y"]]

    if end_of_création_traînée :
        traînées_finales.append(t)
        traînées_finales_pos.append(t_pos)

    return t, t_pos, t_size, traînées_finales, traînées_finales_pos

def création_traînées_BAS(executing, traînées, player_pos_1, player_pos_instant_1, player_pos_instant_0, end_of_création_traînée, traînées_finales, traînées_finales_pos) :
    if executing :
        traînée = traînées.copy()
        traînée = {
            "type_x": 5,
            "type_y": player_pos_1 + 15 - player_pos_instant_1 + 10,
            "color": "#F5FF00",
            "pos_x": player_pos_instant_0 + 10,
            "pos_y": player_pos_instant_1 + 10,
            "size_x": (player_pos_1 + 15) - (player_pos_instant_1 + 10),
            "size_y": 5
        }

        t = pygame.Surface((traînée["type_x"], traînée["type_y"]))
        t_pos = [traînée["pos_x"], traînée["pos_y"]]
        t_size = [traînée["size_x"], traînée["size_y"]]

    if end_of_création_traînée :
        traînées_finales.append(t)
        traînées_finales_pos.append(t_pos)

    return t, t_pos, t_size, traînées_finales, traînées_finales_pos

time.sleep(1)



player_pos_instant = [player_pos[0], player_pos[1]]
player_pos_2_instant = [player_pos_2[0], player_pos_2[1]]



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
            if executing_lightcycle_movement_z :
                end_of_création_traînée_z = True
            if executing_lightcycle_movement_s :
                end_of_création_traînée_s = True
            
            executing_lightcycle_movement_z = False
            executing_lightcycle_movement_s = False

            executing_lightcycle_movement_q = True

            player_pos_instant = [player_pos[0], player_pos[1]]
        else :
            running = False
    if executing_lightcycle_movement_q :
        player_pos[0], running = lightcycle_movement_negative(player_pos[0], grid_pos[0], running)
        
    #-------------------------------------------------------------------------------D---------------------------------------------------------------------------
    
    if pressed_keys[K_d] and not pressed_keys[K_q] and not pressed_keys[K_z] and not pressed_keys[K_s] :
        if executing_lightcycle_movement_q == False or executing_lightcycle_movement_d == False :
            if executing_lightcycle_movement_z :
                end_of_création_traînée_z = True
            if executing_lightcycle_movement_s :
                end_of_création_traînée_s = True

            executing_lightcycle_movement_z = False
            executing_lightcycle_movement_s = False

            executing_lightcycle_movement_d = True

            player_pos_instant = [player_pos[0], player_pos[1]]
        else :
            running = False
    if executing_lightcycle_movement_d :
        player_pos[0], running = lightcycle_movement_positive(player_pos[0], screen_size[0], grid_size[0], player_size[0], running)

    #-------------------------------------------------------------------------------Z---------------------------------------------------------------------------

    if pressed_keys[K_z] and not pressed_keys[K_q] and not pressed_keys[K_d] and not pressed_keys[K_s] :
        if executing_lightcycle_movement_z == False or executing_lightcycle_movement_s == False :
            if executing_lightcycle_movement_q :
                end_of_création_traînée_q = True
            if executing_lightcycle_movement_d :
                end_of_création_traînée_d = True

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
            if executing_lightcycle_movement_q :
                end_of_création_traînée_q = True
            if executing_lightcycle_movement_d :
                end_of_création_traînée_d = True

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
            if executing_lightcycle_movement_up :
                end_of_création_traînée_up = True
            if executing_lightcycle_movement_down :
                end_of_création_traînée_down = True

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
            if executing_lightcycle_movement_up :
                end_of_création_traînée_up = True
            if executing_lightcycle_movement_down :
                end_of_création_traînée_down = True

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
            if executing_lightcycle_movement_left :
                end_of_création_traînée_left = True
            if executing_lightcycle_movement_right :
                end_of_création_traînée_right = True

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
            if executing_lightcycle_movement_left :
                end_of_création_traînée_left = True
            if executing_lightcycle_movement_right :
                end_of_création_traînée_right = True

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

    #---------------------------------------------------------------------------Joueur 1------------------------------------------------------------------------

    #-------------------------------------------------------------------------------Q---------------------------------------------------------------------------
    
    t_q, t_q_pos, t_q_size, traînées_finales, traînées_finales_pos = création_traînée_GAUCHE(executing_lightcycle_movement_q , traînées, player_pos_instant[0], player_pos[0], player_pos[1], end_of_création_traînée_q, traînées_finales, traînées_finales_pos)
        
    #-------------------------------------------------------------------------------D---------------------------------------------------------------------------
    
    t_d, t_d_pos, t_d_size, traînées_finales, traînées_finales_pos = création_traînée_DROITE(executing_lightcycle_movement_d, traînées, player_pos_instant[0], player_pos_instant[1], player_pos[0], end_of_création_traînée_d, traînées_finales, traînées_finales_pos)

    #-------------------------------------------------------------------------------Z---------------------------------------------------------------------------

    t_z, t_z_pos, t_z_size, traînées_finales, traînées_finales_pos = création_traînées_HAUT(executing_lightcycle_movement_z , traînées, player_pos_instant[1], player_pos[1], player_pos[0], end_of_création_traînée_z, traînées_finales, traînées_finales_pos)

    #-------------------------------------------------------------------------------S---------------------------------------------------------------------------
    
    t_s, t_s_pos, t_s_size, traînées_finales, traînées_finales_pos = création_traînées_BAS(executing_lightcycle_movement_s, traînées, player_pos[1], player_pos_instant[1], player_pos_instant[0], end_of_création_traînée_s, traînées_finales, traînées_finales_pos)


    #---------------------------------------------------------------------------Joueur 2------------------------------------------------------------------------

    #-----------------------------------------------------------------------------LEFT--------------------------------------------------------------------------
    
    t_left, t_left_pos, t_left_size, traînées_finales, traînées_finales_pos = création_traînée_GAUCHE(executing_lightcycle_movement_left , traînées, player_pos_2_instant[0], player_pos_2[0], player_pos_2[1], end_of_création_traînée_left, traînées_finales, traînées_finales_pos)

    #-----------------------------------------------------------------------------RIGHT-------------------------------------------------------------------------
    
    t_right, t_right_pos, t_right_size, traînées_finales, traînées_finales_pos = création_traînée_DROITE(executing_lightcycle_movement_right, traînées, player_pos_2_instant[0], player_pos_2_instant[1], player_pos_2[0], end_of_création_traînée_right, traînées_finales, traînées_finales_pos)

    #------------------------------------------------------------------------------UP---------------------------------------------------------------------------
    
    t_up, t_up_pos, t_up_size, traînées_finales, traînées_finales_pos = création_traînées_HAUT(executing_lightcycle_movement_up , traînées, player_pos_2_instant[1], player_pos_2[1], player_pos_2[0], end_of_création_traînée_up, traînées_finales, traînées_finales_pos)

    #-----------------------------------------------------------------------------DOWN--------------------------------------------------------------------------
    
    t_down, t_down_pos, t_down_size, traînées_finales, traînées_finales_pos = création_traînées_BAS(executing_lightcycle_movement_down, traînées, player_pos_2[1], player_pos_2_instant[1], player_pos_2_instant[0], end_of_création_traînée_down, traînées_finales, traînées_finales_pos)


    for i, j in traînées_finales, traînées_finales_pos :
        i.fill(traînées["color"])
        screen.blit(i, j)

    screen.blit(player, player_pos)
    screen.blit(player_2, player_pos_2)
    pygame.display.flip()
    clock.tick(60)

pygame.quit