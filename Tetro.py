import pygame
from board import size, row, col, Board
import random as ran

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

    def putIntoBoard(self):
        for y in range(len(self.tetromino[self.status])):
            for x in range(len(self.tetromino[self.status][y])):
                if self.tetromino[self.status][y][x] == '1':
                    Game_Board.board[y+self.height][x+self.position] = 1

    def draw(self, surface, color):
        should_lock = False
        self.collide_left = False
        self.collide_right =False
        
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
                    if global_y == row - 1:
                        should_lock = True
                    elif  global_y < row-1 and Game_Board.board[global_y + 1][global_x] == 1:
                        should_lock = True
                    if global_x -1 >= 0 and Game_Board.board[global_y][global_x-1] == 1:
                        self.collide_left = True
                    if global_x + 1 < col and Game_Board.board[global_y][global_x+1] == 1:
                        self.collide_right =True
                    
            if should_lock:
                self.hit_bottom = True
                self.putIntoBoard()

                return
                                
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.height += 1

    def move(self, offset):
        self.position += offset

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

    def reset(self):
        self.hit_bottom = False
        self.height = 0
        self.position = 4
        self.status = ran.randint(0, 3)


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
   

        
