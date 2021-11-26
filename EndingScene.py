import pygame 
from pygame import Vector2

from GameSceneBase import SceneBase
from ObjectUtill import pygameUtill
from  UI import UIButton
from GameManager import GameManager, SelectManager

class EndScene (SceneBase): 
        
        
    def Sceneinit(self):
        
        _maintBtn = []
        _exitImage = []
        
        
        
        _maintBtn.append(pygame.image.load(pygameUtill._filePath + "image/Button/Main1.png"))
        _maintBtn.append(pygame.image.load(pygameUtill._filePath + "image/Button/Main2.png"))
        
        
        _exitImage.append(pygame.image.load(pygameUtill._filePath + "image/Button/Exit1.png"))
        _exitImage.append(pygame.image.load(pygameUtill._filePath + "image/Button/Exit2.png"))
               
               
        self._maintBtn = UIButton(_maintBtn, _maintBtn[0].get_size() , Vector2(400 , 500) , self.GameStartBtn)
        self._EndBtn = UIButton(_exitImage, _exitImage[0].get_size() , Vector2(400 , 700) , self.ExitBtn)
        
        
        self._font = pygameUtill.GetFont("arial" , 50)
        return super().Sceneinit()
    
    def __init__ (self):        
        self.Sceneinit()        
        
    
    def Update(self , events):     
        self._maintBtn.UIUpdate(events)
        self._EndBtn.UIUpdate(events)        
        
    def Render(self):
        pygameUtill.FontRender(self._font ,  "winner : " + GameManager._WinnerName , (800, 500))
        self._maintBtn.UIRender()
        self._EndBtn.UIRender()
    
        
    def GameStartBtn(self):
        self._sceneChange = True
    
    
    def ExitBtn(self):
        self._gameExit = True
    
    def ChangeScene (self): 
        if self._sceneChange:
            from  GameMainScene import MainScene
            SelectManager.Clear()
            return MainScene()
        else:
            return None
    
    
        
        
    