from Bullet import *
from pygame import *
from SkillBase import *
import math as mt

from GameManager import *
from ObjectUtill import *
from mineObj import mine



class MineSkill (SkillBase):
    
    def __init__ (self , ID, skillCoolTime   , Range ,  _Damage = 5):        
        
        self._id = ID 
        self._range = Range        
        self._damage = _Damage        
        self._skillCoolTime = skillCoolTime * 1000.0
        self.currentTime = 0.0
        self.image = pygame.image.load(pygameUtill._filePath +  "image/Bullet/mine.png")
        self.Boomimage = pygame.image.load(pygameUtill._filePath +  "image/Bullet/boom.png")
        
        
        
    
    def Execute (self , Angle , StartPos):
                
        if (self._skillCoolTime < (pygame.time.get_ticks() - self.currentTime)):                        
            
            GameManager.mineAdd(mine(self.image , self.Boomimage , self._id , Vector2(StartPos) , self._range , self._damage))            
            self.currentTime = pygame.time.get_ticks()
            
        
        
    
    