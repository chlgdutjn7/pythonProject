import pygame
from ObjectUtill import pygameUtill

from pygame import Rect, Vector2

class UI:
        
    _image = None
    _rect = Rect(0,0,0,0);
    _range = 0.0
    _position = None
    def UIUpdate(self):
         pass
     
    def UIImage(self):
         pass

    

class UIButton (UI):
    
    def __init__ (self , image, imagesize : tuple , pos :Vector2 , size = 0):
        
        centerX = imagesize[0] * 0.5 
        centerY = imagesize[1] * 0.5 
        
        
        self._rect.top = centerY
        self._rect.height = -centerY
        self._rect.left = -centerX                         
        self._rect.width = centerX
                    
        self._image = image
        
        self._position = pos
        self._range = size
        
        self._currentimage = image[0]
        
 

        
        
    def UIUpdate(self):
        
        _mousePos = pygame.mouse.get_pos()
        
        if pygameUtill.UIBoxCrush(self._position , _mousePos , self._rect):
            self._currentimage = self._image[1]
                        
        else:
            self._currentimage = self._image[0]
        
    
    def UIImage(self):
        pygameUtill.DrawImage(self._currentimage , self._position ,self._rect)        
    