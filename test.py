import random
import os
import time
import pygame
from pygame.locals import (KEYDOWN, QUIT, K_ESCAPE, K_LEFT, K_RIGHT, K_UP, K_DOWN, K_q, K_d, K_z, K_s)
pygame.init()

dossier_script = os.path.dirname(__file__)
digital_7 = os.path.join(dossier_script, "assets", "fonts", "digital-7.ttf")
Technos = os.path.join(dossier_script, "assets", "fonts", "Technos.otf")
Score_Board_St = os.path.join(dossier_script, "assets", "fonts", "Score Board St.ttf")

resolution = pygame.display.Info()

screen = pygame.display.set_mode((resolution.current_w, resolution.current_h))
screen_size = [resolution.current_w, resolution.current_h]
violet = (37, 10, 105)

clock = pygame.time.Clock()

running = True

grid = pygame.Surface((screen_size[0] - 20, screen_size[1] - 110))
grid.fill("#0B041F")
grid_pos = [10, 100]
grid_size = [screen_size[0] - 20, screen_size[1] - 110]

player = pygame.Surface((25,25))
player.fill("#CF2F11")
player_pos = [grid_pos[0], grid_size[1] / 2 + 100]
player_pos_instant = [player_pos[0], player_pos[1]]
player_size = [25, 25]

player_2 = pygame.Surface((25,25))
player_2.fill("#0000FF")
player_pos_2 = [grid_pos[0] + grid_size[0] - 25, grid_size[1] / 2 + 100]
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
traînées_finales_size_q = []

traînées_finales_d = []
traînées_finales_pos_d = []
traînées_finales_size_d = []

traînées_finales_z = []
traînées_finales_pos_z = []
traînées_finales_size_z = []

traînées_finales_s = []
traînées_finales_pos_s = []
traînées_finales_size_s = []


traînées_finales_left = []
traînées_finales_pos_left = []
traînées_finales_size_left = []

traînées_finales_right = []
traînées_finales_pos_right = []
traînées_finales_size_right = []

traînées_finales_up = []
traînées_finales_pos_up = []
traînées_finales_size_up = []

traînées_finales_down = []
traînées_finales_pos_down = []
traînées_finales_size_down = []


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


def création_traînée_GAUCHE(executing, traînées, player_pos_instant_0, player_pos_0, player_pos_1, traînées_finales, traînées_finales_pos, traînées_finales_size) :
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
        traînées_finales_size.append(t_size)

    return traînées_finales, traînées_finales_pos, traînées_finales_size

def création_traînée_DROITE(executing, traînées, player_pos_instant_0, player_pos_instant_1, player_pos_0, traînées_finales, traînées_finales_pos, traînées_finales_size) :
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
        traînées_finales_size.append(t_size)

    return traînées_finales, traînées_finales_pos, traînées_finales_size

def création_traînées_HAUT(executing, traînées, player_pos_instant_1, player_pos_1, player_pos_0, traînées_finales, traînées_finales_pos, traînées_finales_size) :
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
            "size_x": 5,
            "size_y": player_pos_instant_1 - player_pos_1 + 5
        }

        t = pygame.Surface((traînée["type_x"], traînée["type_y"]))
        t_pos = [traînée["pos_x"], traînée["pos_y"]]
        t_size = [traînée["size_x"], traînée["size_y"]]

    if t is not None :
        traînées_finales.append(t)
        traînées_finales_pos.append(t_pos)
        traînées_finales_size.append(t_size)

    return traînées_finales, traînées_finales_pos, traînées_finales_size

def création_traînées_BAS(executing, traînées, player_pos_1, player_pos_instant_1, player_pos_instant_0, traînées_finales, traînées_finales_pos, traînées_finales_size) :
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
            "size_x": 5,
            "size_y": player_pos_1 - player_pos_instant_1 + 5
        }

        t = pygame.Surface((traînée["type_x"], traînée["type_y"]))
        t_pos = [traînée["pos_x"], traînée["pos_y"]]
        t_size = [traînée["size_x"], traînée["size_y"]]

    if t is not None :
        traînées_finales.append(t)
        traînées_finales_pos.append(t_pos)
        traînées_finales_size.append(t_size)

    return traînées_finales, traînées_finales_pos, traînées_finales_size


heures = 0
minutes = 0
secondes = 0

temps_total = 0

score_player = 0
score_player_2 = 0

score_attribué_player = False
score_attribué_player_2 = False

frôlements_de_la_mort_qui_tue_player = 0
frôlements_player = 0

frôlements_de_la_mort_qui_tue_player_2 = 0
frôlements_player_2 = 0

