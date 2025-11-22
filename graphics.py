from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze Solver")
        self.canvas = Canvas(self.root, bg="white", height=height, width=width)
        self.canvas.pack()
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)
    
    def draw_line(self, line, fill_color="black"):
        line.draw(self.canvas, fill_color)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        print("Session ended...")
    
    def close(self):
        self.running = False


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def draw(self, canvas, fill_color):
        x1, y1 = self.a.x, self.a.y
        x2, y2 = self.b.x, self.b.y
        canvas.create_line(
            x1, y1, x2, y2, fill=fill_color, width=2
        )        
        