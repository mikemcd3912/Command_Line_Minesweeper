import random, tkinter
from random import randint

class tile:
    def __init__(self) -> None:
        self.bomb=False
        self.flag=False
        self.covered=True
        self.proximity = 0

def makeGrid(gridSize: int)-> list:
    grid = [[tile() for _ in range(gridSize)] for _ in range(gridSize)]
    return grid

def spreadMines(mines: int, grid: list, gridSize: int):
    gridSize-=1
    while mines>0:
        x=random.randint(0,gridSize)
        y=random.randint(0,gridSize)
        focus = grid[y][x]
        if not focus.bomb:
            focus.bomb=True
            mines-=1
            if x-1>=0:
                grid[y][x-1].proximity+=1
            if x-1>=0 and y-1>=0:
                grid[y-1][x-1].proximity+=1
            if y-1>=0:
                grid[y-1][x].proximity+=1
            if y+1<=gridSize:
                grid[y+1][x].proximity+=1
            if y-1>=0 and x+1<=gridSize:
                grid[y-1][x+1].proximity+=1
            if x+1<=gridSize:
                grid[y][x+1].proximity+=1
            if x+1<=gridSize and y+1<=gridSize:
                grid[y+1][x+1].proximity+=1
            if x-1>=0 and y+1<=gridSize:
                grid[y+1][x-1].proximity+=1

def getCoordinates()->int:
    value = input()
    if value.isdigit():
        return int(value)
    else:
        return -1

def action(gameGrid: list)-> bool:
    gridSize=len(gameGrid)
    x=-1
    y=-1
    while x<0 or x>gridSize+1:
        print("Pease provide x coordinate between 1 and "+str(gridSize))
        x=getCoordinates()-1
    while y<0 or y>gridSize+1:
        print("Pease provide y coordinate between 1 and "+str(gridSize))
        y=getCoordinates()-1
    print("Clearing space (C) or Flag space (F)?")
    act = input()
    while not act == "C" and not act == "F":
        print ("Please select Clear (C) or Flag (F)")
        act = input()
    if act == "F":
        clear=False
    else:
        clear = True
    if clear and gameGrid[y][x].bomb:
        return True
    elif clear:
        if gameGrid[y][x].proximity==0:
            clearCells(x, y, gameGrid, gridSize)
        gameGrid[y][x].covered=False
        gameGrid[y][x].flag=False
        return False
    elif gameGrid[y][x].flag: 
        gameGrid[y][x].flag=False
        gameGrid[y][x].covered=True
        return False
    else: 
        gameGrid[y][x].flag=True
        gameGrid[y][x].covered=False
        return False


def clearCells(x: int, y: int, gameGrid: list, gridSize):
    gameGrid[y][x].covered=False
    if gameGrid[y][x].proximity==0:
        if x-1>=0 and gameGrid[y][x-1].covered:
            clearCells(x-1,y, gameGrid, gridSize)
        if x-1>=0 and y-1>=0 and gameGrid[y-1][x-1].covered:
            clearCells(x-1,y-1, gameGrid, gridSize)
        if y-1>=0 and gameGrid[y-1][x].covered:
            clearCells(x,y-1, gameGrid, gridSize)
        if y+1<gridSize and gameGrid[y+1][x].covered:
            clearCells(x,y+1, gameGrid, gridSize)
        if y-1>=0 and x+1<gridSize and gameGrid[y-1][x+1].covered:
            clearCells(x+1,y-1, gameGrid, gridSize)
        if x+1<gridSize and gameGrid[y][x+1].covered:
            clearCells(x+1,y, gameGrid, gridSize)
        if x+1<gridSize and y+1<gridSize and gameGrid[y+1][x+1].covered:
            clearCells(x+1, y+1, gameGrid, gridSize)
        if x-1>=0 and y+1<gridSize and gameGrid[y+1][x-1].covered:
            clearCells(x-1,y+1, gameGrid, gridSize)


def displayGrid(grid: list):
    gridSize = len(grid)
    large = gridSize>9
    rowStr="--"
    cols="   "
    for number in range(gridSize):
        if number<9:
            cols=cols+str(number+1)+"  "
        else:
            cols=cols+str(number+1)+" "
        rowStr=rowStr+"---"
    if large:
        print(" "+cols)
        print(rowStr+"--")
    else:
        print(cols)
        print(rowStr+"-")
    rowNum=1
    for row in grid:
        if large and rowNum<10:
            rowStr=str(rowNum)+" |"
        else:
            rowStr=str(rowNum)+"|"
        for tile in row:
            if tile.covered:
                rowStr=rowStr+" O "
            elif tile.flag:
                rowStr=rowStr+' P '
            elif tile.bomb:
                rowStr=rowStr+' X '
            elif not tile.covered and not tile.bomb:
                if tile.proximity>0:
                    rowStr=rowStr+" "+str(tile.proximity)+" "
                else:
                    rowStr=rowStr+"   "
        rowStr=rowStr+"|"
        print(rowStr)
        rowNum=rowNum+1
    rowStr="--"
    for _ in range(gridSize):
        rowStr=rowStr+"---"
    if large:
        print(rowStr+"--")
    else:
        print(rowStr+"-")

def getInput()->int:
    value = input()
    if value.isdigit():
        return int(value)
    else:
        print("Please enter number above 0")
        return -1
     
def checkWin(gameGrid: list)->bool:
    allUncovered = True
    for row in gameGrid:
        for tile in row:
            if tile.covered ==True:
                return False
    return allUncovered

def revealAll(gameGrid: list):
    for row in gameGrid:
        for tile in row:
            tile.covered=False
    displayGrid(gameGrid)

def newGame():
    print("Welcome to Minesweeper! How large a grid would you like to play?")
    gridSize=-1
    mines=-1
    while gridSize<0:
        gridSize = getInput()
    print("Excellent! And How many mines?")
    while mines<0:
        mines = getInput()
        if mines>=gridSize*gridSize:
            print("That's too many mines. Please enter a number less than the total of squares on the board")
            mines=-1
        
    # print("Would you to play on Command Line (Y) or interactive window? (N)")
    # response = input()
    # while not response == "Y" and not response == "N":
    #     print("Invalid input. Would you to play on Command Line (Y) or interactive window? (N)")
    #     response = str(input())
    # if response == "Y":
    commandLineGame(gridSize, mines)
    # else: 
    #     windowGUIGame(gridSize, mines)
    
def commandLineGame(gridSize: int, mines: int):
    gameGrid = makeGrid(gridSize)
    spreadMines(mines, gameGrid,gridSize)
    gameOver=False
    while not gameOver:
        displayGrid(gameGrid)
        gameOver=action(gameGrid)
        if(checkWin(gameGrid)):
            print("Congrats, You Won!")
            gameOver=True
    revealAll(gameGrid)
    print("Game over! Play Again?")

#def windowGUIGame(gridSize: int, mines: int):



if __name__ == "__main__":
    newGame()

