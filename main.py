from graphics import *
from cell import Cell

def main():
    win = Window(800, 600)
    
    cell_1 = Cell(win)
    cell_1.draw(50, 50, 100, 100)
    
    cell_2 = Cell(win)
    cell_2.draw(100, 50, 150, 100)
    
    cell_3 = Cell(win)
    cell_3.draw(100, 100, 150, 150)
    
    cell_4 = Cell(win)
    cell_4.draw(50, 100, 100, 150)
    
    cell_1.draw_move(cell_2, False)
    cell_2.draw_move(cell_3, True)
    cell_3.draw_move(cell_4, False)
    cell_4.draw_move(cell_1, True)
    
    win.wait_for_close()


if __name__ == "__main__":
    main()
