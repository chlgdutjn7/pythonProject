from ObjectUtill import *
from GameSelectManager import *
import pygame

class Chracter:
    
    def __init__(self , playerNumber , Pos):
        
        if playerNumber == 0:
            self._playerName = SelectManager._player1Name
            self._Player = SelectManager._player1            
            
        if playerNumber == 1:
            self._playerName = SelectManager._player2Name
            self._Player = SelectManager._player2
            
        self._playerPos = Pos
            
    def PlayerMoveMent(self , events):
        
        self._dirX = 0.0
        self._dirY = 0.0
    
        if self._playerName == SelectManager._player1Name:
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP1:
                        pass
                    if event.key == pygame.K_KP2:
                        pass
                    if event.key == pygame.K_KP3:
                        pass
                    if event.key == pygame.K_KP5:
                        pass
                        
                if event.type == pygame.KEYUP:
                    print ("읽힘")
                
            
        if self._playerName == SelectManager._player2Name:
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        pass
                    if event.key == pygame.K_s:
                        pass
                    if event.key == pygame.K_d:
                        pass
                    if event.key == pygame.K_w:
                        pass
                        
                if event.type == pygame.KEYUP:
                    print ("읽힘")
                
            