from asyncio.tasks import sleep
from Bullet import *
from pygame import *
from SkillBase import *

from GameManager import *
from ObjectUtill import *
import random
import threading
import math as mt
import time as normaltime



class RandomShotSkill (SkillBase):
    
    def __init__ (self , ID, skillCoolTime , Count ,ShotDelay, Angle, Range ,  _Damage = 5, spped = 1):        
        
        self._id = ID 
        self._range = Range        
        self._speed = spped
        self._damage = _Damage        
        self._skillCoolTime = skillCoolTime * 1000.0
        self.currentTime = 0.0
        self.image = pygame.image.load(pygameUtill._filePath +  "image/Bullet/Bullet.png")
        self._count = Count
        self._ShotAngle = Angle
        self._shotDelat = ShotDelay 
        
        
    
    def Execute (self , Angle , StartPos):        
        
        mythread = threading.Thread(target = self.RandShot , args = (Angle , StartPos))
        mythread.start()
            
        
    def RandShot(self , Angle , StartPos):
        
            halfAngle = self._ShotAngle / 2
            
            for num in range(0,self._count):
                
                randomAngle = random.randrange(-halfAngle,halfAngle)
                
                sin = mt.sin(mt.radians(randomAngle) + Angle)
                cos = mt.cos(mt.radians(randomAngle) + Angle)
                Dir = Vector2(cos , sin)
                Dir = Dir.normalize();
                
                GameManager.BulletAdd(Bullet(self.image , Dir , StartPos, self._id , self._range , self._damage , self._speed))
                normaltime.sleep(self._shotDelat)
                
                
        
    
    