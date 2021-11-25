import pygame
from ObjectUtill import pygameUtill

from pygame import Rect, Vector2

class UI:
        

    def UIUpdate(self , events):
         pass
     
    def UIRender(self):
         pass

    

class UIButton (UI):
    
    def __init__ (self , image, imagesize : tuple , pos :Vector2 , BtnExecute,size = 0):
        
        centerX = imagesize[0] * 0.5 
        centerY = imagesize[1] * 0.5 
        
        
        
        self._image = None
        self._rect = Rect(0,0,0,0);
        self._range = 0.0
        self._position = None
    
    
        
        self._rect.top = centerY
        self._rect.height = -centerY
        self._rect.left = -centerX                         
        self._rect.width = centerX
                    
        self._image = image
        
        self._position = pos
        self._range = size
        
        self._currentimage = image[0]
        self._btnExecute = BtnExecute
        self._btnCheck = False
        
                
        
    def UIUpdate(self , events):
        
        _mousePos = pygame.mouse.get_pos()
        mouseinButton = pygameUtill.UIBoxCrush(self._position , _mousePos , self._rect)
        if mouseinButton:
            self._currentimage = self._image[1]
        else:
            self._currentimage = self._image[0]
            
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if mouseinButton:
                    self._btnExecute();
        
        
    def UIRender(self):
        pygameUtill.DrawImage(self._currentimage , self._position ,self._rect)  
        
