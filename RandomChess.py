# import the pygame module, so you can use it
import pygame
import math
import os
from pygame.locals import *


 # initialize the pygame module
pygame.display.init()
# load and set the logo
pygame.display.set_caption("Rando Chess")
 
# create a surface on screen that has the size of 240 x 180
window = pygame.display.set_mode((1280,720))

boardBG = pygame.image.load(os.path.join('images','board.png'))
mainmenu = pygame.image.load(os.path.join('images','mainmenu.png'))
highlight = pygame.image.load(os.path.join('images','highlight.png'))

wKnight = pygame.image.load(os.path.join('images','whiteKnight.png'))
WKsmall = pygame.transform.scale(wKnight,(32,32))
wRook = pygame.image.load(os.path.join('images','whiteRook.png'))
WRsmall = pygame.transform.scale(wRook,(32,32))
wBishop = pygame.image.load(os.path.join('images','whiteBishop.png'))
WBsmall = pygame.transform.scale(wBishop,(32,32))
wKing = pygame.image.load(os.path.join('images','whiteKing.png'))
wQueen = pygame.image.load(os.path.join('images','whiteQueen.png'))
WQsmall = pygame.transform.scale(wQueen,(32,32))
wPawn = pygame.image.load(os.path.join('images','whitePawn.png'))
WPsmall = pygame.transform.scale(wPawn,(32,32))

bKnight = pygame.image.load(os.path.join('images','blackKnight.png'))
BKsmall = pygame.transform.scale(bKnight,(32,32))
bRook = pygame.image.load(os.path.join('images','blackRook.png'))
BRsmall = pygame.transform.scale(bRook,(32,32))
bBishop = pygame.image.load(os.path.join('images','blackBishop.png'))
BBsmall = pygame.transform.scale(bBishop,(32,32))
bKing = pygame.image.load(os.path.join('images','blackKing.png'))
bQueen = pygame.image.load(os.path.join('images','blackQueen.png'))
BQsmall = pygame.transform.scale(bQueen,(32,32))
bPawn = pygame.image.load(os.path.join('images','blackPawn.png'))
BPsmall = pygame.transform.scale(bPawn,(32,32))

whiteRules = [0,1,2,3,4,5]
blackRules = [0,1,2,3,4,5]
whiteNextRules = [0,1,2,3,4,5]
blackNextRules = [0,1,2,3,4,5]
blackPiecesCaptured = []
whitePiecesCaptured = []
pieceLastClicked = (0,0)
whiteWins = False
blackWins = False
squareClicked = (0,0)
board = [["br","bn","bb","bq","bk","bb","bn","br"],["bp","bp","bp","bp","bp","bp","bp","bp"],["e","e","e","e","e","e","e","e"],["e","e","e","e","e","e","e","e"],["e","e","e","e","e","e","e","e"],["e","e","e","e","e","e","e","e"],["wp","wp","wp","wp","wp","wp","wp","wp"],["wr","wn","wb","wq","wk","wb","wn","wr"]]
#board = [["e","e","e","e","e","e","e","e"],["e","e","bq","e","wq","e","e","e"],["e","e","e","e","e","wk","e","e"],["e","bq","e","e","e","e","e","e"],["e","e","e","e","e","e","e","e"],["e","e","e","bq","e","e","bq","e"],["e","e","e","e","e","e","e","e"],["e","e","e","e","e","e","e","e"]]
boardHighlights = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]

blackCaptured = ["e"]
whiteCaptured = ["e"]

def updateRules(team):
    if team == "white":
        whiteRules = whiteNextRules
        for i in range(7):
            whiteNextRules[i] = random.randint(0,6)
    elif team == "black":
        blackRules = blackNextRules
        for i in range(7):
            blackNextRules[i] = random.randint(0,6)

#gives top-left corner of square in coords        
def ConvertToScreenCoords(chessSquare):
        (row,col) = chessSquare
        screenX = 33 + col*82
        screenY = 33 + row*82
        return (screenX,screenY)

#gives chess square containing given coords		
def ConvertToChessCoords(square):
        (X,Y) = square
        row = math.floor((Y-33) / 82)
        col = math.floor((X-33) / 82)
        return (row,col)

#gives top-left corner of square in coords        
def ConvertCapturedWhiteToScreenCoords(chessSquare):
        (row,col) = chessSquare
        screenX = 726 + col*32
        screenY = 13 + row*32
        return (screenX,screenY)

#gives chess square containing given coords		
def ConvertToCapturedWhiteCoords(square):
        (X,Y) = square
        row = math.floor((Y-726) / 32)
        col = math.floor((X-13) / 32)
        return (row,col)