def frôlement_GAUCHE(executing, traînées_finales_pos, traînées_finales_size, traînées_finales_pos_2, traînées_finales_size_2, traînées_finales_pos_3, traînées_finales_size_3, traînées_finales_pos_4, traînées_finales_size_4, player_pos, score_attribué, score, frôlements, frôlements_de_la_mort_qui_tue) :
    if executing :
        for i, j in zip(traînées_finales_pos, traînées_finales_size) :
            if score_attribué == False :
                if player_pos[0] <= i[0] + j[0] + 5 and player_pos[0] >= i[0] + j[0] + 1 and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                    score += 50
                    frôlements_de_la_mort_qui_tue += 1
                    score_attribué = True
            if score_attribué == False :
                if player_pos[0] <= i[0] + j[0] + 10 and player_pos[0] >= i[0] + j[0] + 1 and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                    score += 10
                    frôlements += 1
                    score_attribué = True
        for i, j in zip(traînées_finales_pos_2, traînées_finales_size_2) :
            if score_attribué == False :
                if player_pos[0] <= i[0] + j[0] + 5 and player_pos[0] >= i[0] + j[0] + 1 and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                    score += 50
                    frôlements_de_la_mort_qui_tue += 1
                    score_attribué = True
            if score_attribué == False :
                if player_pos[0] <= i[0] + j[0] + 10 and player_pos[0] >= i[0] + j[0] + 1 and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                    score += 10
                    frôlements += 1
                    score_attribué = True
        for i, j in zip(traînées_finales_pos_3, traînées_finales_size_3) :
            if score_attribué == False :
                if player_pos[0] <= i[0] + j[0] + 5 and player_pos[0] >= i[0] + j[0] + 1 and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                    score += 50
                    frôlements_de_la_mort_qui_tue += 1
                    score_attribué = True
            if score_attribué == False :
                if player_pos[0] <= i[0] + j[0] + 10 and player_pos[0] >= i[0] + j[0] + 1 and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                    score += 10
                    frôlements += 1
                    score_attribué = True
        for i, j in zip(traînées_finales_pos_4, traînées_finales_size_4) :
            if score_attribué == False :
                if player_pos[0] <= i[0] + j[0] + 5 and player_pos[0] >= i[0] + j[0] + 1 and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                    score += 50
                    frôlements_de_la_mort_qui_tue += 1
                    score_attribué = True
            if score_attribué == False :
                if player_pos[0] <= i[0] + j[0] + 10 and player_pos[0] >= i[0] + j[0] + 1 and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                    score += 10
                    frôlements += 1
                    score_attribué = True

    return score, frôlements, frôlements_de_la_mort_qui_tue

def frôlement_DROITE(executing, traînées_finales_pos, traînées_finales_size, traînées_finales_pos_2, traînées_finales_size_2, traînées_finales_pos_3, traînées_finales_size_3, traînées_finales_pos_4, traînées_finales_size_4, player_pos, score_attribué, score, frôlements, frôlements_de_la_mort_qui_tue) :
    if executing :
        for i, j in zip(traînées_finales_pos, traînées_finales_size) :
            if score_attribué == False :
                if player_pos[0] + 25 >= i[0] - 5 and player_pos[0] + 25 <= i[0] - 1 and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                    score += 50
                    frôlements_de_la_mort_qui_tue += 1
                    score_attribué = True
            if score_attribué == False :
                if player_pos[0] + 25 >= i[0] - 10 and player_pos[0] + 25 <= i[0] - 1 and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                    score += 10
                    frôlements += 1
                    score_attribué = True
        for i, j in zip(traînées_finales_pos_2, traînées_finales_size_2) :
            if score_attribué == False :
                if player_pos[0] + 25 >= i[0] - 5 and player_pos[0] + 25 <= i[0] - 1 and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                    score += 50
                    frôlements_de_la_mort_qui_tue += 1
                    score_attribué = True
            if score_attribué == False :
                if player_pos[0] + 25 >= i[0] - 10 and player_pos[0] + 25 <= i[0] - 1 and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                    score += 10
                    frôlements += 1
                    score_attribué = True
        for i, j in zip(traînées_finales_pos_3, traînées_finales_size_3) :
            if score_attribué == False :
                if player_pos[0] + 25 >= i[0] - 5 and player_pos[0] + 25 <= i[0] - 1 and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                    score += 50
                    frôlements_de_la_mort_qui_tue += 1
                    score_attribué = True
            if score_attribué == False :
                if player_pos[0] + 25 >= i[0] - 10 and player_pos[0] + 25 <= i[0] - 1 and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                    score += 10
                    frôlements += 1
                    score_attribué = True
        for i, j in zip(traînées_finales_pos_4, traînées_finales_size_4) :
            if score_attribué == False :
                if player_pos[0] + 25 >= i[0] - 5 and player_pos[0] + 25 <= i[0] - 1 and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                    score += 50
                    frôlements_de_la_mort_qui_tue += 1
                    score_attribué = True
            if score_attribué == False :
                if player_pos[0] + 25 >= i[0] - 10 and player_pos[0] + 25 <= i[0] - 1 and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                    score += 10
                    frôlements += 1
                    score_attribué = True

    return score, frôlements, frôlements_de_la_mort_qui_tue

def frôlement_HAUT(executing, traînées_finales_pos, traînées_finales_size, traînées_finales_pos_2, traînées_finales_size_2, traînées_finales_pos_3, traînées_finales_size_3, traînées_finales_pos_4, traînées_finales_size_4, player_pos, score_attribué, score, frôlements, frôlements_de_la_mort_qui_tue) :
    if executing :
        for i, j in zip(traînées_finales_pos, traînées_finales_size) :
            if score_attribué == False :
                if player_pos[1] <= i[1] + j[1] + 5 and player_pos[1] >= i[1] + j[1] + 1 and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                    score += 50
                    frôlements_de_la_mort_qui_tue += 1
                    score_attribué = True
            if score_attribué == False :
                if player_pos[1] <= i[1] + j[1] + 10 and player_pos[1] >= i[1] + j[1] + 1 and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                    score += 10
                    frôlements += 1
                    score_attribué = True
        for i, j in zip(traînées_finales_pos_2, traînées_finales_size_2) :
            if score_attribué == False :
                if player_pos[1] <= i[1] + j[1] + 5 and player_pos[1] >= i[1] + j[1] + 1 and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                    score += 50
                    frôlements_de_la_mort_qui_tue += 1
                    score_attribué = True
            if score_attribué == False :
                if player_pos[1] <= i[1] + j[1] + 10 and player_pos[1] >= i[1] + j[1] + 1 and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                    score += 10
                    frôlements += 1
                    score_attribué = True
        for i, j in zip(traînées_finales_pos_3, traînées_finales_size_3) :
            if score_attribué == False :
                if player_pos[1] <= i[1] + j[1] + 5 and player_pos[1] >= i[1] + j[1] + 1 and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                    score += 50
                    frôlements_de_la_mort_qui_tue += 1
                    score_attribué = True
            if score_attribué == False :
                if player_pos[1] <= i[1] + j[1] + 10 and player_pos[1] >= i[1] + j[1] + 1 and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                    score += 10
                    frôlements += 1
                    score_attribué = True
        for i, j in zip(traînées_finales_pos_4, traînées_finales_size_4) :
            if score_attribué == False :
                if player_pos[1] <= i[1] + j[1] + 5 and player_pos[1] >= i[1] + j[1] + 1 and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                    score += 50
                    frôlements_de_la_mort_qui_tue += 1
                    score_attribué = True
            if score_attribué == False :
                if player_pos[1] <= i[1] + j[1] + 10 and player_pos[1] >= i[1] + j[1] + 1 and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                    score += 10
                    frôlements += 1
                    score_attribué = True

    return score, frôlements, frôlements_de_la_mort_qui_tue

