import pygame
from ObjectUtill import *
from PlayerImage import ChracterImage 
from GameSelectManager import *
from pygame import math


class Chracter:
    
    def __init__(self , Image ,playerNumber , Pos : Vector2 , speed ):
        
        if playerNumber == 0:
            self._playerName = SelectManager._player1Name
            self._Player = SelectManager._player1            
            
        if playerNumber == 1:
            self._playerName = SelectManager._player2Name
            self._Player = SelectManager._player2
            
        self._playerPos = Pos
        self._speed = speed;
        
        self._dirX = 0.0
        self._dirY = 0.0
        
        Tempimage = transform.scale(Image , (50 , 50))        
        self._image = ChracterImage(Tempimage , Tempimage.get_size())     
        
        
    def PlayerMoveKeyCheck(self , events):
        

    
        if self._playerName == SelectManager._player1Name:
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP1:
                        self._dirX = -1.0
                        
                    if event.key == pygame.K_KP2:
                        self._dirY = 1.0
                        
                    if event.key == pygame.K_KP3:
                       self._dirX = 1.0
                        
                    if event.key == pygame.K_KP5:
                        self._dirY = -1.0
                        
                        
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_KP1:
                        self._dirX = 0
                        
                    if event.key == pygame.K_KP2:
                        self._dirY = 0
                        
                    if event.key == pygame.K_KP3:
                        self._dirX = 0
                        
                    if event.key == pygame.K_KP5:
                       self._dirY = 0
                
                
            
        if self._playerName == SelectManager._player2Name:
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self._dirX = -1.0
                    if event.key == pygame.K_s:
                        self._dirY = 1.0
                    if event.key == pygame.K_d:
                        self._dirX = 1.0
                    if event.key == pygame.K_w:
                        self._dirY = -1.0
                                               
                        
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self._dirX = 0.0
                    if event.key == pygame.K_s:
                        self._dirY = 0.0
                    if event.key == pygame.K_d:
                        self._dirX = 0.0
                    if event.key == pygame.K_w:
                        self._dirY = 0.0
      
        if (self._dirX == 0 and self._dirY == 0 ):
            return Vector2(0.0 , 0.0)
            
        return math.Vector2.normalize(Vector2(self._dirX  , self._dirY))
                    
                    
    def PlayerMoveMent(self, event):
        Dir = self.PlayerMoveKeyCheck(event)
        AddX = Dir[0] * pygameUtill._clockDT * self._speed
        AddY = Dir[1] * pygameUtill._clockDT * self._speed
        Map = Rect(0.0 , 0.0 , pygameUtill._width ,   pygameUtill._height)
        if  AddX != 0:
            if pygameUtill.XMapCrush([self._playerPos[0] + AddX ,self._playerPos[1]] , self._image._rect) :            
                self._playerPos[0] += AddX
        if  AddY != 0: 
            if pygameUtill.YMapCrush([self._playerPos[0] ,self._playerPos[1] + AddY] , self._image._rect) :            
                self._playerPos[1] += AddY
              
        
        print (self._playerPos)
        
            
    def PlayerUpdate(self, event):
        self.PlayerMoveMent(event)
    
    def PlayerRender(self):
        pygameUtill.DrawImage(self._image._image, self._playerPos , self._image._rect)