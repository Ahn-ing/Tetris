import pygame
import sys
from board import col, row, score_field, size, Board
from Tetro import Tetromino, NewTetromino
from Tetromino_list import *
import random

FPS = 60

pygame.init()

Main_window = pygame.display.set_mode(((col + score_field) * size, row * size))
Game_Board = Board()
Tetro_list = [
    "L",
    "LL",
    "I",
    "Z",
    "ZZ",
    "W",
    "H",
]
Tetroes = {
    "L": L,
    "LL": LL,
    "I": I,
    "Z": Z,
    "ZZ": ZZ,
    "W": W,
    "H": H,
}

color_dict = {
    "L":    "#d19f32f9",
    "LL":   "#57b857",
    "I":    "#a82a2a",
    "Z":    "#578cb8",
    "ZZ":   "#ad57b8",
    "W":    "#b8578c",
    "H":    "#57b2b8",
}

clock = pygame.time.Clock()
cur_T = random.choice(Tetro_list)
next_T = random.choice(Tetro_list)

cur_Tetro = Tetromino(Tetroes[cur_T])
next_Tetro = NewTetromino(Tetroes[next_T])
while True:

    if cur_Tetro.hit_bottom:
        cur_Tetro.reset()
        # 创建新的当前方块，从顶部开始
        cur_T = next_T
        cur_Tetro = Tetromino(Tetroes[cur_T])
        # 生成新的下一个方块，仅用于右侧显示
        next_T = random.choice(Tetro_list)
        next_Tetro = NewTetromino(Tetroes[next_T])

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if cur_Tetro.getLeftIndex() + cur_Tetro.position > 0:
                    cur_Tetro.move(-1)
            if event.key == pygame.K_RIGHT:
                if cur_Tetro.getRightIndex() + cur_Tetro.position < col - 1:
                    cur_Tetro.move(1)
            if event.key == pygame.K_UP:
                cur_Tetro.rotate()
                while cur_Tetro.getLeftIndex() + cur_Tetro.position < 0:
                    cur_Tetro.move(1)
                while cur_Tetro.getRightIndex() + cur_Tetro.position > col - 1:
                    cur_Tetro.move(-1)

    Main_window.fill("#000000")
    Game_Board.drawGrid(Main_window)
    next_Tetro.draw(Main_window, color_dict[next_T])
    cur_Tetro.draw(Main_window, color_dict[cur_T])

    pygame.display.update()
