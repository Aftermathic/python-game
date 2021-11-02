import pygame
from player import Player
from bacon import Bacon
from pygame import *

pygame.init()

clock = time.Clock()

window_w = 1280
window_h = 720
window_r = (1280, 720)
window = display.set_mode(window_r)
display.set_caption('The Last Bacon')

red = (255, 0, 0)
white = (255, 255, 255)
gray = (32, 32, 32)
brown = (160, 82, 45)
black = (0, 0, 0)

font = pygame.font.Font('data/fonts/game_font.ttf', 20)
game_over_txt = font.render('GAME OVER. Reopen the game to try again!', True, white)
you_win_txt = font.render('YOU WIN! Reopen the game to try again!', True, white)

#objects
hole_img = image.load('data/images/hole.png')
hole_surf = Surface.convert_alpha(hole_img)
hole = transform.scale(hole_surf, (348, 311))

goal_img = image.load('data/images/goal.png')
goal_surf = Surface.convert_alpha(goal_img)
goal = transform.scale(goal_surf, (1280, 64))


player_surf = Surface.convert_alpha(Player.player_img)
player = transform.scale(player_surf, (64, 64))

bacon_surf = Surface.convert_alpha(Bacon.bacon_img)
bacon = transform.scale(bacon_surf, (136, 60))

#game loop
running = True
game = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            mouse_pos = mouse.get_pos()
            mousex = mouse_pos[0]
            mousey = mouse_pos[1]

            Bacon.bacon_x = mousex
            Bacon.bacon_y = mousey

    window.fill(gray)

    clock.tick(120)

    #movement
    Player.player_y += Player.gravity

    if Player.player_x < Bacon.bacon_x:
        Player.player_x += Player.speed
    elif Player.player_x > Bacon.bacon_x:
        Player.player_x -= Player.speed
    elif Player.player_y + Player.jump_pow > Bacon.bacon_y:
        Player.player_y -= Player.jump_pow

    #functions
    if Player.player_y > window_h:
        window.blit(game_over_txt, (window_w // 2, window_h // 2))
        Player.player_y = 9999
        Player.player_x = 9999
    elif Player.player_y < 64:
        window.blit(you_win_txt, (window_w // 2, window_h // 2))
        Player.player_y = 64
        Bacon.bacon_x = Player.player_x

    window.blit(player, (Player.player_x, Player.player_y))
    window.blit(bacon, (Bacon.bacon_x, Bacon.bacon_y))
    window.blit(hole, (Player.player_x - 130, 500))
    window.blit(goal, (0,  64))

    display.update()

pygame.quit()