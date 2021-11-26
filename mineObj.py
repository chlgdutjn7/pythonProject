from pygame import Vector2, transform
import pygame
from Chracter import *
from GameManager import GameManager
from ObjectUtill import pygameUtill
from PlayerImage import ChracterImage

class mine:
    def __init__(self , Image ,BoomImage , Id, Pos : Vector2 , Range , Damage):
            
        self._range = Range        
        self._damage = Damage       
        self._pos = Pos 
        self._size = 50
        self._Id = Id
        self._Boomsize = Range
        
        
        
        Tempimage = transform.scale(Image , (self._size , self._size))        
        self._image = ChracterImage(Tempimage , Tempimage.get_size()) 
        
        TempBoomimage = transform.scale(Image , (self._Boomsize , self._Boomsize)) 
        self._Boomimage = ChracterImage(BoomImage , TempBoomimage.get_size())   
        
        self._hp = 1        
        
        self._isDead = False
        self._isBoom = False
        self._isBoomImage = False
        self._startTime = 0                
        
                
    def Update(self,event):
        if self._hp <= 0 and self._isBoomImage == False:
            self._isBoom = True        
            
        if self._isBoomImage == False:
            for obj in GameManager._BulletList:
                if GameManager._isScanSkill:    
                    if pygameUtill.CircleCrush(obj._position , self._pos , self._size / 2, obj._size / 2):
                        self._isBoom = True
            
            
            
        for obj in GameManager._objectList:
            if (obj._image._id == self._Id):
                continue
            
            if pygameUtill.CircleCrush(obj._pos , self._pos , self._size / 2, obj._size / 2):
                self._isBoom = True  
        
        
        
        
        if  self._isBoom == True and self._isBoomImage == False:
            for obj in GameManager._objectList:
                            
                if pygameUtill.CircleCrush(obj._pos , self._pos , self._range / 2, obj._size / 2):
                    obj._hp -= self._damage
                
            self._isBoom = False
            self._isBoomImage = True
            self._startTime = pygame.time.get_ticks()
            self._circleCrush = False 
            
            
              
    def Render(self):
        if self._isBoomImage == False:
            if GameManager._isScanSkill:
                pygameUtill.DrawImage(self._image._image , self._pos , self._image._rect)
                
        else:
            if pygame.time.get_ticks() - self._startTime < 1000.0:
                pygameUtill.DrawImage(self._Boomimage._image , self._pos , self._Boomimage._rect)
            else:
                self._isDead = True
        
        

        