# import the pygame module, so you can use it
import pygame
import math
import os
import random
from pygame.locals import *
import convertUtils as ct

 # initialize the pygame module
pygame.display.init()
pygame.font.init()
# load and set the logo
pygame.display.set_caption("Rando Chess")
 
# create a surface on screen that has the size of 240 x 180
window = pygame.display.set_mode((1280,720))

boardBG = pygame.image.load(os.path.join('images','board.png'))
mainmenu = pygame.image.load(os.path.join('images','mainmenu.png'))
highlight = pygame.image.load(os.path.join('images','highlight.png'))
whitewins = pygame.image.load(os.path.join('images','whitewins.png'))
blackwins = pygame.image.load(os.path.join('images','blackwins.png'))
turnIndic = pygame.image.load(os.path.join('images','turn.png'))

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


blackPiecesCaptured = []
whitePiecesCaptured = []
pieceLastClicked = (0,0)
#winner 1=black, 2=white
winner = 0
squareClicked = (0,0)
board = [["br","bn","bb","bq","bk","bb","bn","br"],["bp","bp","bp","bp","bp","bp","bp","bp"],["e","e","e","e","e","e","e","e"],["e","e","e","e","e","e","e","e"],["e","e","e","e","e","e","e","e"],["e","e","e","e","e","e","e","e"],["wp","wp","wp","wp","wp","wp","wp","wp"],["wr","wn","wb","wq","wk","wb","wn","wr"]]
#board = [["e","e","e","e","e","e","e","e"],["e","e","bq","e","wq","e","e","e"],["e","e","e","e","e","wk","e","e"],["e","bq","e","e","e","e","e","e"],["e","e","e","e","e","e","e","e"],["e","e","e","bq","e","e","bq","e"],["e","e","e","e","e","e","e","e"],["e","e","e","e","e","e","e","e"]]
whiteRules = [0,1,2,3,4,5]
whiteNextRules = [0,1,2,3,4,5]
blackRules = [0,1,2,3,4,5]
blackNextRules = [0,1,2,3,4,5]
boardHighlights = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]

theFont = pygame.font.Font('Heathergreen.ttf', 38)
winFont = pygame.font.Font('Heathergreen.ttf', 200)


def updateRules(team):
    global whiteRules
    global whiteNextRules
    global blackRules
    global blackNextRules
    if team == "white":
        whiteRules = whiteNextRules.copy()
        for i in range(6):
            whiteNextRules[i] = random.randint(0,5)
    elif team == "black":
        blackRules = blackNextRules.copy()
        for i in range(6):
            blackNextRules[i] = random.randint(0,5)

def resetRules():
    global whiteRules
    global whiteNextRules
    global blackRules
    global blackNextRules
    whiteRules = [0,1,2,3,4,5]
    whiteNextRules = [0,1,2,3,4,5]
    blackRules = [0,1,2,3,4,5]
    blackNextRules = [0,1,2,3,4,5]

def resetCaptures():
    global blackPiecesCaptured
    global whitePiecesCaptured
    for i in range(len(blackPiecesCaptured)):
        blackPiecesCaptured[i] = "e"
    for i in range(len(whitePiecesCaptured)):
        whitePiecesCaptured[i] = "e"
    
