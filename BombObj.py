from pygame import Vector2, transform
from Chracter import *
from PlayerImage import ChracterImage
from GameManager import *
from ObjectUtill import *


class Bomb:
    def __init__(self , Image , BoomImage , Pos : Vector2 , Range , Damage):
        
        self._range = Range        
        self._damage = Damage       
        self._pos = Pos 
        self._size = 50
        self._Boomsize = Range
        
        Tempimage = transform.scale(Image , (self._size , self._size))        
        self._image = ChracterImage(Tempimage , Tempimage.get_size()) 
                
        
        TempBoomimage = transform.scale(Image , (self._Boomsize , self._Boomsize)) 
        self._Boomimage = ChracterImage(BoomImage , TempBoomimage.get_size())  
        
        self._hp = 100
        self._isDead = False
        self._isBoom = False
        self._isBoomImage = False
        self._startTime = 0
        self._circleCrush = True
        
        
    def Update(self, event):
        if self._hp <= 0 and self._isBoomImage == False:
            self._isBoom = True
            
        if  self._isBoom == True and self._isBoomImage == False:
            for obj in GameManager._objectList:
                if self._image._id == obj._image._id:
                    continue
            
                if pygameUtill.CircleCrush(obj._pos , self._pos , self._range / 2, obj._size / 2):
                    obj._hp -= self._damage
            self._isBoom = False
            self._isBoomImage = True
            self._startTime = pygame.time.get_ticks()
            self._circleCrush = False
            
    
    
    def Render(self):
        if self._isBoomImage == False:
            pygameUtill.DrawImage(self._image._image , self._pos , self._image._rect)
        else:
            if pygame.time.get_ticks() - self._startTime < 1000.0:
                pygameUtill.DrawImage(self._Boomimage._image , self._pos , self._Boomimage._rect)
            else:
                self._isDead = True
                
            
        
        