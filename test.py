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
player_pos_instant = [player_pos[0], player_pos[1]]
player_size = [25, 25]

player_2 = pygame.Surface((25,25))
player_2.fill("#0000FF")
player_pos_2 = [1885, 585]
player_pos_2_instant = [player_pos_2[0], player_pos_2[1]]
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

t_q = None
t_q_pos = []
t_q_size = []

t_d = None
t_d_pos = []
t_d_size = []

t_z = None
t_z_pos = []
t_z_size = []

t_s = None
t_s_pos = []
t_s_size = []


t_left = None
t_left_pos = []
t_left_size = []

t_right = None
t_right_pos = []
t_right_size = []

t_up = None
t_up_pos = []
t_up_size = []

t_down = None
t_down_pos = []
t_down_size = []

traînées_finales_q = []
traînées_finales_pos_q = []

traînées_finales_d = []
traînées_finales_pos_d = []

traînées_finales_z = []
traînées_finales_pos_z = []

traînées_finales_s = []
traînées_finales_pos_s = []


traînées_finales_left = []
traînées_finales_pos_left = []

traînées_finales_right = []
traînées_finales_pos_right = []

traînées_finales_up = []
traînées_finales_pos_up = []

traînées_finales_down = []
traînées_finales_pos_down = []


executing_lightcycle_movement_q = False
executing_lightcycle_movement_d = True
executing_lightcycle_movement_z = False
executing_lightcycle_movement_s = False

executing_lightcycle_movement_left = True
executing_lightcycle_movement_right = False
executing_lightcycle_movement_up = False
executing_lightcycle_movement_down = False



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


def création_traînée_GAUCHE(executing, traînées, player_pos_instant_0, player_pos_0, player_pos_1, traînées_finales, traînées_finales_pos) :
    t = None
    t_pos = [5, 5]
    t_size = [5, 5]
    
    if executing :
        traînée = traînées.copy()
        traînée = {
            "type_x": player_pos_instant_0 - player_pos_0 + 5,
            "type_y": 5,
            "color": "#F5FF00",
            "pos_x": player_pos_0 + 10,
            "pos_y": player_pos_1 + 10,
            "size_x": player_pos_instant_0 - player_pos_0 + 5,
            "size_y": 5
        }

        t = pygame.Surface((traînée["type_x"], traînée["type_y"]))
        t_pos = [traînée["pos_x"], traînée["pos_y"]]
        t_size = [traînée["size_x"], traînée["size_y"]]

    if t is not None :
        traînées_finales.append(t)
        traînées_finales_pos.append(t_pos)

    return t_pos, t_size, traînées_finales, traînées_finales_pos

def création_traînée_DROITE(executing, traînées, player_pos_instant_0, player_pos_instant_1, player_pos_0, traînées_finales, traînées_finales_pos) :
    t = None
    t_pos = [5, 5]
    t_size = [5, 5]

    if executing :
        traînée = traînées.copy()
        traînée = {
            "type_x": player_pos_0 + 5 - player_pos_instant_0 + 5,
            "type_y": 5,
            "color": "#F5FF00",
            "pos_x": player_pos_instant_0 + 10,
            "pos_y": player_pos_instant_1 + 10,
            "size_x": player_pos_0 + 5 - player_pos_instant_0 + 5,
            "size_y": 5
        }

        t = pygame.Surface((traînée["type_x"], traînée["type_y"]))
        t_pos = [traînée["pos_x"], traînée["pos_y"]]
        t_size = [traînée["size_x"], traînée["size_y"]]

    if t is not None :
        traînées_finales.append(t)
        traînées_finales_pos.append(t_pos)

    return t_pos, t_size, traînées_finales, traînées_finales_pos