def displayRules():
    blackR1 = theFont.render('Pawns move like '+ct.convertPieceNumberToName(blackRules[0])+'s             Bishops move like '+ct.convertPieceNumberToName(blackRules[3])+'s', True, (255, 255, 255))
    blackR2 = theFont.render('Rooks move like '+ct.convertPieceNumberToName(blackRules[1])+'s             Queens move like '+ct.convertPieceNumberToName(blackRules[4])+'s', True, (255, 255, 255))
    blackR3 = theFont.render('Knights move like '+ct.convertPieceNumberToName(blackRules[2])+'s             Kings move like '+ct.convertPieceNumberToName(blackRules[5])+'s', True, (255, 255, 255))
    window.blit(blackR1,(840,37))
    window.blit(blackR2,(840,80))
    window.blit(blackR3,(840,123))
    blackN1 = theFont.render('Pawns move like '+ct.convertPieceNumberToName(blackNextRules[0])+'s             Bishops move like '+ct.convertPieceNumberToName(blackNextRules[3])+'s', True, (255, 255, 255))
    blackN2 = theFont.render('Rooks move like '+ct.convertPieceNumberToName(blackNextRules[1])+'s             Queens move like '+ct.convertPieceNumberToName(blackNextRules[4])+'s', True, (255, 255, 255))
    blackN3 = theFont.render('Knights move like '+ct.convertPieceNumberToName(blackNextRules[2])+'s             Kings move like '+ct.convertPieceNumberToName(blackNextRules[5])+'s', True, (255, 255, 255))
    window.blit(blackN1,(840,217))
    window.blit(blackN2,(840,260))
    window.blit(blackN3,(840,303))

    
    whiteR1 = theFont.render('Pawns move like '+ct.convertPieceNumberToName(whiteRules[0])+'s             Bishops move like '+ct.convertPieceNumberToName(whiteRules[3])+'s', True, (0, 0, 0))
    whiteR2 = theFont.render('Rooks move like '+ct.convertPieceNumberToName(whiteRules[1])+'s             Queens move like '+ct.convertPieceNumberToName(whiteRules[4])+'s', True, (0, 0, 0))
    whiteR3 = theFont.render('Knights move like '+ct.convertPieceNumberToName(whiteRules[2])+'s             Kings move like '+ct.convertPieceNumberToName(whiteRules[5])+'s', True, (0, 0, 0))
    window.blit(whiteR1,(840,402))
    window.blit(whiteR2,(840,445))
    window.blit(whiteR3,(840,488))
    whiteN1 = theFont.render('Pawns move like '+ct.convertPieceNumberToName(whiteNextRules[0])+'s             Bishops move like '+ct.convertPieceNumberToName(whiteNextRules[3])+'s', True, (0, 0, 0))
    whiteN2 = theFont.render('Rooks move like '+ct.convertPieceNumberToName(whiteNextRules[1])+'s             Queens move like '+ct.convertPieceNumberToName(whiteNextRules[4])+'s', True, (0, 0, 0))
    whiteN3 = theFont.render('Knights move like '+ct.convertPieceNumberToName(whiteNextRules[2])+'s             Kings move like '+ct.convertPieceNumberToName(whiteNextRules[5])+'s', True, (0, 0, 0))
    window.blit(whiteN1,(840,582))
    window.blit(whiteN2,(840,625))
    window.blit(whiteN3,(840,668))


def printWhiteRules():
    dummy =1
##    print("This Turn:")
##    print("Pawns move like ",convertPieceNumberToName(whiteRules[0]),"s")
##    print("Rooks move like ",convertPieceNumberToName(whiteRules[1]),"s")
##    print("Knights move like ",convertPieceNumberToName(whiteRules[2]),"s")
##    print("Bishops move like ",convertPieceNumberToName(whiteRules[3]),"s")
##    print("Queens move like ",convertPieceNumberToName(whiteRules[4]),"s")
##    print("Kings move like ",convertPieceNumberToName(whiteRules[5]),"s")
##    print("Next Turn:")
##    print("Pawns move like ",convertPieceNumberToName(whiteNextRules[0]),"s")
##    print("Rooks move like ",convertPieceNumberToName(whiteNextRules[1]),"s")
##    print("Knights move like ",convertPieceNumberToName(whiteNextRules[2]),"s")
##    print("Bishops move like ",convertPieceNumberToName(whiteNextRules[3]),"s")
##    print("Queens move like ",convertPieceNumberToName(whiteNextRules[4]),"s")
##    print("Kings move like ",convertPieceNumberToName(whiteNextRules[5]),"s")

