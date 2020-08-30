import pygame
import math
import os
import random
from pygame.locals import *

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

def convertPieceNumberToName(number):
    if number==0:
        return "Pawn"
    elif number == 1:
        return "Rook"
    elif number == 2:
        return "Knight"
    elif number == 3:
        return "Bishop"
    elif number == 4:
        return "Queen"
    elif number == 5:
        return "King"

def convertPieceNameToNumber(pieceString):
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