#gives top-left corner of square in coords        
def ConvertCapturedBlackToScreenCoords(chessSquare):
        (row,col) = chessSquare
        screenX = 726 + col*32
        screenY = 376 + row*32
        return (screenX,screenY)

#gives chess square containing given coords		
def ConvertToCapturedBlackCoords(square):
        (X,Y) = square
        row = math.floor((Y-726) / 32)
        col = math.floor((X-376) / 32)
        return (row,col)

def getPieceType(pieceString):
    if pieceString == "e":
        return 6
    final = pieceString[1]
    if final == "p":
        return 0
    elif final == "r":
        return 1
    elif final == "n":
        return 2
    elif final == "b":
        return 3
    elif final == "q":
        return 4
    elif final == "k":
        return 5

def displayHighlights():
    for i in range(8):
        for j in range(8):
            if boardHighlights[i][j] == 1:
                window.blit(highlight, ConvertToScreenCoords((i,j)))

def setHighlightSquare(x,y):
    if x<=7 and x>=0:
        if y>=0 and y<=7:
            boardHighlights[x][y] = 1
    
def clearHighlights():
    for i in range(8):
            for j in range(8):
                boardHighlights[i][j] = 0

def isBlackPiece(x,y):
    if x<=7 and x>=0:
        if y>=0 and y<=7:
            oPiece = board[x][y]
            if oPiece[0] == "b":
                return True
            else:
                return False      

def isWhitePiece(x,y):
    if x<=7 and x>=0:
        if y>=0 and y<=7:
            oPiece = board[x][y]
            if oPiece[0] == "w":
                return True
            else:
                return False       
        
##def highlightMovesBlack(square):
##    piece = getPieceType(board[square[0]][square[1]])
    