def printBlackRules():
    dummy =2
##    print("This Turn:")
##    print("Pawns move like ",convertPieceNumberToName(blackRules[0]),"s")
##    print("Rooks move like ",convertPieceNumberToName(blackRules[1]),"s")
##    print("Knights move like ",convertPieceNumberToName(blackRules[2]),"s")
##    print("Bishops move like ",convertPieceNumberToName(blackRules[3]),"s")
##    print("Queens move like ",convertPieceNumberToName(blackRules[4]),"s")
##    print("Kings move like ",convertPieceNumberToName(blackRules[5]),"s")
##    print("Next Turn:")
##    print("Pawns move like ",convertPieceNumberToName(blackNextRules[0]),"s")
##    print("Rooks move like ",convertPieceNumberToName(blackNextRules[1]),"s")
##    print("Knights move like ",convertPieceNumberToName(blackNextRules[2]),"s")
##    print("Bishops move like ",convertPieceNumberToName(blackNextRules[3]),"s")
##    print("Queens move like ",convertPieceNumberToName(blackNextRules[4]),"s")
##    print("Kings move like ",convertPieceNumberToName(blackNextRules[5]),"s")


def displayHighlights():
    for i in range(8):
        for j in range(8):
            if boardHighlights[i][j] == 1:
                window.blit(highlight, ct.ConvertToScreenCoords((i,j)))

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
        