def création_traînées_HAUT(executing, traînées, player_pos_instant_1, player_pos_1, player_pos_0, traînées_finales, traînées_finales_pos) :
    t = None
    t_pos = [5, 5]
    t_size = [5, 5]

    if executing :
        traînée = traînées.copy()
        traînée = {
            "type_x": 5,
            "type_y": player_pos_instant_1 - player_pos_1 + 5,
            "color": "#F5FF00",
            "pos_x": player_pos_0 + 10,
            "pos_y": player_pos_1 + 10,
            "size_x": player_pos_instant_1 - player_pos_1 + 5,
            "size_y": 5
        }

        t = pygame.Surface((traînée["type_x"], traînée["type_y"]))
        t_pos = [traînée["pos_x"], traînée["pos_y"]]
        t_size = [traînée["size_x"], traînée["size_y"]]

    if t is not None :
        traînées_finales.append(t)
        traînées_finales_pos.append(t_pos)

    return t_pos, t_size, traînées_finales, traînées_finales_pos

def création_traînées_BAS(executing, traînées, player_pos_1, player_pos_instant_1, player_pos_instant_0, traînées_finales, traînées_finales_pos) :
    t = None
    t_pos = [5, 5]
    t_size = [5, 5]

    if executing :
        traînée = traînées.copy()
        traînée = {
            "type_x": 5,
            "type_y": player_pos_1 - player_pos_instant_1 + 5,
            "color": "#F5FF00",
            "pos_x": player_pos_instant_0 + 10,
            "pos_y": player_pos_instant_1 + 10,
            "size_x": player_pos_1 - player_pos_instant_1 + 5,
            "size_y": 5
        }

        t = pygame.Surface((traînée["type_x"], traînée["type_y"]))
        t_pos = [traînée["pos_x"], traînée["pos_y"]]
        t_size = [traînée["size_x"], traînée["size_y"]]

    if t is not None :
        traînées_finales.append(t)
        traînées_finales_pos.append(t_pos)

    return t_pos, t_size, traînées_finales, traînées_finales_pos



