from graphics import *

def main():
    win = Window(800, 600)
        
    a = Point(100, 50)
    b = Point(400, 50)
    line = Line(a, b)
    win.draw_line(line, "black")
    
    win.wait_for_close()


if __name__ == "__main__":
    main()
