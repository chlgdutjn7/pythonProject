from GameSceneBase import SceneBase
from ObjectUtill import *
from Chracter import *
from GameManager import * 

class InGameScene (SceneBase):
    
    def __init__(self):
        player1Image = pygame.image.load(pygameUtill._filePath +  "image/SelectChracter/chracterBtn 1-1.png")
        
        self._player1 = Chracter(player1Image , 0 , Vector2 (100 , 100) , 1)
        self._player2 = Chracter(player1Image , 1 , Vector2 (200 , 200) , 1)
        
        GameManager.ObjectAdd(self._player1)
        GameManager.ObjectAdd(self._player2)               
        

    def Update(self , events):
        self._player1.Update(events)
        self._player2.Update(events)
        GameManager.BulletUpdate()
                
    def Render(self):
        self._player1.Render()
        self._player2.Render()
        GameManager.BulletRender()
    
    
    def ChangeScene (self):        
        if self._sceneChange:
            GameManager._objectList.clear()
            return None
        else:
            return None
    
    