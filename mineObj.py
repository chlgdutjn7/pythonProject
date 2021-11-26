from pygame import Vector2, transform
from Chracter import object
from PlayerImage import ChracterImage

class mine:
    def __init__(self , Image , Id, Pos : Vector2 , Range , Damage):
            
        self._range = Range        
        self._damage = Damage       
        self._pos = Pos 
        self._size = 50
        
        Tempimage = transform.scale(Image , (self._size , self._size))        
        self._image = ChracterImage(Tempimage , Tempimage.get_size())  
        
        self._hp = 1
        self._isDead = False
        self._Id = Id
        
        
                
    def Update(event):
        pass
    
    def Render():
        pass
        
        

        