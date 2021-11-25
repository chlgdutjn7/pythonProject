import pygame
from GameSceneBase import *
from GameMainScene import MainScene   
from ObjectUtill import pygameUtill



pygameUtill.pygameInit(1920 , 1080)

_currentScene = MainScene()

_gameRoop = True


while _gameRoop:
    
    
    pygameUtill._screen.fill((0,0,0))
    
           
    events = pygame.event.get()    
    for event in events:
        
        if event.type == pygame.QUIT:
            _gameRoop = False
            
    
    _currentScene.Render()
    _currentScene.Update(events)
    if _gameRoop == True:
        _gameRoop = not _currentScene.GameExit()
    
    TempScene = _currentScene.ChangeScene()
    if TempScene != None:
        _currentScene = TempScene

    
    pygameUtill._clock.tick(144)
    pygame.display.update()