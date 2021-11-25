from GameSceneBase import SceneBase
from ObjectUtill import *
from Chracter import *

class InGameScene (SceneBase):
    
    def __init__(self):
        player1Image = pygame.image.load(pygameUtill._filePath +  "image/SelectChracter/chracterBtn 1-1.png")
        
        self._player1 = Chracter(player1Image , 0 , [100 , 100] , 1)
        self._player2 = Chracter(player1Image , 1 , [200 , 200] , 1)
        
        
        

    def Update(self , events):
        self._player1.PlayerUpdate(events)
        self._player2.PlayerUpdate(events)
        
                
    def Render(self):
        self._player1.PlayerRender()
        self._player2.PlayerRender()
    
    def ChangeScene (self):        
        if self._sceneChange:
            return None
        else:
            return None
    
    