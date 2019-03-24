# minesweeper tiles

from graphics import *

class Tile:

    def __init__(self, win, fill, label, row, column, exposed, mine, total_rows, total_columns):
        self.fill = fill
        self.label = label
        self.exposed = exposed
        self.mine = mine
        self.row = row
        self.column = column
        width = 600 / total_columns
        height = 600 / total_rows
        change_x = 600 / total_columns
        change_y = 600 / total_rows
        self.center = Point((100 + change_x / 2) + change_x * column, (50 + change_y / 2) + change_y * row)
        self.xMin = self.center.getX() - width/2
        self.xMax = self.center.getX() + width/2
        self.yMin = self.center.getY() - height/2
        self.yMax = self.center.getY() + height/2
        pt1 = Point(self.xMin, self.yMin)
        pt2 = Point(self.xMax, self.yMax)
        self.outline = Rectangle(pt1, pt2)
        self.outline.setFill(self.fill)
        self.outline.draw(win)
        self.activate()

    def clicked(self, pt):
        wasClicked = False
        if self.xMin <= pt.getX() and self.xMax >= pt.getX():
            if self.yMin <= pt.getY() and self.yMax >= pt.getY():
                if self.active == True:
                    wasClicked = True
        return wasClicked

    def activate(self):
        self.outline.setWidth(2)
        self.active = True

    def deactivate(self):
        self.outline.setWidth(1)
        self.active = False

    def updateFill(self):
        if self.exposed == True:
            self.outline.setFill("beige")
        else:
            self.outline.setFill("white")

    def changeExposed(self):
        self.exposed = True
        self.deactivate()

    def changeText(self, win, label):
        self.label = label
        try:
            self.text.undraw()
        except AttributeError:
            blank = 0            
        self.text = Text(self.center, self.label)
        self.text.setSize(12)
        self.text.setStyle("bold")
        self.text.setFace("times roman")
        self.text.draw(win)

    def getMine(self):
        return self.mine

    def getRow(self):
        return self.row

    def getColumn(self):
        return self.column

    def getLabel(self):
        return self.label

    def getExposed(self):
        return self.exposed
