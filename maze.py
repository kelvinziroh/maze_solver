import time
import random
from cell import Cell

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.__cells = []

        self.__create_cells()
        self.__break_entrance_and_exit()
        
        if seed is not None:
            random.seed(seed)
        
        self.__break_walls_r(0, 0)
    
    def __create_cells(self):
        for i in range(self.num_cols):
            cell_col = []
            for j in range(self.num_rows):
                cell_col.append(Cell(self.win))
            self.__cells.append(cell_col)
        
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.__draw_cell(i, j)
        
    
    def __draw_cell(self, i, j):
        if self.win is None:
            return
        x1 = self.x1 + (i * self.cell_size_x)
        y1 = self.y1 + (j * self.cell_size_y)
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        self.__cells[i][j].draw(x1, y1, x2, y2)
        self.__animate()
    
    def __animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.05)
    
    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        
        self.__cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
        self.__draw_cell(self.num_cols - 1, self.num_rows - 1)
    
    def __break_walls_r(self, i, j):
        self.__cells[i][j].visited = True
        while True:
            possible_directions = []
            
            if i > 0 and not self.__cells[i - 1][j].visited:
                possible_directions.append((i - 1, j))
            if i < self.num_cols - 1 and not self.__cells[i + 1][j].visited:
                possible_directions.append((i + 1, j))
            if j > 0 and not self.__cells[i][j - 1].visited:
                possible_directions.append((i, j - 1))
            if j < self.num_rows - 1 and not self.__cells[i][j + 1].visited:
                possible_directions.append((i, j + 1))
            
            if len(possible_directions) == 0:
                self.__draw_cell(i, j)
                return

            direction = random.choice(possible_directions)

            # knock down the walls between the current cell and the chosen cell
            if direction[1] < j:
                self.__cells[i][j].has_top_wall = False
                self.__cells[i][j - 1].has_bottom_wall = False
            
            if direction[0] > i:
                self.__cells[i][j].has_right_wall = False
                self.__cells[i + 1][j].has_left_wall = False
    
            if direction[1] > j:
                self.__cells[i][j].has_bottom_wall = False
                self.__cells[i][j + 1].has_top_wall = False
    
            if direction[0] < i:
                self.__cells[i][j].has_left_wall = False
                self.__cells[i - 1][j].has_right_wall = False
            
            i = direction[0]
            j = direction[1]
            
            self.__break_walls_r(i, j)         
