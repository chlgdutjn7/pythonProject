from typing import ClassVar


class SceneBase:
    
    _gameExit = False; 
    _sceneChange = False;
    
    def Sceneinit (self):
        print("게임 씬 초기화")
        
    def __init__ (self):
        self.Sceneinit()
    
    def Update(self , events):
        pass
        
    def Render(self):
        pass
    
    def ChangeScene(self):        
        pass
    
    
    def GameExit(self):
        return self._gameExit;
    
    

    
    