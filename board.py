import pygame
import numpy as np

col = 10  # 列数
row = 25  # 行数
size = 45  # 格子大小
score_field = 6  # 得分窗口列数


class Board:
    """docstring for Board."""

    def __init__(
        self,
    ):
        super().__init__()
        self.board = np.zeros((row, col))
        self.score = 0

    def drawGrid(self, surface):
        for i in range(row):
            for j in range(col):
                if self.board[i][j] == 0:
                    pygame.draw.rect(
                        surface,
                        "#3f3f3f",
                        (
                            j * size,
                            i * size,
                            size - 1,
                            size - 1,
                        ),  # 以左上角为原点，第三个参数rec(x,y,x_range,y_range),x是横坐标
                    )
                elif self.board[i][j] == 1:
                    pygame.draw.rect(
                        surface,
                        "#8B8B8B",
                        (
                            j * size,
                            i * size,
                            size - 1,
                            size - 1,
                        ),  # 以左上角为原点，第三个参数rec(x,y,x_range,y_range),x是横坐标
                    )

    def eliminate(self):
        for i in range(row):
            count = 0
            for j in range(col):
                if self.board[i][j] :
                    count+=1
            if count == col:
                self.score += 1
                self.board[i:i+1] = [0]*col
                shifted = np.zeros_like(self.board[:i+1])
                shifted[1:] = self.board[:i]
                self.board[:i+1] = shifted
                
                  
    def updateBoard(self,surface):
        self.eliminate()
        self.drawGrid(surface)

    
