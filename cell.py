from graphics import Point, Line

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
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
        
        if self.has_left_wall:
            a = Point(x1, y1)
            b = Point(x1, y2) 
            line = Line(a, b)
            self.__win.draw_line(line)

        if self.has_top_wall:
            a = Point(x1, y1)
            b = Point(x2, y1)
            line = Line(a, b)
            self.__win.draw_line(line)

        if self.has_right_wall:
            a = Point(x2, y1)
            b = Point(x2, y2)
            line = Line(a, b)
            self.__win.draw_line(line)

        if self.has_bottom_wall:
            a = Point(x1, y2)
            b = Point(x2, y2)
            line = Line(a, b)
            self.__win.draw_line(line)

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
            