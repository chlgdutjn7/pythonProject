import pygame
from ObjectUtill import *
from PlayerImage import ChracterImage 
from GameManager import *
from pygame import math
import math as mt

from NormalSkill import NormalSkill


class Object:
            
    def Update(event):
        pass
    
    def Render():
        pass



class Chracter (Object):
    
    def __init__(self , Image ,playerNumber , Pos : Vector2 , speed ):
        
        self._circleCrush = True;  
        
        if playerNumber == 0:
            self._playerName = SelectManager._player1Name
            self._Player = SelectManager._player1            
            
        if playerNumber == 1:
            self._playerName = SelectManager._player2Name
            self._Player = SelectManager._player2
        
          
        self._pos = Pos
        self._speed = speed;
        self._size = 50
        
        self._dirX = 0.0
        self._dirY = 0.0
        
        self.angle = 0
        
        
        Tempimage = transform.scale(Image , (self._size , self._size))        
        self._image = ChracterImage(Tempimage , Tempimage.get_size())     
        
        self._skills = [NormalSkill(self._image._id , 0.5 ,  500)]
        self._hp = 100
        
        
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
                    
                    if event.key == pygame.K_p:
                        self.UseSkill(0)
                                            
                    if event.key == pygame.K_LEFTBRACKET:
                        pass
                    if event.key == pygame.K_RIGHTBRACKET :
                        pass
                        
                        
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
                    if event.key == pygame.K_t:
                        pass                    
                    if event.key == pygame.K_y:
                        pass
                    if event.key == pygame.K_u:
                        pass
                    
                                               
                        
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
        
        if AddX != 0  or AddY != 0:
            self.PlayerAngle(AddX , AddY)
            pass
        
        if pygameUtill.XMapCrush([self._pos[0] + AddX ,self._pos[1]] , self._image._rect) :
                if not self.CrushCheckObj(self._pos[0] + AddX , self._pos[1]):
                    self._pos[0] += AddX
        if pygameUtill.YMapCrush([self._pos[0] ,self._pos[1] + AddY] , self._image._rect) :       
            if not self.CrushCheckObj(self._pos[0] ,self._pos[1] + AddY):     
                self._pos[1] += AddY
                
        
        
    def PlayerAngle(self , addX , addY):
        self.angle = mt.atan2(addY,addX)
        print (self.angle)
        self._image._roateImage = transform.rotate(self._image._image ,mt.degrees(self.angle))
        pass
        
        
    
    def CrushCheckObj (self , PosX, PosY):
        crushCheck = False
        
        for obj in GameManager._objectList:
            if obj._image._id == self._image._id:
                continue
            if self._circleCrush == True and obj._circleCrush == True:
                crushCheck = pygameUtill.CircleCrush(Vector2(PosX, PosY) , obj._pos ,self._size *0.5,  obj._size *0.5)
            else:
                pass
            
            if crushCheck == True:
                break
        
        return crushCheck
        
        
        
    
    def Update(self, event):
        self.PlayerMoveMent(event)
    
    def Render(self):
        pygameUtill.DrawImage(self._image._roateImage, self._pos , self._image._rect)
        
    def UseSkill(self, skillType):
        
        sin = mt.sin(self.angle)
        cos = mt.cos(self.angle)
        
        Dir = Vector2(cos , sin)
        Dir = Dir.normalize();
        self._skills[skillType].Execute(Dir , self._pos)    
        