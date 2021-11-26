from Bullet import *
from pygame import *
from SkillBase import *
import math as mt

from GameManager import *
from ObjectUtill import *


class ScanSkill (SkillBase):
    
    def __init__ (self , ID, skillCoolTime , continueTime, treatment , CallBack ):        
        
        self._id = ID         
        self._skillCoolTime = skillCoolTime * 1000.0
        self.currentTime = 0.0
        self._countinueTime = continueTime
        self._treatment = treatment
        self._callBack = CallBack                
        
    
    def Execute (self , Angle , StartPos):
                  
        self._callBack(self._treatment)
        GameManager.UseScanSkill(self._countinueTime)
            
            
        
        
    
    