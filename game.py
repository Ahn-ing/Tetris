import pygame
import sys
from board import col, row, score_field, size, Board
from Tetro import Tetromino
from Tetromino_list import *

pygame.init()

Main_window = pygame.display.set_mode(((col + score_field) * size, row * size))
Game_Board = Board()
Tetro_L = Tetromino(L)

while True:
    cur_Tetro = Tetro_L

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
                    cur_Tetro.move(1)

    Main_window.fill("#dfdede")
    Game_Board.drawGrid(Main_window)
    Tetro_L.draw(Main_window, "orange")

    pygame.display.update()
