from BombObj import Bomb
from GameSceneBase import SceneBase
from ObjectUtill import *
from Chracter import *
from GameManager import * 

class InGameScene (SceneBase):
    
    def __init__(self):
        player1Image = pygame.image.load(pygameUtill._filePath +  "image/SelectChracter/chracterBtn 1-1.png")
        BombImage = pygame.image.load(pygameUtill._filePath +  "/Image/Bullet/bomb.png")
        BoomImage = pygame.image.load(pygameUtill._filePath +  "/Image/Bullet/boom.png")
        
        self._player1 = Chracter(player1Image , 0 , Vector2 (100 , 100) , 1)
        self._player2 = Chracter(player1Image , 1 , Vector2 (200 , 200) , 1)
        
        
        self._Boom = Bomb(BombImage , BoomImage , Vector2 (500 , 500) , 100 , 10)
        
        
        
        GameManager.ObjectAdd(self._player1)
        GameManager.ObjectAdd(self._player2)
        GameManager.ObjectAdd(self._Boom)
             
        

    def Update(self , events):
        
        for obj in GameManager._objectList:
            obj.Update(events)
        GameManager.BulletUpdate()
        GameManager.ObjUpdate(events)
                
    def Render(self):
        GameManager.ObjRender()
        GameManager.BulletRender()
    
    
    def ChangeScene (self):        
        if self._sceneChange:
            GameManager._objectList.clear()
            return None
        else:
            return None
    
    