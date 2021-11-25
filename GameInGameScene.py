from GameSceneBase import SceneBase
from ObjectUtill import *
from Chracter import *

class InGameScene (SceneBase):
    
    def __init__(self):
        self._player1 = Chracter(0 , (30 , 30))

    def Update(self , events):
        self._player1.PlayerMoveMent(events)
        
                
    def Render(self):
        pass
    
    def ChangeScene (self):        
        if self._sceneChange:
            return None
        else:
            return None
    
    