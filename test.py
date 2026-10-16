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

traînée_q = {}

t_q = pygame.Surface((traînées["type_x"], traînées["type_y"]))
t_q.fill(traînées["color"])
t_q_pos = [traînées["pos_x"], traînées["pos_y"]]
t_q_size = [traînées["size_x"], traînées["size_y"]]

t_d = pygame.Surface((traînées["type_x"], traînées["type_y"]))
t_d.fill(traînées["color"])
t_d_pos = [traînées["pos_x"], traînées["pos_y"]]
t_d_size = [traînées["size_x"], traînées["size_y"]]

t_z = pygame.Surface((5,5))
t_z.fill("#F5FF00")
t_z_pos = [player_pos[0] + 10, player_pos[1]]
t_z_size = [5, 5]

t_s = pygame.Surface((5,5))
t_s.fill("#F5FF00")
t_s_pos = [player_pos[0] + 10, player_pos[1]]
t_s_size = [5, 5]

t_left = pygame.Surface((5,5))
t_left.fill("#F5FF00")
t_left_pos = [player_pos_2[0], player_pos_2[1] + 10]
t_left_size = [5, 5]

t_right = pygame.Surface((5,5))
t_right.fill("#F5FF00")
t_right_pos = [player_pos_2[0], player_pos_2[1] + 10]
t_right_size = [5, 5]

t_up = pygame.Surface((5,5))
t_up.fill("#F5FF00")
t_up_pos = [player_pos_2[0] + 10, player_pos_2[1]]
t_up_size = [5, 5]

t_down = pygame.Surface((5,5))
t_down.fill("#F5FF00")
t_down_pos = [player_pos_2[0] + 10, player_pos_2[1]]
t_down_size = [5, 5]

traînées_finales = []

def création_traînée_GAUCHE(executing, traînées, traînée, player_pos_instant, player_pos_0, player_pos_1, t, t_pos, t_size, traînées_finales) :
    if executing :
        traînée_q = traînées_q.copy()
        traînée_q = {
            "type_x": player_pos_instant - player_pos_0 + 25,
            "type_y": 5,
            "color": "#F5FF00",
            "pos_x": player_pos_0 + 25,
            "pos_y": player_pos_1 + 10,
            "size_x": player_pos_instant - (player_pos_0 + 25),
            "size_y": 5
        }

        t = pygame.Surface((traînée["type_x"], traînée["type_y"]))
        t.fill(traînée["color"])
        t_pos = [traînée["pos_x"], traînée["pos_y"]]
        t_size = [traînée["size_x"], traînée["size_y"]]
    else :
        traînées_finales.append(traînée)

def création_traînée_DROITE(executing, traînées, traînée, player_pos_instant_0, player_pos_instant_1, player_pos, t, t_pos, t_size, traînées_finales)
    if executing :
        traînée = traînées.copy()
        traînée = {
            "type_x": player_pos - player_pos_instant_0,
            "type_y": 5,
            "color": "#F5FF00",
            "pos_x": player_pos_instant_0,
            "pos_y": player_pos_instant_1 + 10,
            "size_x": player_pos - player_pos_instant_0,
            "size_y": 5
        }

        t = pygame.Surface((traînée["type_x"], traînée["type_y"]))
        t.fill(traînée["color"])
        t_pos = [traînée["pos_x"], traînée["pos_y"]]
        t_size = [traînée["size_x"], traînée["size_y"]]
    else :
        traînées_finales.append(traînée)

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