time.sleep(1)



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

            player_pos_instant = [player_pos[0], player_pos[1]]
        else :
            running = False
    if executing_lightcycle_movement_q :
        player_pos[0], running = lightcycle_movement_negative(player_pos[0], grid_pos[0], running)
        
    #-------------------------------------------------------------------------------D---------------------------------------------------------------------------
    
    if pressed_keys[K_d] and not pressed_keys[K_q] and not pressed_keys[K_z] and not pressed_keys[K_s] :
        if executing_lightcycle_movement_q == False or executing_lightcycle_movement_d == False :
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
            executing_lightcycle_movement_q = False
            executing_lightcycle_movement_d = False

            executing_lightcycle_movement_z = True

            player_pos_instant = [player_pos[0], player_pos[1]]
        else :
            running = False
    if executing_lightcycle_movement_z :
        player_pos[1], running = lightcycle_movement_negative(player_pos[1], grid_pos[1], running)

    #-------------------------------------------------------------------------------S---------------------------------------------------------------------------
    
    if pressed_keys[K_s] and not pressed_keys[K_q] and not pressed_keys[K_d] and not pressed_keys[K_z] :
        if executing_lightcycle_movement_z == False or executing_lightcycle_movement_s == False :
            executing_lightcycle_movement_q = False
            executing_lightcycle_movement_d = False

            executing_lightcycle_movement_s = True

            player_pos_instant = [player_pos[0], player_pos[1]]
        else :
            running = False
    if executing_lightcycle_movement_s :
        player_pos[1], running = lightcycle_movement_positive(player_pos[1], screen_size[1], grid_size[1], player_size[1], running)


    #-----------------------------------------------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------Joueur 2------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------

    #-----------------------------------------------------------------------------LEFT--------------------------------------------------------------------------
    
    if pressed_keys[K_LEFT] and not pressed_keys[K_RIGHT] and not pressed_keys[K_UP] and not pressed_keys[K_DOWN] :
        if executing_lightcycle_movement_left == False or executing_lightcycle_movement_right == False :
            executing_lightcycle_movement_up = False
            executing_lightcycle_movement_down = False

            executing_lightcycle_movement_left = True

            player_pos_2_instant = [player_pos_2[0], player_pos_2[1]]
        else :
            running = False
    if executing_lightcycle_movement_left :
        player_pos_2[0], running = lightcycle_movement_negative(player_pos_2[0], grid_pos[0], running)

    #-----------------------------------------------------------------------------RIGHT-------------------------------------------------------------------------
    
    if pressed_keys[K_RIGHT] and not pressed_keys[K_LEFT] and not pressed_keys[K_UP] and not pressed_keys[K_DOWN] :
        if executing_lightcycle_movement_left == False or executing_lightcycle_movement_right == False :
            executing_lightcycle_movement_up = False
            executing_lightcycle_movement_down = False

            executing_lightcycle_movement_right = True

            player_pos_2_instant = [player_pos_2[0], player_pos_2[1]]
        else :
            running = False
    if executing_lightcycle_movement_right :
        player_pos_2[0], running = lightcycle_movement_positive(player_pos_2[0], screen_size[0], grid_size[0], player_size_2[0], running)

    #------------------------------------------------------------------------------UP---------------------------------------------------------------------------
    
    if pressed_keys[K_UP] and not pressed_keys[K_LEFT] and not pressed_keys[K_RIGHT] and not pressed_keys[K_DOWN] :
        if executing_lightcycle_movement_up == False or executing_lightcycle_movement_down == False :
            executing_lightcycle_movement_left = False
            executing_lightcycle_movement_right = False

            executing_lightcycle_movement_up = True

            player_pos_2_instant = [player_pos_2[0], player_pos_2[1]]
        else :
            running = False
    if executing_lightcycle_movement_up :
        player_pos_2[1], running = lightcycle_movement_negative(player_pos_2[1], grid_pos[1], running)

    #-----------------------------------------------------------------------------DOWN--------------------------------------------------------------------------
    
    if pressed_keys[K_DOWN] and not pressed_keys[K_LEFT] and not pressed_keys[K_RIGHT] and not pressed_keys[K_UP] :
        if executing_lightcycle_movement_up == False or executing_lightcycle_movement_down == False :
            executing_lightcycle_movement_left = False
            executing_lightcycle_movement_right = False

            executing_lightcycle_movement_down = True

            player_pos_2_instant = [player_pos_2[0], player_pos_2[1]]
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
    #------------------------------------------------------------------------TRAÎNEES---------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------

    #---------------------------------------------------------------------------Joueur 1------------------------------------------------------------------------

    #-------------------------------------------------------------------------------Q---------------------------------------------------------------------------
    
    t_q_pos, t_q_size, traînées_finales_q, traînées_finales_pos_q = création_traînée_GAUCHE(executing_lightcycle_movement_q , traînées, player_pos_instant[0], player_pos[0], player_pos[1], traînées_finales_q, traînées_finales_pos_q)
    
    #-------------------------------------------------------------------------------D---------------------------------------------------------------------------
    
    t_d_pos, t_d_size, traînées_finales_d, traînées_finales_pos_d = création_traînée_DROITE(executing_lightcycle_movement_d, traînées, player_pos_instant[0], player_pos_instant[1], player_pos[0], traînées_finales_d, traînées_finales_pos_d)

    #-------------------------------------------------------------------------------Z---------------------------------------------------------------------------

    t_z_pos, t_z_size, traînées_finales_z, traînées_finales_pos_z = création_traînées_HAUT(executing_lightcycle_movement_z , traînées, player_pos_instant[1], player_pos[1], player_pos[0], traînées_finales_z, traînées_finales_pos_z)

    #-------------------------------------------------------------------------------S---------------------------------------------------------------------------
    
    t_s_pos, t_s_size, traînées_finales_s, traînées_finales_pos_s = création_traînées_BAS(executing_lightcycle_movement_s, traînées, player_pos[1], player_pos_instant[1], player_pos_instant[0], traînées_finales_s, traînées_finales_pos_s)


    #---------------------------------------------------------------------------Joueur 2------------------------------------------------------------------------

    #-----------------------------------------------------------------------------LEFT--------------------------------------------------------------------------
    
    t_left_pos, t_left_size, traînées_finales_left, traînées_finales_pos_left = création_traînée_GAUCHE(executing_lightcycle_movement_left , traînées, player_pos_2_instant[0], player_pos_2[0], player_pos_2[1], traînées_finales_left, traînées_finales_pos_left)

    #-----------------------------------------------------------------------------RIGHT-------------------------------------------------------------------------
    
    t_right_pos, t_right_size, traînées_finales_right, traînées_finales_pos_right = création_traînée_DROITE(executing_lightcycle_movement_right, traînées, player_pos_2_instant[0], player_pos_2_instant[1], player_pos_2[0], traînées_finales_right, traînées_finales_pos_right)

    #------------------------------------------------------------------------------UP---------------------------------------------------------------------------
    
    t_up_pos, t_up_size, traînées_finales_up, traînées_finales_pos_up = création_traînées_HAUT(executing_lightcycle_movement_up , traînées, player_pos_2_instant[1], player_pos_2[1], player_pos_2[0], traînées_finales_up, traînées_finales_pos_up)

    #-----------------------------------------------------------------------------DOWN--------------------------------------------------------------------------
    
    t_down_pos, t_down_size, traînées_finales_down, traînées_finales_pos_down = création_traînées_BAS(executing_lightcycle_movement_down, traînées, player_pos_2[1], player_pos_2_instant[1], player_pos_2_instant[0], traînées_finales_down, traînées_finales_pos_down)


    #-----------------------------------------------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------COLLISIONS TRAÎNEES-------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------

    if executing_lightcycle_movement_d :
        for i in traînées_finales_pos_z :
            if player_pos[0] + 25 >= i[0] and player_pos[0] + 20 <= i[0] and player_pos[1] - 24 >= traînées_finales_pos_z[-1][1] and player_pos[1] - 1 <= traînées_finales_pos_z[1][1] :
                running = False
        
        for i in traînées_finales_pos_s :
            if player_pos[0] + 25 >= i[0] and player_pos[0] + 20 <= i[0] and player_pos[1] - 24 >= traînées_finales_pos_s[1][1] and player_pos[1] - 1 <= traînées_finales_pos_s[-1][1] :
                running = False
        
        for i in traînées_finales_pos_up :
            if player_pos[0] + 25 >= i[0] and player_pos[0] + 20 <= i[0] and player_pos[1] - 24 >= traînées_finales_pos_up[-1][1] and player_pos[1] - 1 <= traînées_finales_pos_up[1][1] :
                running = False
        
        for i in traînées_finales_pos_down :
            if player_pos[0] + 25 >= i[0] and player_pos[0] + 20 <= i[0] and player_pos[1] - 24 >= traînées_finales_pos_down[1][1] and player_pos[1] - 1 <= traînées_finales_pos_down[-1][1] :
                running = False


    for i, j in zip(traînées_finales_q, traînées_finales_pos_q) :
        i.fill(traînées["color"])
        screen.blit(i, j)

    for i, j in zip(traînées_finales_d, traînées_finales_pos_d) :
        i.fill(traînées["color"])
        screen.blit(i, j)

    for i, j in zip(traînées_finales_z, traînées_finales_pos_z) :
        i.fill(traînées["color"])
        screen.blit(i, j)

    for i, j in zip(traînées_finales_s, traînées_finales_pos_s) :
        i.fill(traînées["color"])
        screen.blit(i, j)


    for i, j in zip(traînées_finales_left, traînées_finales_pos_left) :
        i.fill(traînées["color"])
        screen.blit(i, j)

    for i, j in zip(traînées_finales_right, traînées_finales_pos_right) :
        i.fill(traînées["color"])
        screen.blit(i, j)

    for i, j in zip(traînées_finales_up, traînées_finales_pos_up) :
        i.fill(traînées["color"])
        screen.blit(i, j)

    for i, j in zip(traînées_finales_down, traînées_finales_pos_down) :
        i.fill(traînées["color"])
        screen.blit(i, j)


    screen.blit(player, player_pos)
    screen.blit(player_2, player_pos_2)
    pygame.display.flip()
    clock.tick(60)

pygame.quit