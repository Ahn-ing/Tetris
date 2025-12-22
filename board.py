import pygame
import numpy as np

col = 10  # 列数
row = 25  # 行数
size = 25  # 格子大小
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
        self.game_over_font = pygame.font.SysFont('SimHei', 40, True)
        self.game_pause_font = pygame.font.SysFont('SimHei', 40, True)

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
        lines_cleared = 0
        for i in range(row-1, -1, -1):  # 从底部向上检查
            if np.all(self.board[i] == 1):
                lines_cleared += 1
                # 上方行整体下移
                self.board[1:i+1] = self.board[0:i]
                # 清空最顶行
                self.board[0] = np.zeros(col)
        
        self.score += lines_cleared * 10
        return lines_cleared
                

    def drawScore(self,surface):
        

        # 分数标题 
        text_tittle = self.title_font.render("分 数",True,"#5537c0")
        
        start_x = (col+score_field//2-1)*size
        start_y = (row*size)*0.6

        surface.blit(text_tittle,(start_x,start_y))
        # 分数显示
        text_score = self.score_font.render(str(self.score),True,"#317e4b")

        surface.blit(text_score,(start_x+size//2,start_y+2*size))

    def drawGameOver(self,surface):
        text_game_over = self.game_over_font.render("游戏结束",True,"#c03e3e") # 第四个参数是背景色
        text_game_over_rect = text_game_over.get_rect(center=(surface.get_width()//2, surface.get_height()//2))
        surface.blit(text_game_over, text_game_over_rect)

    def drawGamePause(self,surface):
        text_game_pause = self.game_pause_font.render("游戏暂停",True,"#c0a33e")
        text_game_pause_rect = text_game_pause.get_rect(center=(surface.get_width()//2, surface.get_height()//2))
        surface.blit(text_game_pause, text_game_pause_rect)

              
    def updateBoard(self,surface):
        self.eliminate()
        self.drawScore(surface)
        self.drawGrid(surface)

    
    


    