def frôlement_BAS(executing, traînées_finales_pos, traînées_finales_size, traînées_finales_pos_2, traînées_finales_size_2, traînées_finales_pos_3, traînées_finales_size_3, traînées_finales_pos_4, traînées_finales_size_4, player_pos, score_attribué, score, frôlements, frôlements_de_la_mort_qui_tue) :
    if executing :
        for i, j in zip(traînées_finales_pos, traînées_finales_size) :
            if score_attribué == False :
                if player_pos[1] + 25 >= i[1] - 5 and player_pos[1] + 25 <= i[1] - 1 and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                    score += 50
                    frôlements_de_la_mort_qui_tue += 1
                    score_attribué = True
            if score_attribué == False :
                if player_pos[1] + 25 >= i[1] - 10 and player_pos[1] + 25 <= i[1] - 1 and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                    score += 10
                    frôlements += 1
                    score_attribué = True
        for i, j in zip(traînées_finales_pos_2, traînées_finales_size_2) :
            if score_attribué == False :
                if player_pos[1] + 25 >= i[1] - 5 and player_pos[1] + 25 <= i[1] - 1 and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                    score += 50
                    frôlements_de_la_mort_qui_tue += 1
                    score_attribué = True
            if score_attribué == False :
                if player_pos[1] + 25 >= i[1] - 10 and player_pos[1] + 25 <= i[1] - 1 and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                    score += 10
                    frôlements += 1
                    score_attribué = True
        for i, j in zip(traînées_finales_pos_3, traînées_finales_size_3) :
            if score_attribué == False :
                if player_pos[1] + 25 >= i[1] - 5 and player_pos[1] + 25 <= i[1] - 1 and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                    score += 50
                    frôlements_de_la_mort_qui_tue += 1
                    score_attribué = True
            if score_attribué == False :
                if player_pos[1] + 25 >= i[1] - 10 and player_pos[1] + 25 <= i[1] - 1 and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                    score += 10
                    frôlements += 1
                    score_attribué = True
        for i, j in zip(traînées_finales_pos_4, traînées_finales_size_4) :
            if score_attribué == False :
                if player_pos[1] + 25 >= i[1] - 5 and player_pos[1] + 25 <= i[1] - 1 and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                    score += 50
                    frôlements_de_la_mort_qui_tue += 1
                    score_attribué = True
            if score_attribué == False :
                if player_pos[1] + 25 >= i[1] - 10 and player_pos[1] + 25 <= i[1] - 1 and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                    score += 10
                    frôlements += 1
                    score_attribué = True

    return score, frôlements, frôlements_de_la_mort_qui_tue


collectibles = pygame.Surface((15,15))
collectibles.fill("#346910")
collectibles_pos = [random.randint(grid_pos[0], grid_pos[0] + grid_size[0] - 15), random.randint(grid_pos[1], grid_pos[1] + grid_size[1] - 15)]
collectibles_size = [15, 15]

collectibles_player = 0
collectibles_player_2 = 0

def réapparition_collectibles(executing_GAUCHE, executing_DROITE, executing_HAUT, executing_BAS, grid_pos, grid_size, player_pos, player_size, collectibles_pos, collectibles_size, collectibles, score) :
    if executing_GAUCHE :
        if player_pos[0] <= collectibles_pos[0] + collectibles_size[0] and player_pos[0] >= collectibles_pos[0] and player_pos[1] + 24 >= collectibles_pos[1] and player_pos[1] - 1 <= collectibles_pos[1] + collectibles_size[1] :
            score += 50
            collectibles += 1
            collectibles_pos = [random.randint(grid_pos[0], grid_pos[0] + grid_size[0] - 15), random.randint(grid_pos[1], grid_pos[1] + grid_size[1] - 15)]
    if executing_DROITE :
        if player_pos[0] + player_size[0] >= collectibles_pos[0] and player_pos[0] + player_size[0] <= collectibles_pos[0] + collectibles_size[0] and player_pos[1] + 24 >= collectibles_pos[1] and player_pos[1] - 1 <= collectibles_pos[1] + collectibles_size[1] :
            score += 50
            collectibles += 1
            collectibles_pos = [random.randint(grid_pos[0], grid_pos[0] + grid_size[0] - 15), random.randint(grid_pos[1], grid_pos[1] + grid_size[1] - 15)]
    if executing_HAUT :
        if player_pos[1] <= collectibles_pos[1] + collectibles_size[1] and player_pos[1] >= collectibles_pos[1] and player_pos[0] + 24 >= collectibles_pos[0] and player_pos[0] - 1 <= collectibles_pos[0] + collectibles_size[0] :
            score += 50
            collectibles += 1
            collectibles_pos = [random.randint(grid_pos[0], grid_pos[0] + grid_size[0] - 15), random.randint(grid_pos[1], grid_pos[1] + grid_size[1] - 15)]
    if executing_BAS :
        if player_pos[1] + player_size[1] >= collectibles_pos[1] and player_pos[1] + player_size[1] <= collectibles_pos[1] + collectibles_size[1] and player_pos[0] + 24 >= collectibles_pos[0] and player_pos[0] - 1 <= collectibles_pos[0] + collectibles_size[0] :
            score += 50
            collectibles += 1
            collectibles_pos = [random.randint(grid_pos[0], grid_pos[0] + grid_size[0] - 15), random.randint(grid_pos[1], grid_pos[1] + grid_size[1] - 15)]

    return score, collectibles, collectibles_pos



