from graphics import Point, Line

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = win
    
    def draw(self, x1, y1, x2, y2):
        if self.__win is None:
            return
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        
        left_line = Line(Point(x1, y1), Point(x1, y2))
        top_line = Line(Point(x1, y1), Point(x2, y1))
        right_line = Line(Point(x2, y1), Point(x2, y2))
        bottom_line = Line(Point(x1, y2), Point(x2, y2))
        
        if self.has_left_wall:
            self.__win.draw_line(left_line)
        else:
            self.__win.draw_line(left_line, "white")

        if self.has_top_wall:
            self.__win.draw_line(top_line)
        else:
            self.__win.draw_line(top_line, "white")

        if self.has_right_wall:
            self.__win.draw_line(right_line)
        else:
            self.__win.draw_line(right_line, "white")

        if self.has_bottom_wall:
            self.__win.draw_line(bottom_line)
        else:
            self.__win.draw_line(bottom_line, "white")

    def draw_move(self, to_cell, undo=False):
        
        half_start = abs(self.__x2 - self.__x1) // 2
        half_dest = abs(to_cell.__x2 - to_cell.__x1) // 2
        
        mid_x = half_start + self.__x1
        mid_y = half_start + self.__y1
        
        dest_mid_x = half_dest + to_cell.__x1
        dest_mid_y = half_dest + to_cell.__y1

        a = Point(mid_x, mid_y)
        b = Point(dest_mid_x, dest_mid_y)
        
        move_color = "red"
        if undo:
            move_color = "gray"
            
        line = Line(a, b)
        
        self.__win.draw_line(line, move_color)
            