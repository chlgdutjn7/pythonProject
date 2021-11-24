import pygame
from GameSceneBase import *
from GameMainScene import MainScene   
from ObjectUtill import pygameUtill



pygameUtill.pygameInit(1920 , 1080)

_currentScene = SceneBase()
_mainScene = MainScene()

_currentScene = _mainScene;
_gameRoop = True


while _gameRoop:
           
      
    for event in pygame.event.get():
               
        if event.type == pygame.QUIT:
            _gameRoop = False
            
    
    _currentScene.Render()
    _currentScene.Update()
                
    pygameUtill._clock.tick(144)
    pygame.display.update()