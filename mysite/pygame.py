#! python -m pip instal pygame

import pygame
from random import *

pygame.init()

clock = pygame.time.Clock()
sc = pygame.display.set_mode((500,375))
pic = ['bg', 'logo', 'm1', 'm2', 'm3', 'm4', 'm5', 'ps1', 'ps2',]
Surf = {}
for i in pic:
    Surf[i] = pygame.image.load(f'{i}.png')
menu = True
while menu:
    clock.tick(60)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            menu = False
    sc.blit(Surf['bg'],(0,0))
    sc.blit(Surf['logo'],(0,0))
    for i in range(5):
        sc.blit(Surf[f'm{str(i+1)}'], (180, 50+45*i))
    if iter < 100:
        pl = Surf['ps2']
    elif iter < 200:
        pl = Surf['ps1']
    else: iter = 0
    sc.blit(pl,  (40, 190))
    pygame.display.update()
