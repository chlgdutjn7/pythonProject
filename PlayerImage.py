from pygame import Rect, Vector2

class ChracterImage:
    
    def __init__(self , Image , ImageSize):
        
        centerX = ImageSize[0] * 0.5 
        centerY = ImageSize[1] * 0.5 
        
        self._image = None
        self._rect = Rect(0,0,0,0);
        self._range = 0.0
        self._position = None
        
        self._rect.top = centerY
        self._rect.height = -centerY
        self._rect.left = -centerX                         
        self._rect.width = centerX
        
        self._image = Image
        
    