def highlightMovesWhite(square):
    clearHighlights()
    pieceX = square[0]
    pieceY = square[1]
    piece = getPieceType(board[pieceX][pieceY])
    if piece != 6 and isWhitePiece(pieceX,pieceY):
        movesLike = whiteRules[piece]
        if movesLike == 0:
            if not isBlackPiece(pieceX-1,pieceY) and not isWhitePiece(pieceX-1,pieceY):
                setHighlightSquare(pieceX-1,pieceY)
            if pieceX == 6:
                if not isBlackPiece(pieceX-2,pieceY) and not isWhitePiece(pieceX-2,pieceY):
                    setHighlightSquare(pieceX-2,pieceY)
            if isBlackPiece(pieceX-1,pieceY-1):
                setHighlightSquare(pieceX-1,pieceY-1)
            if isBlackPiece(pieceX-1,pieceY+1):
                setHighlightSquare(pieceX-1,pieceY+1)
                
        elif movesLike == 1:
            for i in range(1,8):
                if isBlackPiece(pieceX+i,pieceY):
                    setHighlightSquare(pieceX+i,pieceY)
                    break
                elif isWhitePiece(pieceX+i,pieceY):
                    break
                else:
                    setHighlightSquare(pieceX+i,pieceY)
            
            for i in range(1,8):
                if isBlackPiece(pieceX-i,pieceY):
                    setHighlightSquare(pieceX-i,pieceY)
                    break
                elif isWhitePiece(pieceX-i,pieceY):
                    break
                else:
                    setHighlightSquare(pieceX-i,pieceY)
                    
            for i in range(1,8):
                if isBlackPiece(pieceX,pieceY+i):
                    setHighlightSquare(pieceX,pieceY+i)
                    break
                elif isWhitePiece(pieceX,pieceY+i):
                    break
                else:
                    setHighlightSquare(pieceX,pieceY+i)
                    
            for i in range(1,8):
                if isBlackPiece(pieceX,pieceY-i):
                    setHighlightSquare(pieceX,pieceY-i)
                    break
                elif isWhitePiece(pieceX,pieceY-i):
                    break
                else:
                    setHighlightSquare(pieceX,pieceY-i)

        elif movesLike == 2:
            if not isWhitePiece(pieceX+2,pieceY+1):
                setHighlightSquare(pieceX+2,pieceY+1)
            if not isWhitePiece(pieceX+2,pieceY-1):
                setHighlightSquare(pieceX+2,pieceY-1)
            if not isWhitePiece(pieceX+1,pieceY-2):
                setHighlightSquare(pieceX+1,pieceY-2)
            if not isWhitePiece(pieceX+1,pieceY+2):
                setHighlightSquare(pieceX+1,pieceY+2)
            if not isWhitePiece(pieceX-1,pieceY-2):
                setHighlightSquare(pieceX-1,pieceY-2)
            if not isWhitePiece(pieceX-1,pieceY+2):
                setHighlightSquare(pieceX-1,pieceY+2)
            if not isWhitePiece(pieceX-2,pieceY+1):
                setHighlightSquare(pieceX-2,pieceY+1)
            if not isWhitePiece(pieceX-2,pieceY-1):
                setHighlightSquare(pieceX-2,pieceY-1)
                
        elif movesLike == 3:
            for i in range(1,8):
                if isBlackPiece(pieceX+i,pieceY+i):
                    setHighlightSquare(pieceX+i,pieceY+i)
                    break
                elif isWhitePiece(pieceX+i,pieceY+i):
                    break
                else:
                    setHighlightSquare(pieceX+i,pieceY+i)
            for i in range(1,8):
                if isBlackPiece(pieceX-i,pieceY+i):
                    setHighlightSquare(pieceX-i,pieceY+i)
                    break
                elif isWhitePiece(pieceX-i,pieceY+i):
                    break
                else:
                    setHighlightSquare(pieceX-i,pieceY+i)     
            for i in range(1,8):
                if isBlackPiece(pieceX-i,pieceY-i):
                    setHighlightSquare(pieceX-i,pieceY-i)
                    break
                elif isWhitePiece(pieceX-i,pieceY-i):
                    break
                else:
                    setHighlightSquare(pieceX-i,pieceY-i)
            for i in range(1,8):
                if isBlackPiece(pieceX+i,pieceY-i):
                    setHighlightSquare(pieceX+i,pieceY-i)
                    break
                elif isWhitePiece(pieceX+i,pieceY-i):
                    break
                else:
                    setHighlightSquare(pieceX+i,pieceY-i)

                    
        elif movesLike == 4:
            for i in range(1,8):
                if isBlackPiece(pieceX+i,pieceY):
                    setHighlightSquare(pieceX+i,pieceY)
                    break
                elif isWhitePiece(pieceX+i,pieceY):
                    break
                else:
                    setHighlightSquare(pieceX+i,pieceY)
            
            for i in range(1,8):
                if isBlackPiece(pieceX-i,pieceY):
                    setHighlightSquare(pieceX-i,pieceY)
                    break
                elif isWhitePiece(pieceX-i,pieceY):
                    break
                else:
                    setHighlightSquare(pieceX-i,pieceY)
                    
            for i in range(1,8):
                if isBlackPiece(pieceX,pieceY+i):
                    setHighlightSquare(pieceX,pieceY+i)
                    break
                elif isWhitePiece(pieceX,pieceY+i):
                    break
                else:
                    setHighlightSquare(pieceX,pieceY+i)
                    
            for i in range(1,8):
                if isBlackPiece(pieceX,pieceY-i):
                    setHighlightSquare(pieceX,pieceY-i)
                    break
                elif isWhitePiece(pieceX,pieceY-i):
                    break
                else:
                    setHighlightSquare(pieceX,pieceY-i)
            for i in range(1,8):
                if isBlackPiece(pieceX+i,pieceY+i):
                    setHighlightSquare(pieceX+i,pieceY+i)
                    break
                elif isWhitePiece(pieceX+i,pieceY+i):
                    break
                else:
                    setHighlightSquare(pieceX+i,pieceY+i)
            for i in range(1,8):
                if isBlackPiece(pieceX-i,pieceY+i):
                    setHighlightSquare(pieceX-i,pieceY+i)
                    break
                elif isWhitePiece(pieceX-i,pieceY+i):
                    break
                else:
                    setHighlightSquare(pieceX-i,pieceY+i)     
            for i in range(1,8):
                if isBlackPiece(pieceX-i,pieceY-i):
                    setHighlightSquare(pieceX-i,pieceY-i)
                    break
                elif isWhitePiece(pieceX-i,pieceY-i):
                    break
                else:
                    setHighlightSquare(pieceX-i,pieceY-i)
            for i in range(1,8):
                if isBlackPiece(pieceX+i,pieceY-i):
                    setHighlightSquare(pieceX+i,pieceY-i)
                    break
                elif isWhitePiece(pieceX+i,pieceY-i):
                    break
                else:
                    setHighlightSquare(pieceX+i,pieceY-i)
                    
        elif movesLike == 5:
            for i in range(-1,2):
                for j in range(-1,2):
                    if not isWhitePiece(pieceX+i,pieceY+j):
                        setHighlightSquare(pieceX+i,pieceY+j)

def moveWhitePiece(fromSquare, toSquare):
    pieceX = fromSquare[0]
    pieceY = fromSquare[1]
    toX = toSquare[0]
    toY = toSquare[1]
    if isBlackPiece(toX,toY):
        if board[toX][toY] == "bk":
            whiteWins = True
        else:
            blackPiecesCaptured.append(board[toX][toY])
    board[toX][toY] = board[pieceX][pieceY]
    board[pieceX][pieceY] = "e"
    clearHighlights()
        
