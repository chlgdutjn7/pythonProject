
class SceneBase:
    
    def Sceneinit (self):
        print("게임 씬 초기화")
        
    def __init__ (self):
        self.Sceneinit()
    
    def Update(self):
        pass
        
    def Render(self):
        pass
    
    def ChangeScene(self , ChangeScene):
        ChangeScene.init()
        return ChangeScene
    
    