player_pos_instant = [player_pos[0], player_pos[1]]
player_pos__2instant = [player_pos_2[0], player_pos_2[1]]



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

    #---------------------------------------------------------------------------Joueur 1------------------------------------------------------------------------

    #-------------------------------------------------------------------------------Q---------------------------------------------------------------------------
    
    création_traînée_GAUCHE(executing_lightcycle_movement_q, traînées, traînée_q, player_pos_instant[0], player_pos[0], player_pos[1], t_q, t_q_pos, t_q_size, traînées_finales)
        
    #-------------------------------------------------------------------------------D---------------------------------------------------------------------------
    

    #-------------------------------------------------------------------------------Z---------------------------------------------------------------------------

    if executing_lightcycle_movement_q :
        traînée_q = traînées_q.copy()
        traînée_q = {
            "type_x": player_pos_instant[0] - player_pos[0] + 25,
            "type_y": 5,
            "color": "#F5FF00",
            "pos_x": player_pos[0] + 25,
            "pos_y": player_pos[1] + 10,
            "size_x": player_pos_instant[0] - (player_pos[0] + 25),
            "size_y": 5
        }

        t_q = pygame.Surface((traînée_q["type_x"], traînée_q["type_y"]))
        t_q.fill(traînée_q["color"])
        t_q_pos = [traînée_q["pos_x"], traînée_q["pos_y"]]
        t_q_size = [traînée_q["size_x"], traînée_q["size_y"]]

    #-------------------------------------------------------------------------------S---------------------------------------------------------------------------
    
    if executing_lightcycle_movement_q :
        traînée_q = traînées_q.copy()
        traînée_q = {
            "type_x": player_pos_instant[0] - player_pos[0] + 25,
            "type_y": 5,
            "color": "#F5FF00",
            "pos_x": player_pos[0] + 25,
            "pos_y": player_pos[1] + 10,
            "size_x": player_pos_instant[0] - (player_pos[0] + 25),
            "size_y": 5
        }

        t_q = pygame.Surface((traînée_q["type_x"], traînée_q["type_y"]))
        t_q.fill(traînée_q["color"])
        t_q_pos = [traînée_q["pos_x"], traînée_q["pos_y"]]
        t_q_size = [traînée_q["size_x"], traînée_q["size_y"]]


    #---------------------------------------------------------------------------Joueur 2------------------------------------------------------------------------

    #-----------------------------------------------------------------------------LEFT--------------------------------------------------------------------------
    
    if executing_lightcycle_movement_q :
        traînée_q = traînées_q.copy()
        traînée_q = {
            "type_x": player_pos_instant[0] - player_pos[0] + 25,
            "type_y": 5,
            "color": "#F5FF00",
            "pos_x": player_pos[0] + 25,
            "pos_y": player_pos[1] + 10,
            "size_x": player_pos_instant[0] - (player_pos[0] + 25),
            "size_y": 5
        }

        t_q = pygame.Surface((traînée_q["type_x"], traînée_q["type_y"]))
        t_q.fill(traînée_q["color"])
        t_q_pos = [traînée_q["pos_x"], traînée_q["pos_y"]]
        t_q_size = [traînée_q["size_x"], traînée_q["size_y"]]

    #-----------------------------------------------------------------------------RIGHT-------------------------------------------------------------------------
    
    if executing_lightcycle_movement_q :
        traînée_q = traînées_q.copy()
        traînée_q = {
            "type_x": player_pos_instant[0] - player_pos[0] + 25,
            "type_y": 5,
            "color": "#F5FF00",
            "pos_x": player_pos[0] + 25,
            "pos_y": player_pos[1] + 10,
            "size_x": player_pos_instant[0] - (player_pos[0] + 25),
            "size_y": 5
        }

        t_q = pygame.Surface((traînée_q["type_x"], traînée_q["type_y"]))
        t_q.fill(traînée_q["color"])
        t_q_pos = [traînée_q["pos_x"], traînée_q["pos_y"]]
        t_q_size = [traînée_q["size_x"], traînée_q["size_y"]]

    #------------------------------------------------------------------------------UP---------------------------------------------------------------------------
    
    if executing_lightcycle_movement_q :
        traînée_q = traînées_q.copy()
        traînée_q = {
            "type_x": player_pos_instant[0] - player_pos[0] + 25,
            "type_y": 5,
            "color": "#F5FF00",
            "pos_x": player_pos[0] + 25,
            "pos_y": player_pos[1] + 10,
            "size_x": player_pos_instant[0] - (player_pos[0] + 25),
            "size_y": 5
        }

        t_q = pygame.Surface((traînée_q["type_x"], traînée_q["type_y"]))
        t_q.fill(traînée_q["color"])
        t_q_pos = [traînée_q["pos_x"], traînée_q["pos_y"]]
        t_q_size = [traînée_q["size_x"], traînée_q["size_y"]]

    #-----------------------------------------------------------------------------DOWN--------------------------------------------------------------------------
    
    if executing_lightcycle_movement_q :
        traînée_q = traînées_q.copy()
        traînée_q = {
            "type_x": player_pos_instant[0] - player_pos[0] + 25,
            "type_y": 5,
            "color": "#F5FF00",
            "pos_x": player_pos[0] + 25,
            "pos_y": player_pos[1] + 10,
            "size_x": player_pos_instant[0] - (player_pos[0] + 25),
            "size_y": 5
        }

        t_q = pygame.Surface((traînée_q["type_x"], traînée_q["type_y"]))
        t_q.fill(traînée_q["color"])
        t_q_pos = [traînée_q["pos_x"], traînée_q["pos_y"]]
        t_q_size = [traînée_q["size_x"], traînée_q["size_y"]]

    for i in traînées_finales :
        screen.blit([pygame.Surface((i["type_x"], i["type_y"]))], [i["pos_x"], i["pos_y"]])


    screen.blit(player, player_pos)
    screen.blit(player_2, player_pos_2)
    pygame.display.flip()
    clock.tick(60)

pygame.quit