def highlightMovesBlack(square):
    clearHighlights()
    pieceX = square[0]
    pieceY = square[1]
    piece = ct.convertPieceNameToNumber(board[pieceX][pieceY])
    if piece != 6 and isBlackPiece(pieceX,pieceY):
        movesLike = blackRules[piece]
        if movesLike == 0:
            if not isWhitePiece(pieceX+1,pieceY) and not isBlackPiece(pieceX+1,pieceY):
                setHighlightSquare(pieceX+1,pieceY)
            if pieceX == 1:
                if not isWhitePiece(pieceX+2,pieceY) and not isBlackPiece(pieceX+2,pieceY):
                    setHighlightSquare(pieceX+2,pieceY)
            if isWhitePiece(pieceX+1,pieceY+1):
                setHighlightSquare(pieceX+1,pieceY+1)
            if isWhitePiece(pieceX+1,pieceY-1):
                setHighlightSquare(pieceX+1,pieceY-1)
                
        elif movesLike == 1:
            for i in range(1,8):
                if isWhitePiece(pieceX+i,pieceY):
                    setHighlightSquare(pieceX+i,pieceY)
                    break
                elif isBlackPiece(pieceX+i,pieceY):
                    break
                else:
                    setHighlightSquare(pieceX+i,pieceY)
            
            for i in range(1,8):
                if isWhitePiece(pieceX-i,pieceY):
                    setHighlightSquare(pieceX-i,pieceY)
                    break
                elif isBlackPiece(pieceX-i,pieceY):
                    break
                else:
                    setHighlightSquare(pieceX-i,pieceY)
                    
            for i in range(1,8):
                if isWhitePiece(pieceX,pieceY+i):
                    setHighlightSquare(pieceX,pieceY+i)
                    break
                elif isBlackPiece(pieceX,pieceY+i):
                    break
                else:
                    setHighlightSquare(pieceX,pieceY+i)
                    
            for i in range(1,8):
                if isWhitePiece(pieceX,pieceY-i):
                    setHighlightSquare(pieceX,pieceY-i)
                    break
                elif isBlackPiece(pieceX,pieceY-i):
                    break
                else:
                    setHighlightSquare(pieceX,pieceY-i)

        elif movesLike == 2:
            if not isBlackPiece(pieceX+2,pieceY+1):
                setHighlightSquare(pieceX+2,pieceY+1)
            if not isBlackPiece(pieceX+2,pieceY-1):
                setHighlightSquare(pieceX+2,pieceY-1)
            if not isBlackPiece(pieceX+1,pieceY-2):
                setHighlightSquare(pieceX+1,pieceY-2)
            if not isBlackPiece(pieceX+1,pieceY+2):
                setHighlightSquare(pieceX+1,pieceY+2)
            if not isBlackPiece(pieceX-1,pieceY-2):
                setHighlightSquare(pieceX-1,pieceY-2)
            if not isBlackPiece(pieceX-1,pieceY+2):
                setHighlightSquare(pieceX-1,pieceY+2)
            if not isBlackPiece(pieceX-2,pieceY+1):
                setHighlightSquare(pieceX-2,pieceY+1)
            if not isBlackPiece(pieceX-2,pieceY-1):
                setHighlightSquare(pieceX-2,pieceY-1)
                
        elif movesLike == 3:
            for i in range(1,8):
                if isWhitePiece(pieceX+i,pieceY+i):
                    setHighlightSquare(pieceX+i,pieceY+i)
                    break
                elif isBlackPiece(pieceX+i,pieceY+i):
                    break
                else:
                    setHighlightSquare(pieceX+i,pieceY+i)
            for i in range(1,8):
                if isWhitePiece(pieceX-i,pieceY+i):
                    setHighlightSquare(pieceX-i,pieceY+i)
                    break
                elif isBlackPiece(pieceX-i,pieceY+i):
                    break
                else:
                    setHighlightSquare(pieceX-i,pieceY+i)     
            for i in range(1,8):
                if isWhitePiece(pieceX-i,pieceY-i):
                    setHighlightSquare(pieceX-i,pieceY-i)
                    break
                elif isBlackPiece(pieceX-i,pieceY-i):
                    break
                else:
                    setHighlightSquare(pieceX-i,pieceY-i)
            for i in range(1,8):
                if isWhitePiece(pieceX+i,pieceY-i):
                    setHighlightSquare(pieceX+i,pieceY-i)
                    break
                elif isBlackPiece(pieceX+i,pieceY-i):
                    break
                else:
                    setHighlightSquare(pieceX+i,pieceY-i)

                    
        elif movesLike == 4:
            for i in range(1,8):
                if isWhitePiece(pieceX+i,pieceY):
                    setHighlightSquare(pieceX+i,pieceY)
                    break
                elif isBlackPiece(pieceX+i,pieceY):
                    break
                else:
                    setHighlightSquare(pieceX+i,pieceY)
            
            for i in range(1,8):
                if isWhitePiece(pieceX-i,pieceY):
                    setHighlightSquare(pieceX-i,pieceY)
                    break
                elif isBlackPiece(pieceX-i,pieceY):
                    break
                else:
                    setHighlightSquare(pieceX-i,pieceY)
                    
            for i in range(1,8):
                if isWhitePiece(pieceX,pieceY+i):
                    setHighlightSquare(pieceX,pieceY+i)
                    break
                elif isBlackPiece(pieceX,pieceY+i):
                    break
                else:
                    setHighlightSquare(pieceX,pieceY+i)
                    
            for i in range(1,8):
                if isWhitePiece(pieceX,pieceY-i):
                    setHighlightSquare(pieceX,pieceY-i)
                    break
                elif isBlackPiece(pieceX,pieceY-i):
                    break
                else:
                    setHighlightSquare(pieceX,pieceY-i)
            for i in range(1,8):
                if isWhitePiece(pieceX+i,pieceY+i):
                    setHighlightSquare(pieceX+i,pieceY+i)
                    break
                elif isBlackPiece(pieceX+i,pieceY+i):
                    break
                else:
                    setHighlightSquare(pieceX+i,pieceY+i)
            for i in range(1,8):
                if isWhitePiece(pieceX-i,pieceY+i):
                    setHighlightSquare(pieceX-i,pieceY+i)
                    break
                elif isBlackPiece(pieceX-i,pieceY+i):
                    break
                else:
                    setHighlightSquare(pieceX-i,pieceY+i)     
            for i in range(1,8):
                if isWhitePiece(pieceX-i,pieceY-i):
                    setHighlightSquare(pieceX-i,pieceY-i)
                    break
                elif isBlackPiece(pieceX-i,pieceY-i):
                    break
                else:
                    setHighlightSquare(pieceX-i,pieceY-i)
            for i in range(1,8):
                if isWhitePiece(pieceX+i,pieceY-i):
                    setHighlightSquare(pieceX+i,pieceY-i)
                    break
                elif isBlackPiece(pieceX+i,pieceY-i):
                    break
                else:
                    setHighlightSquare(pieceX+i,pieceY-i)
                    
        elif movesLike == 5:
            for i in range(-1,2):
                for j in range(-1,2):
                    if not isBlackPiece(pieceX+i,pieceY+j):
                        setHighlightSquare(pieceX+i,pieceY+j)
    

