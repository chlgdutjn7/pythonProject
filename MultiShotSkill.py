from Bullet import *
from pygame import *
from SkillBase import *

from GameManager import *
from ObjectUtill import *
import asyncio
import math as mt


class MultiShotSkill (SkillBase):
    
    def __init__ (self , ID, skillCoolTime , Count , Angle, Range ,  _Damage = 5, spped = 1):        
        
        self._id = ID 
        self._range = Range        
        self._speed = spped
        self._damage = _Damage        
        self._skillCoolTime = skillCoolTime * 1000.0
        self.currentTime = 0.0
        self.image = pygame.image.load(pygameUtill._filePath +  "image/Bullet/Bullet.png")
        self._count = Count
        self._ShotAngle = Angle        
        self._isShot = False
        
        
    
    def Execute (self , Angle , StartPos):
                
        if (self._skillCoolTime < (pygame.time.get_ticks() - self.currentTime)):
            halfAngle = self._ShotAngle / 2
            shotangle = self._ShotAngle / self._count
            startshotAngle = -halfAngle
            for num in range(0,self._count):
                
                
                sin = mt.sin(mt.radians(startshotAngle) + Angle)
                cos = mt.cos(mt.radians(startshotAngle) + Angle)
                Dir = Vector2(cos , sin)
                Dir = Dir.normalize();
                startshotAngle += shotangle
                
                
                GameManager.BulletAdd(Bullet(self.image , Dir , StartPos, self._id , self._range , self._damage , self._speed))
                
                
            self.currentTime = pygame.time.get_ticks()
            
        
        
    
    