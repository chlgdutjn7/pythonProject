from Bullet import *
from pygame import *
from SkillBase import *

from GameManager import *
from ObjectUtill import *


class NormalSkill (SkillBase):
    
    def __init__ (self , ID, skillCoolTime   , Range ,  _Damage = 5, spped = 1):        
        
        self._id = ID 
        self._range = Range        
        self._speed = spped
        self._damage = _Damage        
        self._skillCoolTime = skillCoolTime * 1000.0
        self.currentTime = 0.0
        self.image = pygame.image.load(pygameUtill._filePath +  "image/Bullet/Bullet.png")
        
        
    
    def Execute (self , Dir , StartPos):
                
        if (self._skillCoolTime < (pygame.time.get_ticks() - self.currentTime)):
            
            GameManager.BulletAdd(Bullet(self.image , Dir , StartPos, self._id , self._range , self._damage , self._speed))
            self.currentTime = pygame.time.get_ticks()
            
        
        
    
    