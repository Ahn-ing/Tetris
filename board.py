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
        super(Board, self).__init__()
        self.board = np.zeros((row, col))

    def drawGrid(self, surface):
        for i in range(row):
            for j in range(col):
                if self.board[i][j] == 0:
                    pygame.draw.rect(
                        surface, "#3f3f3f", (j * size, i * size, size - 1, size - 1)  # 以左上角为原点，第三个参数rec(x,y,x_range,y_range),x是横坐标
                    )