def highlightMovesWhite(square):
    clearHighlights()
    pieceX = square[0]
    pieceY = square[1]
    piece = ct.convertPieceNameToNumber(board[pieceX][pieceY])
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


def moveBlackPiece(fromSquare, toSquare):
    global winner
    pieceX = fromSquare[0]
    pieceY = fromSquare[1]
    toX = toSquare[0]
    toY = toSquare[1]
    if isWhitePiece(toX,toY):
        if board[toX][toY] != "wk":
            whitePiecesCaptured.append(board[toX][toY])
        else:
            winner = 1
    board[toX][toY] = board[pieceX][pieceY]
    board[pieceX][pieceY] = "e"
    clearHighlights()

def moveWhitePiece(fromSquare, toSquare):
    global winner
    pieceX = fromSquare[0]
    pieceY = fromSquare[1]
    toX = toSquare[0]
    toY = toSquare[1]
    if isBlackPiece(toX,toY):
        if board[toX][toY] != "bk":
            blackPiecesCaptured.append(board[toX][toY])
        else:
            winner = 2
    board[toX][toY] = board[pieceX][pieceY]
    board[pieceX][pieceY] = "e"
    clearHighlights()

        
def displayCapturedBlackPieces():
    i = 0
    j = 0
    for x in blackPiecesCaptured:
        if x == "bp":
            window.blit(BPsmall,ct.ConvertCapturedBlackToScreenCoords((i,j)))
        elif x == "br":
            window.blit(BRsmall,ct.ConvertCapturedBlackToScreenCoords((i,j)))
        elif x == "bn":
            window.blit(BKsmall,ct.ConvertCapturedBlackToScreenCoords((i,j)))
        elif x == "bb":
            window.blit(BBsmall,ct.ConvertCapturedBlackToScreenCoords((i,j)))
        elif x == "bq":
            window.blit(BQsmall,ct.ConvertCapturedBlackToScreenCoords((i,j)))
        j+=1
        if j==3:
            j=0
            i+=1

def displayCapturedWhitePieces():
    i = 0
    j = 0
    for x in whitePiecesCaptured:
        if x == "wp":
            window.blit(WPsmall, ct.ConvertCapturedWhiteToScreenCoords((i,j)))
        elif x == "wr":
            window.blit(WRsmall, ct.ConvertCapturedWhiteToScreenCoords((i,j)))
        elif x == "wn":
            window.blit(WKsmall, ct.ConvertCapturedWhiteToScreenCoords((i,j)))
        elif x == "wb":
            window.blit(WBsmall, ct.ConvertCapturedWhiteToScreenCoords((i,j)))
        elif x == "wq":
            window.blit(WQsmall, ct.ConvertCapturedWhiteToScreenCoords((i,j)))
        j+=1
        if j==3:
            j=0
            i+=1

