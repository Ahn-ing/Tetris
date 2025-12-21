import pygame
from board import size, row, col, Board
import random as ran

pygame.init()
pygame.font.init()
Game_Board = Board()


class Tetromino:
    """docstring for Tetromino."""

    def __init__(self, character, status=0):
        super().__init__()
        self.tetromino = character
        self.position = 4
        self.status = status
        self.height = 0
        self.hit_bottom = False
        self.collide_left = False
        self.collide_right = False
        self.drop_timer = 0
        self.drop_speed = 500
        self.lock_timer = 0
        self.lock_delay = 500  # ms

    def putIntoBoard(self):
        for y in range(len(self.tetromino[self.status])):
            for x in range(len(self.tetromino[self.status][y])):
                if self.tetromino[self.status][y][x] == '1':
                    global_x = x + self.position
                    global_y = y + self.height

                    if global_x >= 0 and global_x < col and global_y >= 0 and global_y < row:
                        Game_Board.board[global_y][global_x] = 1

    def draw(self, surface, color, dt):
        # 每次while时都会调用draw
        self.collide_left = False
        self.collide_right =False
        grounded = self.is_collide(Game_Board,offset_y=1)

        if grounded:
            self.lock_timer += dt
            if self.lock_timer >= self.lock_delay:
                self.hit_bottom = True
        else:
            self.lock_timer = 0

        self.drop_timer += dt
        if self.drop_timer >= self.drop_speed:
            if not grounded:
                self.height += 1
            self.drop_timer = 0
        
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            if not grounded:
                self.height += 1
            else:
                self.lock_timer += 250  # 快速下落时增加锁定时间

        for i in range(len(self.tetromino[self.status])):
            for j in range(len(self.tetromino[self.status][i])):
                if self.tetromino[self.status][i][j] == "1":
                    global_x = j + self.position
                    global_y = i + self.height
                    pygame.draw.rect(
                        surface,
                        color,
                        (
                            global_x * size,
                            global_y * size,
                            size - 1,
                            size - 1,
                        ),
                    )
                    if global_x -1 >= 0 and Game_Board.board[global_y][global_x-1] == 1:
                        self.collide_left = True
                    if global_x + 1 < col and Game_Board.board[global_y][global_x+1] == 1:
                        self.collide_right =True
                    
                
                                

    def move(self, offset):
        self.position += offset

        return False
    
    def is_collide(self, board_obj, offset_x=0, offset_y=0, check_status=None):
        """
        检测碰撞的辅助函数
        offset_x, offset_y: 用于测试由于踢墙移动后的位置
        check_status: 用于测试旋转后的状态
        """
        status_to_check = self.status if check_status is None else check_status
        
        for y in range(len(self.tetromino[status_to_check])):
            for x in range(len(self.tetromino[status_to_check][y])):
                if self.tetromino[status_to_check][y][x] == '1':
                    # 计算在整个棋盘上的绝对坐标
                    global_x = x + self.position + offset_x
                    global_y = y + self.height + offset_y

                    # 1. 检查 底部
                    if global_y >= row:
                        return True
                    
                    # 2. 检查是否与已有的方块重叠 (Game_Board)
                    # 注意：只检查 global_y >= 0 的情况，防止还没进场就报错
                    if global_y >= 0 and board_obj.board[global_y][global_x] == 1:
                        return True
        return False

    def getLeftIndex(self):  # 返回的是方块内部的形状索引，并不是全局的位置
        left_index = float("inf")
        for i in range(len(self.tetromino[self.status])):
            for j in range(len(self.tetromino[self.status][i])):
                if self.tetromino[self.status][i][j] == "1":
                    left_index = min(left_index, j)
        return left_index

    def getRightIndex(self):
        right_index = float("-inf")
        for i in range(len(self.tetromino[self.status])):
            for j in range(len(self.tetromino[self.status][i])):
                if self.tetromino[self.status][i][j] == "1":
                    right_index = max(right_index, j)
        return right_index
    
    def rotate(self):
        self.status = (self.status + 1) % 4
    
    def check_game_over(self):
        for i in range(len(self.tetromino[self.status])):
            for j in range(len(self.tetromino[self.status][i])):
                if self.tetromino[self.status][i][j] == "1":
                    global_x = j + 4
                    global_y = i

                    if 0<= global_x < col and 0<= global_y < row:  # 检测是否越界
                        if Game_Board.board[global_y][global_x] == 1:
                            return True
        
        return False

    def reset(self):
        self.hit_bottom = False
        self.height = 0
        self.position = 4
        self.status = ran.randint(0, 3)
        self.drop_timer = 0
        self.lock_timer = 0


class NewTetromino(Tetromino):
    """docstring for NewTetromino."""

    def __init__(self, character, status=0):
        super().__init__(character, status=0)
        self.height = 4
        self.position = col + 2  # 列数

    def draw(self, surface, color):
        for i in range(len(self.tetromino[self.status])):
            for j in range(len(self.tetromino[self.status][i])):
                if self.tetromino[self.status][i][j] == "1":
                    pygame.draw.rect(
                        surface,
                        color,
                        (
                            (j + self.position) * size,
                            (i + self.height) * size,
                            size - 1,
                            size - 1,
                        ),
                    )
   
   


        
