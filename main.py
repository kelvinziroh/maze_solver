from graphics import *
from cell import Cell

def main():
    win = Window(800, 600)
    
    cell = Cell(win)
    cell.draw(12, 12, 52, 52)
    
    win.wait_for_close()


if __name__ == "__main__":
    main()
