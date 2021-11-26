import pygame
from GameSceneBase import *
from GameMainScene import MainScene   
from ObjectUtill import pygameUtill



pygameUtill.pygameInit(1920 , 1080)

_currentScene = MainScene()

_gameLoop = True


while _gameLoop:
    
    
    pygameUtill._screen.fill((0,0,0))
    
           
    events = pygame.event.get()    
    for event in events:
        
        if event.type == pygame.QUIT:
            _gameLoop = False
            
    
    _currentScene.Update(events)
    _currentScene.Render()    
    if _gameLoop == True:
        _gameLoop = not _currentScene.GameExit()
    
    TempScene = _currentScene.ChangeScene()
    if TempScene != None:
        _currentScene = TempScene

    
    pygameUtill.ClockTick(144)
    pygame.display.update()