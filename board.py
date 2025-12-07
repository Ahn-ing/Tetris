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

        # --- 新增：初始化字体 ---
        # 使用系统字体 'Arial' (或 'SimHei' 支持中文)，字号 30，加粗 True
        self.title_font = pygame.font.SysFont('SimHei', 30, True)
        self.score_font = pygame.font.SysFont('Arial', 40, True)

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
                self.score += 10
                self.board[i:i+1] = [0]*col
                shifted = np.zeros_like(self.board[:i+1])
                shifted[1:] = self.board[:i]
                self.board[:i+1] = shifted
                

    def drawScore(self,surface):
        

        # 分数标题 
        text_tittle = self.title_font.render("分 数",True,"#5537c0")
        
        start_x = (col+score_field//2-1)*size
        start_y = (row*size)*0.6

        surface.blit(text_tittle,(start_x,start_y))
        # 分数显示
        text_score = self.score_font.render(str(self.score),True,"#317e4b")

        surface.blit(text_score,(start_x+size//2,start_y+2*size))

        
              
    def updateBoard(self,surface):
        self.eliminate()
        self.drawScore(surface)
        self.drawGrid(surface)

    


    
