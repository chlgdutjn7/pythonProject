from GameSceneBase import SceneBase
import pygame 
from ObjectUtill import pygameUtill
from UI import *

class MainScene (SceneBase): 
    
    def Sceneinit(self):
        _startImage = []
        _ExitImage = []
        
        
        
        _startImage.append(pygame.image.load(pygameUtill._filePath + "image/Button/GameStart1.png"))
        _startImage.append(pygame.image.load(pygameUtill._filePath + "image/Button/GameStart2.png"))
        
        
        _ExitImage.append(pygame.image.load(pygameUtill._filePath + "image/Button/Exit1.png"))
        _ExitImage.append(pygame.image.load(pygameUtill._filePath + "image/Button/Exit2.png"))
               
        self._startBtn = UIButton(_startImage, _startImage[0].get_size() , (400 , 500) , self.GameStartBtn)
        self._endBtn = UIButton(_ExitImage, _ExitImage[0].get_size() , (400 , 700) , self.ExitBtn)
        
        
        return super().Sceneinit()
    
    def __init__ (self):
        self.Sceneinit()
        
       
        
        
    
    def Update(self):     
        self._startBtn.UIUpdate()
        self._endBtn.UIUpdate()
           

        
        
    def Render(self):
        self._startBtn.UIRender()
        self._endBtn.UIRender()
        
    

        
        
    def GameStartBtn(self):
        print ("게임 시작 실행") 
    
    def ExitBtn(self):
        print ("게임에서 나감") 
    
    
    
        
        
    