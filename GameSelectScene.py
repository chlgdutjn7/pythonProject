from GameSceneBase import SceneBase
from GameInGameScene import InGameScene
from ObjectUtill import *
from GameSelectManager import * 
from UI import UIButton

class SelectScene (SceneBase):
    
    def Sceneinit(self):
        
        _chracterFirstImage = []
        _chracterSceondImage = []
        _gameStartImage = []
        
        self._btnUIList = []
                
        _chracterFirstImage.append(pygame.image.load(pygameUtill._filePath +  "image/SelectChracter/chracterBtn 1-1.png"))
        _chracterFirstImage.append(pygame.image.load(pygameUtill._filePath +  "image/SelectChracter/chracterBtn 1-2.png"))
        
        
        _chracterSceondImage.append(pygame.image.load(pygameUtill._filePath + "image/SelectChracter/chracterBtn 2-1.png"))
        _chracterSceondImage.append(pygame.image.load(pygameUtill._filePath + "image/SelectChracter/chracterBtn 2-2.png"))
        
        _gameStartImage.append(pygame.image.load(pygameUtill._filePath + "image/SelectChracter/GameStartBtn 1.png"))
        _gameStartImage.append(pygame.image.load(pygameUtill._filePath + "image/SelectChracter/GameStartBtn 2.png"))
        
        
        self._chracterCheckBoxImage = pygame.image.load(pygameUtill._filePath + "image/SelectChracter/CheckBox.png")
        self._chracterCheckImage= pygame.image.load(pygameUtill._filePath + "image/SelectChracter/Check.png")
        
        
        _firstCracter = UIButton(_chracterFirstImage , _chracterFirstImage[0].get_size() , (400 , 400) , self.GameStartSceneChracter1)
        _sceondCracter = UIButton(_chracterSceondImage , _chracterSceondImage[0].get_size() , (900 , 400) , self.GameStartSceneChracter2)
        _startBtn = UIButton(_gameStartImage , _gameStartImage[0].get_size() , (1500 , 970) , self.GameStartBtn)
        
        self._btnUIList.append(_firstCracter)
        self._btnUIList.append(_sceondCracter)
        self._btnUIList.append(_startBtn)
        
        
        self._font = pygameUtill.GetFont("arial" , 30)
        self._playerChoice = True

    
    
    
    def __init__(self):
        self.Sceneinit();
    
    def Update(self , events):
        
        for btnUI in self._btnUIList:
            btnUI.UIUpdate(events)
        
        
    def Render(self):
        for btnUI in self._btnUIList:
            btnUI.UIRender()
        pygameUtill.FontRender(self._font , "Player1 : " , (400 , 900) )
        pygameUtill.FontRender(self._font , "Player2 : " , (900 , 900) )
            
        self.OkayerChoiseCheckBoxRender()
    
    
    def ChangeScene(self):       
        if self._sceneChange: 
            return InGameScene();
        return None
    
    def GameStartSceneChracter1(self):
        if self._playerChoice:
            SelectManager.SelectPlayer1(0)
        else:
            SelectManager.SelectPlayer2(0)
            
        self._playerChoice = not self._playerChoice;
        
    def GameStartSceneChracter2(self):
        if self._playerChoice:
            SelectManager.SelectPlayer1(1)
        else:
            SelectManager.SelectPlayer2(1)
            
        self._playerChoice = not self._playerChoice;
        
    def GameStartBtn(self):
        if SelectManager._player1 == None:            
            return
        if SelectManager._player2 == None:            
            return
        
        self._sceneChange = True;
            
    
    def OkayerChoiseCheckBoxRender(self):
        

        
        pygameUtill.DrawImageNormal(self._chracterCheckBoxImage , (1100 , 900))    
        pygameUtill.DrawImageNormal(self._chracterCheckBoxImage  , (600 , 900))
                        
        if SelectManager._player1 != None:                      
            pygameUtill.DrawImageNormal(self._chracterCheckImage  , (600 , 900))              
            
        if SelectManager._player2 != None:
            pygameUtill.DrawImageNormal(self._chracterCheckImage  ,  (1100 , 900))
            
            
            
            
            
        
