import pygame
from pygame import *

class Player():
    speed = 1
    gravity = 1
    player_x = 540
    player_y = 300
    jump_pow = 5

    player_img = image.load('data/images/player.png')