def displayPieces():
    for i in range(8):
        for j in range(8):
            if board[i][j] == "bp":
                window.blit(bPawn, ct.ConvertToScreenCoords((i,j)))
            elif board[i][j] == "br":
                window.blit(bRook, ct.ConvertToScreenCoords((i,j)))
            elif board[i][j] == "bn":
                window.blit(bKnight, ct.ConvertToScreenCoords((i,j)))
            elif board[i][j] == "bb":
                window.blit(bBishop, ct.ConvertToScreenCoords((i,j)))
            elif board[i][j] == "bq":
                window.blit(bQueen, ct.ConvertToScreenCoords((i,j)))
            elif board[i][j] == "bk":
                window.blit(bKing, ct.ConvertToScreenCoords((i,j)))
            elif board[i][j] == "wp":
                window.blit(wPawn, ct.ConvertToScreenCoords((i,j)))
            elif board[i][j] == "wr":
                window.blit(wRook, ct.ConvertToScreenCoords((i,j)))
            elif board[i][j] == "wn":
                window.blit(wKnight, ct.ConvertToScreenCoords((i,j)))
            elif board[i][j] == "wb":
                window.blit(wBishop, ct.ConvertToScreenCoords((i,j)))
            elif board[i][j] == "wq":
                window.blit(wQueen, ct.ConvertToScreenCoords((i,j)))
            elif board[i][j] == "wk":
                window.blit(wKing, ct.ConvertToScreenCoords((i,j)))
            
        
def main():
    #0=main menu, 1=game, 2=options
    screen = 0
    global winner
    global board
    #0=ai, 1=2-player
    gamemode = 0
    dummy = 0
    updateRules("white")
    updateRules("black")
     
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
            displayRules()
            displayHighlights()
            displayPieces()
            displayCapturedBlackPieces()
            displayCapturedWhitePieces()
            if turn%2 == 0:
                window.blit(turnIndic,(711,-10))
            else:
                window.blit(turnIndic,(711,358))
            if winner == 1:
                window.blit(blackwins,(0,0))
            elif winner == 2:
                window.blit(whitewins,(0,0))
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
                            turn = 1
                            gamemode = 0
                            winner = 0
                        elif y >= 500 and y <= 620:
                            screen = 1
                            turn = 1
                            gamemode = 1
                            winner = 0
                elif screen == 1:
                    squareClicked = ct.ConvertToChessCoords(pos)
                    boardx = squareClicked[0]
                    boardy = squareClicked[1]
                    print(pos)
                    if winner != 0:
                        if x >= 220 and x <= 506:
                            if y >= 380 and y <= 506:
                                screen = 0
                                resetRules()
                                resetCaptures()
                                board = [["br","bn","bb","bq","bk","bb","bn","br"],["bp","bp","bp","bp","bp","bp","bp","bp"],["e","e","e","e","e","e","e","e"],["e","e","e","e","e","e","e","e"],["e","e","e","e","e","e","e","e"],["e","e","e","e","e","e","e","e"],["wp","wp","wp","wp","wp","wp","wp","wp"],["wr","wn","wb","wq","wk","wb","wn","wr"]]
                                #board = [["e","e","e","e","e","e","e","e"],["e","e","bq","e","wq","e","e","e"],["e","e","e","e","e","wk","e","e"],["e","bq","e","e","e","e","e","e"],["e","e","e","e","e","e","e","e"],["e","e","e","bq","e","e","bq","e"],["e","e","e","e","e","e","e","e"],["e","e","e","e","e","e","e","e"]]
                    if x>=33 and x<=685:
                        if y>=33 and y<=685:
                            if winner == 0:
                                if turn%2 == 0:
                                    if boardHighlights[boardx][boardy] == 1:
                                        moveBlackPiece(pieceLastClicked,squareClicked)
                                        turn += 1
                                        updateRules("black")
                                    else:
                                        pieceLastClicked = squareClicked
                                        highlightMovesBlack(squareClicked)
                                else:
                                    if boardHighlights[boardx][boardy] == 1:
                                        moveWhitePiece(pieceLastClicked,squareClicked)
                                        turn += 1
                                        updateRules("white")
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
     
