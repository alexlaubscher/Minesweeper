# minesweeper runner

from graphics import *
from button import *
from random import *
from Tile import *

def main():
    #rows, columns, mines = startUp()
    rows = 12
    columns = 12
    mines = 28
    win = GraphWin("MINESWEEPER", 900, 700)
    flag_button = Button(win, Point(800, 300), 100, 70, "FLAG")
    unflag_button = Button(win, Point(800, 400), 100, 70, "UNFLAG")
    restart_button = Button(win, Point(800, 500), 100, 70, "TRY AGAIN")
    quit_button = Button(win, Point(800, 600), 100, 70, "QUIT")
    flag_button.activate()
    unflag_button.activate()
    restart_button.activate()
    quit_button.activate()

    mine_list = [ ]
    for number in range(int(mines)):
        mine_list.append(1)
    filler = rows * columns - len(mine_list)
    for number in range(filler):
        mine_list.append(0)
    shuffle(mine_list)

    tile_list = [ ]
    fake_tile_list = [ ]
    counter = 0
    for i in range(int(columns)):
        small_tile_list = [ ]
        for k in range(int(rows)):
            if mine_list[counter] == 1:
                mine = True
            else:
                mine = False
            small_tile_list.append(Tile(win, "white", " ", k, i, False, mine, rows, columns))
            counter += 1
        fake_tile_list.append(small_tile_list)
        tile_list.append(small_tile_list)

    for i in tile_list:
        for k in i:
            k.changeText(win, k.getLabel())

    pt = win.getMouse()
    close = False
    while close == False:
        if restart_button.clicked(pt) == True:
            win.close()
            main()
        elif quit_button.clicked(pt):
            close = True
        elif flag_button.clicked(pt):
            pt = win.getMouse()
            out = False
            for k in tile_list:
                if out == True:
                    break
                else:
                    for tile in k:
                        if tile.clicked(pt) == True:
                            tile.changeText(win, "flagged")
                            out = True
                            break
        elif unflag_button.clicked(pt):
            pt = win.getMouse()
            out = False
            for k in tile_list:
                if out == True:
                    break
                else:
                    for tile in k:
                        if tile.clicked(pt) == True:
                            tile.changeText(win, " ")
                            out = True
                            break
        else:
            out = False
            for k in tile_list:
                if out == True:
                    break
                else:
                    for tile in k:
                        if tile.clicked(pt) == True:
                            if tile.getMine() == True:
                                game_over(win)
                                tile.changeText(win, "BOMB!")
                            else:
                                tile.changeExposed()
                                tile.updateFill()
                                nearby_mines = check_mines(tile, tile_list)
                                tile.changeText(win, str(nearby_mines))
                                if nearby_mines == 0:
                                    clear_squares(win, tile, tile_list)
                                out = True
                            break
        if close == False:        
            pt = win.getMouse()
    win.close()

def clear_squares(win, tile, tile_list):
    some_list = [-1, 0, 1]
    row = tile.getRow()
    column = tile.getColumn()
    for x in some_list:
        for y in some_list:
            if x == 0 and y == 0:
                count = 0
            else:
                index_one = column + x
                index_two = row + y
                if index_one > -1 and index_one < 12:
                    if index_two > -1 and index_two < 12:
                        if tile_list[index_one][index_two].getExposed() == False:
                            nearby_mines = check_mines(tile_list[index_one][index_two], tile_list)
                            tile_list[index_one][index_two].changeText(win, str(nearby_mines))
                            tile_list[index_one][index_two].changeExposed()
                            tile_list[index_one][index_two].updateFill()
                            if nearby_mines == 0:
                                clear_squares(win, tile_list[index_one][index_two], tile_list)
                        
    

    
def check_mines(tile, tile_list):
    count = 0
    some_list = [-1, 0, 1]
    row = tile.getRow()
    column = tile.getColumn()
    for x in some_list:
        for y in some_list:
            if x == 0 and y == 0:
                count += 0
            else:
                index_one = column + x
                index_two = row + y
                if index_one > -1 and index_one < 12:
                    if index_two > -1 and index_two < 12:
                        if tile_list[index_one][index_two].getMine() == True:
                            count += 1
    return count

def game_over(win):
    game_over_text = Text(Point(800, 200), "YOU LOST!")
    game_over_text.setSize(36)
    game_over_text.setStyle("bold")
    game_over_text.setFace("times roman")
    game_over_text.draw(win)

def startUp():
    win = GraphWin("START UP", 400, 200)
    row_entry = Entry(Point(250, 35), 6)
    row_entry.draw(win)
    column_entry = Entry(Point(250, 70), 6)
    column_entry.draw(win)
    mines_entry = Entry(Point(250, 105), 6)
    mines_entry.draw(win)
    Text(Point(125, 35), "# of Rows:").draw(win)
    Text(Point(125, 70), "# of Columns:").draw(win)
    Text(Point(125, 105), "# of Mines:").draw(win)
    start_button = Button(win, Point(200, 160), 80, 50, "START!")
    start_button.activate()
    pt = win.getMouse()
    while start_button.clicked(pt) == False:
        pt = win.getMouse()
    win.close()
    rows = row_entry.getText()
    columns = column_entry.getText()
    mines = mines_entry.getText()
    return rows, columns, mines

main()
        