def displayCapturedBlackPieces():
    i = 0
    j = 0
    for x in blackPiecesCaptured:
        if x == "bp":
            window.blit(BPsmall,ConvertCapturedBlackToScreenCoords((i,j)))
        elif x == "br":
            window.blit(BRsmall,ConvertCapturedBlackToScreenCoords((i,j)))
        elif x == "bn":
            window.blit(BKsmall,ConvertCapturedBlackToScreenCoords((i,j)))
        elif x == "bb":
            window.blit(BBsmall,ConvertCapturedBlackToScreenCoords((i,j)))
        elif x == "bq":
            window.blit(BQsmall,ConvertCapturedBlackToScreenCoords((i,j)))
        j+=1
        if j==3:
            j=0
            i+=1

def displayCapturedWhitePieces():
    i = 0
    j = 0
    for x in whitePiecesCaptured:
        if x == "wp":
            window.blit(WPsmall, ConvertCapturedWhiteToScreenCoords((i,j)))
        elif x == "wr":
            window.blit(WRsmall, ConvertCapturedWhiteToScreenCoords((i,j)))
        elif x == "wn":
            window.blit(WKsmall, ConvertCapturedWhiteToScreenCoords((i,j)))
        elif x == "wb":
            window.blit(WBsmall, ConvertCapturedWhiteToScreenCoords((i,j)))
        elif x == "wq":
            window.blit(WQsmall, ConvertCapturedWhiteToScreenCoords((i,j)))
        j+=1
        if j==3:
            j=0
            i+=1

def displayPieces():
    for i in range(8):
        for j in range(8):
            if board[i][j] == "bp":
                window.blit(bPawn, ConvertToScreenCoords((i,j)))
            elif board[i][j] == "br":
                window.blit(bRook, ConvertToScreenCoords((i,j)))
            elif board[i][j] == "bn":
                window.blit(bKnight, ConvertToScreenCoords((i,j)))
            elif board[i][j] == "bb":
                window.blit(bBishop, ConvertToScreenCoords((i,j)))
            elif board[i][j] == "bq":
                window.blit(bQueen, ConvertToScreenCoords((i,j)))
            elif board[i][j] == "bk":
                window.blit(bKing, ConvertToScreenCoords((i,j)))
            elif board[i][j] == "wp":
                window.blit(wPawn, ConvertToScreenCoords((i,j)))
            elif board[i][j] == "wr":
                window.blit(wRook, ConvertToScreenCoords((i,j)))
            elif board[i][j] == "wn":
                window.blit(wKnight, ConvertToScreenCoords((i,j)))
            elif board[i][j] == "wb":
                window.blit(wBishop, ConvertToScreenCoords((i,j)))
            elif board[i][j] == "wq":
                window.blit(wQueen, ConvertToScreenCoords((i,j)))
            elif board[i][j] == "wk":
                window.blit(wKing, ConvertToScreenCoords((i,j)))
            
        
def main(): 
    #0=main menu, 1=game, 2=options
    screen = 0
    #0=ai, 1=2-player
    gamemode = 0
    dummy = 0
   

     
    # define a variable to control the main loop
    running = True
    white = (255, 255, 255)
     
    # main loop
    while running:
        pygame.event.get()
        pygame.display.flip()
        window.fill(white) 
        #main menu
        if screen == 0:
            window.blit(mainmenu, (0, 0))
        #game screen    
        elif screen == 1:
            window.blit(boardBG, (0, 0))
            displayHighlights()
            displayPieces()
            displayCapturedBlackPieces()
            displayCapturedWhitePieces()
        #options    
        elif screen == 2:
            window.blit(bBishop, (x, y))


            
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]
                if screen == 0:
                    if x >=410 and x<=870:
                        if y >= 320 and y <= 438:
                            screen = 1
                            gamemode = 0
                        elif y >= 500 and y <= 620:
                            screen = 1
                            gamemode = 1
                elif screen == 1:
                    squareClicked = ConvertToChessCoords(pos)
                    boardx = squareClicked[0]
                    boardy = squareClicked[1]
                    if x>=33 and x<=685:
                        if y>=33 and y<=685:
                            if boardHighlights[boardx][boardy] == 1:
                                moveWhitePiece(pieceLastClicked,squareClicked)
                            else:
                                pieceLastClicked = squareClicked
                                highlightMovesWhite(squareClicked)
            if event.type == pygame.KEYDOWN:
                dummy = 0
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
                pygame.quit()

main()
     
