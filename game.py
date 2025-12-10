import pygame
import sys
from board import col, row, score_field, size
from Tetro import Tetromino, NewTetromino,Game_Board
from Tetromino_list import *
import random

FPS = 30



Main_window = pygame.display.set_mode(((col + score_field) * size, row * size))



clock = pygame.time.Clock()
cur_T = random.choice(Tetro_list)
next_T = random.choice(Tetro_list)

cur_Tetro = Tetromino(Tetroes[cur_T])
next_Tetro = NewTetromino(Tetroes[next_T])


while True:
    drop_timer += clock.tick(FPS)
    if drop_timer > drop_interval:
        cur_Tetro.height += 1
        
        drop_timer = 0

    cur_Tetro.drop_timer += clock.tick(FPS)

    if cur_Tetro.hit_bottom:
        cur_Tetro.putIntoBoard()
        cur_Tetro.reset()
        # 创建新的当前方块，从顶部开始
        cur_T = next_T
        cur_Tetro = Tetromino(Tetroes[cur_T])
        # 生成新的下一个方块，仅用于右侧显示
        next_T = random.choice(Tetro_list)
        next_Tetro = NewTetromino(Tetroes[next_T])

        cur_Tetro.drop_timer = 0

    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT :
                if cur_Tetro.getLeftIndex() + cur_Tetro.position > 0 and not cur_Tetro.collide_left:
                    cur_Tetro.move(-1)
            if event.key == pygame.K_RIGHT :
                if cur_Tetro.getRightIndex() + cur_Tetro.position < col - 1 and not cur_Tetro.collide_right:
                    cur_Tetro.move(1)
            if event.key == pygame.K_UP :
                old_status = cur_Tetro.status
                cur_Tetro.rotate()

                if cur_Tetro.is_collide(Game_Board):
                # === 踢墙逻辑 (Wall Kick) ===
                # 尝试向右挪一格是否能容纳？
                    if not cur_Tetro.is_collide(Game_Board, offset_x=1):
                        cur_Tetro.move(1)
                    # 尝试向左挪一格是否能容纳？
                    elif not cur_Tetro.is_collide(Game_Board, offset_x=-1):
                        cur_Tetro.move(-1)
                    # 尝试向右挪两格 (主要针对长条I)
                    elif not cur_Tetro.is_collide(Game_Board, offset_x=2):
                        cur_Tetro.move(2)
                    # 尝试向左挪两格
                    elif not cur_Tetro.is_collide(Game_Board, offset_x=-2):
                        cur_Tetro.move(-2)
                    # === 如果左右挪动都无法解决冲突 ===
                    else:
                        cur_Tetro.status = old_status  # 4. 退回旋转前的状态 (撤销旋转)
                while cur_Tetro.getLeftIndex() + cur_Tetro.position < 0 :
                    cur_Tetro.move(1)
                while cur_Tetro.getRightIndex() + cur_Tetro.position > col - 1:
                    cur_Tetro.move(-1)

    Main_window.fill("#000000")

    Game_Board.drawGrid(Main_window)
    Game_Board.updateBoard(Main_window)
    next_Tetro.draw(Main_window, color_dict[next_T])
    cur_Tetro.draw(Main_window, color_dict[cur_T])
    

    pygame.display.update()
