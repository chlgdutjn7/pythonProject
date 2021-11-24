from GameSceneBase import SceneBase
import pygame 
from ObjectUtill import pygameUtill
from UI import *
class MainScene (SceneBase): 
    
    def Sceneinit(self):
        _startImage = []
        
        _startImage.append(pygame.image.load(pygameUtill._filePath + "image\\Button\\GameStart1.png"))
        _startImage.append(pygame.image.load(pygameUtill._filePath + "image\\Button\\GameStart2.png"))
               
        self._startbtn = UIButton(_startImage, _startImage[0].get_size() , (400 , 500))
        
        return super().Sceneinit()
    
    def __init__ (self):
        self.Sceneinit()
        
       
        
        
    
    def Update(self):        
        mouse = pygame.mouse.get_pos();       
        print (mouse)
        for event in pygame.event.get():
            pass
        
        self._startbtn.UIImage()
        self._startbtn.UIUpdate()
        
    def Render(self):
        pass
        
    
    
    
        
        
    