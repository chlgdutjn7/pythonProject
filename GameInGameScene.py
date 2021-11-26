from BombObj import Bomb
from GameSceneBase import SceneBase
from ObjectUtill import *
from Chracter import *
from GameManager import * 
from EndingScene import * 


class InGameScene (SceneBase):
    
    def __init__(self):      
        
        
        self._Booms = []
        
        player1Image = pygame.image.load(pygameUtill._filePath +  "image/Player/Player1.png")
        player2Image = pygame.image.load(pygameUtill._filePath +  "image/Player/Player2.png")
        
        BombImage = pygame.image.load(pygameUtill._filePath +  "/Image/Bullet/bomb.png")
        BoomImage = pygame.image.load(pygameUtill._filePath +  "/Image/Bullet/boom.png")
        
        self._player1 = Chracter(player1Image , 0 , Vector2 (100 , 100) , 0.3)
        self._player2 = Chracter(player2Image , 1 , Vector2 (200 , 200) , 0.3)
        
        
        
        self._Booms.append(Bomb(BombImage , BoomImage , Vector2 (500 , 500) , 100 , 10))
        
        
               
        self.PlayerList = [self._player1 , self._player2]
        self.WinnerPlayerName = None
        
        GameManager.ObjectAdd(self._player1)
        GameManager.ObjectAdd(self._player2)
        
        for boom in self._Booms:
            GameManager.ObjectAdd(boom)
             
        

    def Update(self , events):
        
        for obj in GameManager._objectList:
            obj.Update(events)
        GameManager.BulletUpdate()
        GameManager.ObjUpdate(events)
        GameManager.mineUpdate(events)
        GameManager.ScanSkillUpdate()
        self.isPlayerDead()
        self.WinnerPlayer()
        
                
    def Render(self):
        GameManager.ObjRender()
        GameManager.BulletRender()
        GameManager.mineRender()
    
    def isPlayerDead(self):
        DestroyList = []
        for player in self.PlayerList:
            
            if (player._isDead == True):
                DestroyList.append(player)

        for Destroy in DestroyList:
            self.PlayerList.remove(Destroy)
            
            
    def WinnerPlayer(self):
        if len(self.PlayerList) == 1:
            self.WinnerPlayerName = self.PlayerList[0]._playerName
            self._sceneChange = True
            pass




    def ChangeScene (self):        
        if self._sceneChange:
            GameManager.ClearValue()        
            GameManager._WinnerName = self.WinnerPlayerName
            return EndScene()
        else:
            return None
    
    