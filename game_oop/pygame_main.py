from random import randint

import pygame
from pygame.locals import *

from game_oop.game import Game


def change_color(image, color):
    coloured_image = pygame.Surface(image.get_size())
    coloured_image.fill(color)

    final_image = image.copy()
    final_image.blit(coloured_image, (0, 0), special_flags=pygame.BLEND_MULT)
    return final_image


def draw_characters():
    for pos_y in range(1, 11):
        for pos_x in range(1, 11):
            if not game.all_team.check_position(pos_x, pos_y):
                hero = game.all_team.get_hero_by_pos(pos_x, pos_y)
                x = pos_x * size[0] / 12
                y = pos_y * size[1] / 12
                if hero.class_name == "Арбалетчик":
                    sprite = crossbowman
                elif hero.class_name == "Волшебник":
                    sprite = mage
                elif hero.class_name == "Монах":
                    sprite = monk
                elif hero.class_name == "Фермер":
                    sprite = peasant
                elif hero.class_name == "Разбойник":
                    sprite = rogue
                elif hero.class_name == "Лучник":
                    sprite = sniper
                elif hero.class_name == "Копейщик":
                    sprite = spearman
                if hero.state == "Dead":
                    sprite = change_color(sprite, 'Red')
                elif hero.state == "Hide":
                    sprite = change_color(sprite, 'Grey')
                if hero.team_side:
                    screen.blit(sprite, (x, y))
                else:
                    screen.blit(pygame.transform.flip(sprite, True, False), (x, y))


bgs = ['bg1', 'bg2', 'bg3', 'bg4', 'bg5']
musics = ['m1', 'm2', 'm3', 'm4']

pygame.init()

game = Game()
game.create_teams()
size = (800, 556)
screen = pygame.display.set_mode(size, HWSURFACE | DOUBLEBUF | RESIZABLE)
bg = pygame.image.load(f'assets/фоны/{bgs[randint(0, len(bgs) - 1)]}.png')
screen.blit(pygame.transform.scale(bg, size), (0, 0))
pygame.display.flip()
pygame.display.set_caption('Игра началась')
icon = pygame.image.load('assets/icon.png')
pygame.display.set_icon(icon)

music = pygame.mixer.Sound(f'assets/Музыка/{musics[randint(0, len(musics) - 1)]}.mp3')
music.set_volume(0.06)
music.play()

crossbowman = pygame.image.load(f'assets/персонажи/CrossBowMan.png')
mage = pygame.image.load(f'assets/персонажи/Mage.png')
monk = pygame.image.load(f'assets/персонажи/Monk.png')
peasant = pygame.image.load(f'assets/персонажи/Peasant.png')
rogue = pygame.image.load(f'assets/персонажи/Rogue.png')
sniper = pygame.image.load(f'assets/персонажи/Sniper.png')
spearman = pygame.image.load(f'assets/персонажи/SpearMan.png')

sprite = ""

turn_count = 0

draw_characters()

pygame.display.update()

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == VIDEORESIZE:
            size = event.dict['size']
            screen = pygame.display.set_mode(size, HWSURFACE | DOUBLEBUF | RESIZABLE)
            screen.blit(pygame.transform.scale(bg, size), (0, 0))
            draw_characters()
            pygame.display.flip()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if game.game_ended():
                if game.dark_team:
                    bg = pygame.image.load(f'assets/фоны/GameEnd2.png')
                else:
                    bg = pygame.image.load(f'assets/фоны/GameEnd1.png')
                pygame.display.set_caption('Игра закончилась')
                screen.blit(pygame.transform.scale(bg, size), (0, 0))
            else:
                game.teams_make_turns()
                turn_count += 1
                pygame.display.set_caption(f'Ход номер {turn_count}')
                screen.blit(pygame.transform.scale(bg, size), (0, 0))
                draw_characters()
            pygame.display.update()