succès_temps_1_player = False
succès_temps_2_player = False
succès_temps_3_player = False
succès_temps_caché_player = False

succès_score_1_player = False
succès_score_2_player = False
succès_score_3_player = False
succès_score_caché_player = False

succès_frôlements_1_player = False
succès_frôlements_2_player = False
succès_frôlements_3_player = False
succès_frôlements_caché_player = False

succès_collectibles_1_player = False
succès_collectibles_2_player = False
succès_collectibles_3_player = False
succès_collectibles_caché_player = False


succès_temps_1_player_2 = False
succès_temps_2_player_2 = False
succès_temps_3_player_2 = False
succès_temps_caché_player_2 = False

succès_score_1_player_2 = False
succès_score_2_player_2 = False
succès_score_3_player_2 = False
succès_score_caché_player_2 = False

succès_frôlements_1_player_2 = False
succès_frôlements_2_player_2 = False
succès_frôlements_3_player_2 = False
succès_frôlements_caché_player_2 = False

succès_collectibles_1_player_2 = False
succès_collectibles_2_player_2 = False
succès_collectibles_3_player_2 = False
succès_collectibles_caché_player_2 = False

def succès_temps(temps_total, succès_temps_1_player, succès_temps_1_player_2, succès_temps_2_player, succès_temps_2_player_2, succès_temps_3_player, succès_temps_3_player_2, succès_temps_caché_player, succès_temps_caché_player_2) :
    if temps_total >= 30 :
        succès_temps_1_player = True
        succès_temps_1_player_2 = True

    if temps_total >= 60 :
        succès_temps_2_player = True
        succès_temps_2_player_2 = True

    if temps_total >= 150 :
        succès_temps_3_player = True
        succès_temps_3_player_2 = True

    if temps_total >= 300 :
        succès_temps_caché_player = True
        succès_temps_caché_player_2 = True

    return succès_temps_1_player, succès_temps_1_player_2, succès_temps_2_player, succès_temps_2_player_2, succès_temps_3_player, succès_temps_3_player_2, succès_temps_caché_player, succès_temps_caché_player_2

def succès_score(score_player, succès_score_1, succès_score_2, succès_score_3, succès_score_caché) :
    if score_player >= 100 :
        succès_score_1 = True
    
    if score_player >= 500 :
        succès_score_2 = True

    if score_player >= 1000 :
        succès_score_3 = True

    if score_player >= 8888 :
        succès_score_caché = True

    return succès_score_1, succès_score_2, succès_score_3, succès_score_caché

def succès_frôlements(frôlements_player, succès_frôlements_1, succès_frôlements_2, succès_frôlements_3, succès_frôlements_caché) :
    if frôlements_player >= 5 :
        succès_frôlements_1 = True

    if frôlements_player >= 10 :
        succès_frôlements_2 = True

    if frôlements_player >= 25 :
        succès_frôlements_3 = True

    if frôlements_player >= 50 :
        succès_frôlements_caché = True

    return succès_frôlements_1, succès_frôlements_2, succès_frôlements_3, succès_frôlements_caché

