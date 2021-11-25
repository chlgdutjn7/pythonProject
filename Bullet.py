from pygame import Vector2, math, transform
from GameManager import * 
from PlayerImage import ChracterImage
from ObjectUtill import *
class Bullet:
    
    
    def __init__ (self ,image, Dir , StartPos , Id , Range , Damage = 5, speed = 1):
        
        self._startPos = Vector2 (StartPos)
        self._dir = Dir
        self._id = Id 
        self._range = Range        
        self._speed = speed
        self._damage = Damage
        self._isDead = False
        
        self._position = Vector2 (StartPos)
        self._size = 10
        self._attackList = []
        Tempimage = transform.scale(image , (self._size , self._size))        
        self._image = ChracterImage(Tempimage , Tempimage.get_size())
        
    
    
    def Update(self):
        self.BulletRange()
        self.BulletMoveMent()
        
        
    def Render (self):
        if self._isDead:
            return;
        pygameUtill.DrawImage(self._image._image , self._position , self._image._rect) 
        
    
    def BulletRange(self):
        dist = Vector2.distance_to(self._startPos , self._position)
        if self._isDead:
            return;
        
        if dist > self._range:
            self._isDead = True
        
        for obj in GameManager._objectList:
            if pygameUtill.CircleCrush(self._position , obj._pos , obj._size *0.5 , self._size * 0.5 ):
                if self._id != obj._image._id:
                    self._isDead = True
                    obj._hp -= self._damage
                    
    
    def BulletMoveMent(self):        
        self._position[0] += self._dir[0] * pygameUtill._clockDT * self._speed;
        self._position[1] += self._dir[1] * pygameUtill._clockDT * self._speed;