import pygame
from board import size


class Tetromino:
    """docstring for Tetromino."""

    def __init__(self, character, status=0):
        super().__init__()
        self.tetromino = character
        self.position = 3

    def draw(self, surface, color):
        for i in range(len(self.tetromino)):
            for j in range(len(self.tetromino[i])):
                if self.tetromino[i][j] == "1":
                    pygame.draw.rect(
                        surface,
                        color,
                        ((j + self.position) * size, i * size, size - 1, size - 1),
                    )

    def move(self, offset):
        self.position += offset

    def getLeftIndex(self):  # 返回的是方块内部的形状索引，并不是全局的位置
        left_index = float("inf")
        for i in range(len(self.tetromino)):
            for j in range(len(self.tetromino[i])):
                if self.tetromino[i][j] == "1":
                    left_index = min(left_index, j)
        return left_index

    def getRightIndex(self):
        right_index = float("-inf")
        for i in range(len(self.tetromino)):
            for j in range(len(self.tetromino[i])):
                if self.tetromino[i][j] == "1":
                    right_index = max(right_index, j)
        return right_index

    def rotate(self):
        temp_list = [
            [int(self.tetromino[i][j]) for j in range(len(self.tetromino[i]))]
            for i in range(len(self.tetromino))
        ]
        n = len(temp_list)
        temp_list[:] = [
            [temp_list[j][n - 1 - i] for j in range(len(temp_list[i]))]
            for i in range(n)
        ]

        self.tetromino = ["".join(map(str,temp_list[i])) for i in range(n)]