def succès_collectibles(collectibles_player, succès_collectibles_1, succès_collectibles_2, succès_collectibles_3, succès_collectibles_caché) :
    if collectibles_player >= 1 :
        succès_collectibles_1 = True

    if collectibles_player >= 5 :
        succès_collectibles_2 = True

    if collectibles_player >= 10 :
        succès_collectibles_3 = True

    if collectibles_player >= 25 :
        succès_collectibles_caché = True

    return succès_collectibles_1, succès_collectibles_2, succès_collectibles_3, succès_collectibles_caché



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
            score_player, frôlements_player, frôlements_de_la_mort_qui_tue_player = frôlement_HAUT(executing_lightcycle_movement_z, traînées_finales_pos_q, traînées_finales_size_q, traînées_finales_pos_d, traînées_finales_size_d, traînées_finales_pos_left, traînées_finales_size_left, traînées_finales_pos_right, traînées_finales_size_right, player_pos, score_attribué_player, score_player, frôlements_player, frôlements_de_la_mort_qui_tue_player)
            score_player, frôlements_player, frôlements_de_la_mort_qui_tue_player = frôlement_BAS(executing_lightcycle_movement_s, traînées_finales_pos_q, traînées_finales_size_q, traînées_finales_pos_d, traînées_finales_size_d, traînées_finales_pos_left, traînées_finales_size_left, traînées_finales_pos_right, traînées_finales_size_right, player_pos, score_attribué_player, score_player, frôlements_player, frôlements_de_la_mort_qui_tue_player)
            
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
            score_player, frôlements_player, frôlements_de_la_mort_qui_tue_player = frôlement_HAUT(executing_lightcycle_movement_z, traînées_finales_pos_q, traînées_finales_size_q, traînées_finales_pos_d, traînées_finales_size_d, traînées_finales_pos_left, traînées_finales_size_left, traînées_finales_pos_right, traînées_finales_size_right, player_pos, score_attribué_player, score_player, frôlements_player, frôlements_de_la_mort_qui_tue_player)
            score_player, frôlements_player, frôlements_de_la_mort_qui_tue_player = frôlement_BAS(executing_lightcycle_movement_s, traînées_finales_pos_q, traînées_finales_size_q, traînées_finales_pos_d, traînées_finales_size_d, traînées_finales_pos_left, traînées_finales_size_left, traînées_finales_pos_right, traînées_finales_size_right, player_pos, score_attribué_player, score_player, frôlements_player, frôlements_de_la_mort_qui_tue_player)
            
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
            score_player, frôlements_player, frôlements_de_la_mort_qui_tue_player = frôlement_GAUCHE(executing_lightcycle_movement_q, traînées_finales_pos_z, traînées_finales_size_z, traînées_finales_pos_s, traînées_finales_size_s, traînées_finales_pos_up, traînées_finales_size_up, traînées_finales_pos_down, traînées_finales_size_down, player_pos, score_attribué_player, score_player, frôlements_player, frôlements_de_la_mort_qui_tue_player)
            score_player, frôlements_player, frôlements_de_la_mort_qui_tue_player = frôlement_DROITE(executing_lightcycle_movement_d, traînées_finales_pos_z, traînées_finales_size_z, traînées_finales_pos_s, traînées_finales_size_s, traînées_finales_pos_up, traînées_finales_size_up, traînées_finales_pos_down, traînées_finales_size_down, player_pos, score_attribué_player, score_player, frôlements_player, frôlements_de_la_mort_qui_tue_player)
            
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
            score_player, frôlements_player, frôlements_de_la_mort_qui_tue_player = frôlement_GAUCHE(executing_lightcycle_movement_q, traînées_finales_pos_z, traînées_finales_size_z, traînées_finales_pos_s, traînées_finales_size_s, traînées_finales_pos_up, traînées_finales_size_up, traînées_finales_pos_down, traînées_finales_size_down, player_pos, score_attribué_player, score_player, frôlements_player, frôlements_de_la_mort_qui_tue_player)
            score_player, frôlements_player, frôlements_de_la_mort_qui_tue_player = frôlement_DROITE(executing_lightcycle_movement_d, traînées_finales_pos_z, traînées_finales_size_z, traînées_finales_pos_s, traînées_finales_size_s, traînées_finales_pos_up, traînées_finales_size_up, traînées_finales_pos_down, traînées_finales_size_down, player_pos, score_attribué_player, score_player, frôlements_player, frôlements_de_la_mort_qui_tue_player)

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
            score_player_2, frôlements_player_2, frôlements_de_la_mort_qui_tue_player_2 = frôlement_HAUT(executing_lightcycle_movement_up, traînées_finales_pos_q, traînées_finales_size_q, traînées_finales_pos_d, traînées_finales_size_d, traînées_finales_pos_left, traînées_finales_size_left, traînées_finales_pos_right, traînées_finales_size_right, player_pos_2, score_attribué_player_2, score_player_2, frôlements_player_2, frôlements_de_la_mort_qui_tue_player_2)
            score_player_2, frôlements_player_2, frôlements_de_la_mort_qui_tue_player_2 = frôlement_BAS(executing_lightcycle_movement_down, traînées_finales_pos_q, traînées_finales_size_q, traînées_finales_pos_d, traînées_finales_size_d, traînées_finales_pos_left, traînées_finales_size_left, traînées_finales_pos_right, traînées_finales_size_right, player_pos_2, score_attribué_player_2, score_player_2, frôlements_player_2, frôlements_de_la_mort_qui_tue_player_2)

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
            score_player_2, frôlements_player_2, frôlements_de_la_mort_qui_tue_player_2 = frôlement_HAUT(executing_lightcycle_movement_up, traînées_finales_pos_q, traînées_finales_size_q, traînées_finales_pos_d, traînées_finales_size_d, traînées_finales_pos_left, traînées_finales_size_left, traînées_finales_pos_right, traînées_finales_size_right, player_pos_2, score_attribué_player_2, score_player_2, frôlements_player_2, frôlements_de_la_mort_qui_tue_player_2)
            score_player_2, frôlements_player_2, frôlements_de_la_mort_qui_tue_player_2 = frôlement_BAS(executing_lightcycle_movement_down, traînées_finales_pos_q, traînées_finales_size_q, traînées_finales_pos_d, traînées_finales_size_d, traînées_finales_pos_left, traînées_finales_size_left, traînées_finales_pos_right, traînées_finales_size_right, player_pos_2, score_attribué_player_2, score_player_2, frôlements_player_2, frôlements_de_la_mort_qui_tue_player_2)

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
            score_player_2, frôlements_player_2, frôlements_de_la_mort_qui_tue_player_2 = frôlement_GAUCHE(executing_lightcycle_movement_left, traînées_finales_pos_z, traînées_finales_size_z, traînées_finales_pos_s, traînées_finales_size_s, traînées_finales_pos_up, traînées_finales_size_up, traînées_finales_pos_down, traînées_finales_size_down, player_pos_2, score_attribué_player_2, score_player_2, frôlements_player_2, frôlements_de_la_mort_qui_tue_player_2)
            score_player_2, frôlements_player_2, frôlements_de_la_mort_qui_tue_player_2 = frôlement_DROITE(executing_lightcycle_movement_right, traînées_finales_pos_z, traînées_finales_size_z, traînées_finales_pos_s, traînées_finales_size_s, traînées_finales_pos_up, traînées_finales_size_up, traînées_finales_pos_down, traînées_finales_size_down, player_pos_2, score_attribué_player_2, score_player_2, frôlements_player_2, frôlements_de_la_mort_qui_tue_player_2)

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
            score_player_2, frôlements_player_2, frôlements_de_la_mort_qui_tue_player_2 = frôlement_GAUCHE(executing_lightcycle_movement_left, traînées_finales_pos_z, traînées_finales_size_z, traînées_finales_pos_s, traînées_finales_size_s, traînées_finales_pos_up, traînées_finales_size_up, traînées_finales_pos_down, traînées_finales_size_down, player_pos_2, score_attribué_player_2, score_player_2, frôlements_player_2, frôlements_de_la_mort_qui_tue_player_2)
            score_player_2, frôlements_player_2, frôlements_de_la_mort_qui_tue_player_2 = frôlement_DROITE(executing_lightcycle_movement_right, traînées_finales_pos_z, traînées_finales_size_z, traînées_finales_pos_s, traînées_finales_size_s, traînées_finales_pos_up, traînées_finales_size_up, traînées_finales_pos_down, traînées_finales_size_down, player_pos_2, score_attribué_player_2, score_player_2, frôlements_player_2, frôlements_de_la_mort_qui_tue_player_2)

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
    
    traînées_finales_q, traînées_finales_pos_q, traînées_finales_size_q = création_traînée_GAUCHE(executing_lightcycle_movement_q , traînées, player_pos_instant[0], player_pos[0], player_pos[1], traînées_finales_q, traînées_finales_pos_q, traînées_finales_size_q)
    
    #-------------------------------------------------------------------------------D---------------------------------------------------------------------------
    
    traînées_finales_d, traînées_finales_pos_d, traînées_finales_size_d = création_traînée_DROITE(executing_lightcycle_movement_d, traînées, player_pos_instant[0], player_pos_instant[1], player_pos[0], traînées_finales_d, traînées_finales_pos_d, traînées_finales_size_d)

    #-------------------------------------------------------------------------------Z---------------------------------------------------------------------------

    traînées_finales_z, traînées_finales_pos_z, traînées_finales_size_z = création_traînées_HAUT(executing_lightcycle_movement_z , traînées, player_pos_instant[1], player_pos[1], player_pos[0], traînées_finales_z, traînées_finales_pos_z, traînées_finales_size_z)

    #-------------------------------------------------------------------------------S---------------------------------------------------------------------------
    
    traînées_finales_s, traînées_finales_pos_s, traînées_finales_size_s = création_traînées_BAS(executing_lightcycle_movement_s, traînées, player_pos[1], player_pos_instant[1], player_pos_instant[0], traînées_finales_s, traînées_finales_pos_s, traînées_finales_size_s)


    #---------------------------------------------------------------------------Joueur 2------------------------------------------------------------------------

    #-----------------------------------------------------------------------------LEFT--------------------------------------------------------------------------
    
    traînées_finales_left, traînées_finales_pos_left, traînées_finales_size_left = création_traînée_GAUCHE(executing_lightcycle_movement_left , traînées, player_pos_2_instant[0], player_pos_2[0], player_pos_2[1], traînées_finales_left, traînées_finales_pos_left, traînées_finales_size_left)

    #-----------------------------------------------------------------------------RIGHT-------------------------------------------------------------------------
    
    traînées_finales_right, traînées_finales_pos_right, traînées_finales_size_right = création_traînée_DROITE(executing_lightcycle_movement_right, traînées, player_pos_2_instant[0], player_pos_2_instant[1], player_pos_2[0], traînées_finales_right, traînées_finales_pos_right, traînées_finales_size_right)

    #------------------------------------------------------------------------------UP---------------------------------------------------------------------------
    
    traînées_finales_up, traînées_finales_pos_up, traînées_finales_size_up = création_traînées_HAUT(executing_lightcycle_movement_up , traînées, player_pos_2_instant[1], player_pos_2[1], player_pos_2[0], traînées_finales_up, traînées_finales_pos_up, traînées_finales_size_up)

    #-----------------------------------------------------------------------------DOWN--------------------------------------------------------------------------
    
    traînées_finales_down, traînées_finales_pos_down, traînées_finales_size_down = création_traînées_BAS(executing_lightcycle_movement_down, traînées, player_pos_2[1], player_pos_2_instant[1], player_pos_2_instant[0], traînées_finales_down, traînées_finales_pos_down, traînées_finales_size_down)


    #-----------------------------------------------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------COLLISIONS TRAÎNEES-------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------

    #---------------------------------------------------------------------------Joueur 1------------------------------------------------------------------------
    
    #-------------------------------------------------------------------------------Q---------------------------------------------------------------------------

    if executing_lightcycle_movement_q :
        for i, j in zip(traînées_finales_pos_z, traînées_finales_size_z) :
            if player_pos[0] <= i[0] + 5 and player_pos[0] >= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                running = False
        
        for i, j in zip(traînées_finales_pos_s, traînées_finales_size_s) :
            if player_pos[0] <= i[0] + 5 and player_pos[0] >= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                running = False
        
        for i, j in zip(traînées_finales_pos_up, traînées_finales_size_up) :
            if player_pos[0] <= i[0] + 5 and player_pos[0] >= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                running = False
        
        for i, j in zip(traînées_finales_pos_down, traînées_finales_size_down) :
            if player_pos[0] <= i[0] + 5 and player_pos[0] >= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                running = False

    #-------------------------------------------------------------------------------D---------------------------------------------------------------------------

    if executing_lightcycle_movement_d :
        for i, j in zip(traînées_finales_pos_z, traînées_finales_size_z) :
            if player_pos[0] + 25 >= i[0] and player_pos[0] + 20 <= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                running = False
        
        for i, j in zip(traînées_finales_pos_s, traînées_finales_size_s) :
            if player_pos[0] + 25 >= i[0] and player_pos[0] + 20 <= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                running = False
        
        for i, j in zip(traînées_finales_pos_up, traînées_finales_size_up) :
            if player_pos[0] + 25 >= i[0] and player_pos[0] + 20 <= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                running = False
        
        for i, j in zip(traînées_finales_pos_down, traînées_finales_size_down) :
            if player_pos[0] + 25 >= i[0] and player_pos[0] + 20 <= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                running = False

    #-------------------------------------------------------------------------------Z---------------------------------------------------------------------------

    if executing_lightcycle_movement_z :
        for i, j in zip(traînées_finales_pos_q, traînées_finales_size_q) :
            if player_pos[1] <= i[1] + 5 and player_pos[1] >= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                running = False
        
        for i, j in zip(traînées_finales_pos_d, traînées_finales_size_d) :
            if player_pos[1] <= i[1] + 5 and player_pos[1] >= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                running = False
        
        for i, j in zip(traînées_finales_pos_left, traînées_finales_size_left) :
            if player_pos[1] <= i[1] + 5 and player_pos[1] >= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                running = False
        
        for i, j in zip(traînées_finales_pos_right, traînées_finales_size_right) :
            if player_pos[1] <= i[1] + 5 and player_pos[1] >= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                running = False

    #-------------------------------------------------------------------------------S---------------------------------------------------------------------------

    if executing_lightcycle_movement_s :
        for i, j in zip(traînées_finales_pos_q, traînées_finales_size_q) :
            if player_pos[1] + 25 >= i[1] and player_pos[1] + 20 <= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                running = False
        
        for i, j in zip(traînées_finales_pos_d, traînées_finales_size_d) :
            if player_pos[1] + 25 >= i[1] and player_pos[1] + 20 <= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                running = False
        
        for i, j in zip(traînées_finales_pos_left, traînées_finales_size_left) :
            if player_pos[1] + 25 >= i[1] and player_pos[1] + 20 <= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                running = False
        
        for i, j in zip(traînées_finales_pos_right, traînées_finales_size_right) :
            if player_pos[1] + 25 >= i[1] and player_pos[1] + 20 <= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                running = False


    #---------------------------------------------------------------------------Joueur 2------------------------------------------------------------------------

    #-----------------------------------------------------------------------------LEFT--------------------------------------------------------------------------

    if executing_lightcycle_movement_left :
        for i, j in zip(traînées_finales_pos_z, traînées_finales_size_z) :
            if player_pos_2[0] <= i[0] + 5 and player_pos_2[0] >= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                running = False
        
        for i, j in zip(traînées_finales_pos_s, traînées_finales_size_s) :
            if player_pos_2[0] <= i[0] + 5 and player_pos_2[0] >= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                running = False
        
        for i, j in zip(traînées_finales_pos_up, traînées_finales_size_up) :
            if player_pos_2[0] <= i[0] + 5 and player_pos_2[0] >= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                running = False
        
        for i, j in zip(traînées_finales_pos_down, traînées_finales_size_down) :
            if player_pos_2[0] <= i[0] + 5 and player_pos_2[0] >= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                running = False

    #-----------------------------------------------------------------------------RIGHT-------------------------------------------------------------------------

    if executing_lightcycle_movement_right :
        for i, j in zip(traînées_finales_pos_z, traînées_finales_size_z) :
            if player_pos_2[0] + 25 >= i[0] and player_pos_2[0] + 20 <= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                running = False
        
        for i, j in zip(traînées_finales_pos_s, traînées_finales_size_s) :
            if player_pos_2[0] + 25 >= i[0] and player_pos_2[0] + 20 <= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                running = False
        
        for i, j in zip(traînées_finales_pos_up, traînées_finales_size_up) :
            if player_pos_2[0] + 25 >= i[0] and player_pos_2[0] + 20 <= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                running = False
        
        for i, j in zip(traînées_finales_pos_down, traînées_finales_size_down) :
            if player_pos_2[0] + 25 >= i[0] and player_pos_2[0] + 20 <= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                running = False

    #------------------------------------------------------------------------------UP---------------------------------------------------------------------------

    if executing_lightcycle_movement_up :
        for i, j in zip(traînées_finales_pos_q, traînées_finales_size_q) :
            if player_pos_2[1] <= i[1] + 5 and player_pos_2[1] >= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                running = False
        
        for i, j in zip(traînées_finales_pos_d, traînées_finales_size_d) :
            if player_pos_2[1] <= i[1] + 5 and player_pos_2[1] >= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                running = False
        
        for i, j in zip(traînées_finales_pos_left, traînées_finales_size_left) :
            if player_pos_2[1] <= i[1] + 5 and player_pos_2[1] >= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                running = False
        
        for i, j in zip(traînées_finales_pos_right, traînées_finales_size_right) :
            if player_pos_2[1] <= i[1] + 5 and player_pos_2[1] >= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                running = False

    #-----------------------------------------------------------------------------DOWN--------------------------------------------------------------------------
    
    if executing_lightcycle_movement_down :
        for i, j in zip(traînées_finales_pos_q, traînées_finales_size_q) :
            if player_pos_2[1] + 25 >= i[1] and player_pos_2[1] + 20 <= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                running = False
        
        for i, j in zip(traînées_finales_pos_d, traînées_finales_size_d) :
            if player_pos_2[1] + 25 >= i[1] and player_pos_2[1] + 20 <= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                running = False
        
        for i, j in zip(traînées_finales_pos_left, traînées_finales_size_left) :
            if player_pos_2[1] + 25 >= i[1] and player_pos_2[1] + 20 <= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                running = False
        
        for i, j in zip(traînées_finales_pos_right, traînées_finales_size_right) :
            if player_pos_2[1] + 25 >= i[1] and player_pos_2[1] + 20 <= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
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

    #-----------------------------------------------------------------------------------------------------------------------------------------------------------
    #------------------------------------------------------------------------STATISTIQUES-----------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------

    secondes += 1/60
    
    if secondes == 60 :
        secondes = 0
        minutes += 1
        score_player += 100
        score_player_2 += 100
    
    if minutes == 60 :
        minutes = 0
        heures += 1
        score_player += 10000
        score_player_2 += 10000

    #--------------------------------------------------------------------------AFFICHAGE------------------------------------------------------------------------

    Temps = f"{heures} : {minutes} : {round(secondes)}"
    font_Temps = pygame.font.Font(digital_7, 30)
    Temps_img = font_Temps.render(Temps, True, (255, 255, 255))
    Temps_dimensions = Temps_img.get_size()
    Temps_pos = [screen_size[0] / 2 - Temps_dimensions[0] / 2, grid_pos[1] / 2 - Temps_dimensions[1] / 2]

    screen.blit(Temps_img, Temps_pos)

    titre_Temps = "TEMPS"
    font_titre_Temps = pygame.font.Font(Score_Board_St, 15)
    titre_Temps_img = font_titre_Temps.render(titre_Temps, True, (255, 255, 255))
    titre_Temps_dimensions = titre_Temps_img.get_size()
    titre_Temps_pos = [screen_size[0] / 2 - titre_Temps_dimensions[0] / 2, Temps_pos[1] + Temps_dimensions[1]]

    screen.blit(titre_Temps_img, titre_Temps_pos)


    Score_player = f"{score_player}"
    font_Score_player = pygame.font.Font(Technos, 20)
    Score_player_img = font_Score_player.render(Score_player, True, (207, 47, 17))
    Score_player_dimensions = Score_player_img.get_size()
    Score_player_pos = [screen_size[0] / 2 - Score_player_dimensions[0] / 2 - 100, grid_pos[1] / 2 - Score_player_dimensions[1] / 2]

    screen.blit(Score_player_img, Score_player_pos)

    titre_Score_player = "SCORE J1"
    font_titre_Score_player = pygame.font.Font(Score_Board_St, 15)
    titre_Score_player_img = font_titre_Score_player.render(titre_Score_player, True, (207, 47, 17))
    titre_Score_player_dimensions = titre_Score_player_img.get_size()
    titre_Score_player_pos = [screen_size[0] / 2 - titre_Score_player_dimensions[0] / 2 - 100, Score_player_pos[1] / 2 - 5]

    screen.blit(titre_Score_player_img, titre_Score_player_pos)    

    Score_player_2 = f"{score_player_2}"
    font_Score_player_2 = pygame.font.Font(Technos, 20)
    Score_player_2_img = font_Score_player_2.render(Score_player_2, True, (0, 0, 255))
    Score_player_2_dimensions = Score_player_2_img.get_size()
    Score_player_2_pos = [screen_size[0] / 2 - Score_player_2_dimensions[0] / 2 + 100, grid_pos[1] / 2 - Score_player_2_dimensions[1] / 2]

    screen.blit(Score_player_2_img, Score_player_2_pos)

    titre_Score_player_2 = "SCORE J2"
    font_titre_Score_player_2 = pygame.font.Font(Score_Board_St, 15)
    titre_Score_player_2_img = font_titre_Score_player_2.render(titre_Score_player_2, True, (0, 0, 255))
    titre_Score_player_2_dimensions = titre_Score_player_2_img.get_size()
    titre_Score_player_2_pos = [screen_size[0] / 2 - titre_Score_player_2_dimensions[0] / 2 + 100, Score_player_2_pos[1] / 2 - 5]

    screen.blit(titre_Score_player_2_img, titre_Score_player_2_pos)

    
    score_player, collectibles_player, collectibles_pos = réapparition_collectibles(executing_lightcycle_movement_q, executing_lightcycle_movement_d , executing_lightcycle_movement_z, executing_lightcycle_movement_s, grid_pos, grid_size, player_pos, player_size, collectibles_pos, collectibles_size, collectibles_player, score_player)
    score_player_2, collectibles_player_2, collectibles_pos = réapparition_collectibles(executing_lightcycle_movement_left, executing_lightcycle_movement_right, executing_lightcycle_movement_up, executing_lightcycle_movement_down, grid_pos, grid_size, player_pos_2, player_size_2, collectibles_pos, collectibles_size, collectibles_player_2, score_player_2)

    screen.blit(collectibles, collectibles_pos)

    #------------------------------------------------------------------CALCULS DE FIN DE PARTIE-----------------------------------------------------------------

    temps_total = heures * 3600 + minutes * 60 + secondes

    frôlements_player += frôlements_de_la_mort_qui_tue_player
    frôlements_player_2 += frôlements_de_la_mort_qui_tue_player_2

    succès_temps_1_player, succès_temps_1_player_2, succès_temps_2_player, succès_temps_2_player_2, succès_temps_3_player, succès_temps_3_player_2, succès_temps_caché_player, succès_temps_caché_player_2 = succès_temps(temps_total, succès_temps_1_player, succès_temps_1_player_2, succès_temps_2_player, succès_temps_2_player_2, succès_temps_3_player, succès_temps_3_player_2, succès_temps_caché_player, succès_temps_caché_player_2)

    succès_score_1_player, succès_score_2_player, succès_score_3_player, succès_score_caché_player = succès_score(score_player, succès_score_1_player, succès_score_2_player, succès_score_3_player, succès_score_caché_player)
    succès_score_1_player_2, succès_score_2_player_2, succès_score_3_player_2, succès_score_caché_player_2 = succès_score(score_player_2, succès_score_1_player_2, succès_score_2_player_2, succès_score_3_player_2, succès_score_caché_player_2)

    succès_frôlements_1_player, succès_frôlements_2_player, succès_frôlements_3_player, succès_frôlements_caché_player = succès_frôlements(frôlements_player, succès_frôlements_1_player, succès_frôlements_2_player, succès_frôlements_3_player, succès_frôlements_caché_player)
    succès_frôlements_1_player_2, succès_frôlements_2_player_2, succès_frôlements_3_player_2, succès_frôlements_caché_player_2 = succès_frôlements(frôlements_player_2, succès_frôlements_1_player_2, succès_frôlements_2_player_2, succès_frôlements_3_player_2, succès_frôlements_caché_player_2)

    succès_collectibles_1_player, succès_collectibles_2_player, succès_collectibles_3_player, succès_collectibles_caché_player = succès_collectibles(collectibles_player, succès_collectibles_1_player, succès_collectibles_2_player, succès_collectibles_3_player, succès_collectibles_caché_player)
    succès_collectibles_1_player_2, succès_collectibles_2_player_2, succès_collectibles_3_player_2, succès_collectibles_caché_player_2 = succès_collectibles(collectibles_player_2, succès_collectibles_1_player_2, succès_collectibles_2_player_2, succès_collectibles_3_player_2, succès_collectibles_caché_player_2)


    pygame.display.flip()
    clock.tick(60)

pygame.quit