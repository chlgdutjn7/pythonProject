import pygame
from ObjectUtill import pygameUtill

class SelectManager:
    
    _player1 = None
    _player2 = None
    
    @classmethod
    def SelectPlayer1(cls , Player1):
        cls._player1 = Player1;
        cls._player1Name = "player1"
    @classmethod        
    def SelectPlayer2(cls , Player2):
        cls._player2 = Player2;
        cls._player2Name = "player2"
        
    @classmethod
    def Clear(cls):
        cls._player1 = None
        cls._player2 = None 


class GameManager:
    
    _objectList = []
    _BulletList = []
    _mineList = []
    _WinnerName = ""
    _isScanSkill = False
    _currentTime = 0.0
    
    _IDNumber = 0

    @classmethod
    def ObjectAdd (cls , obj):
        cls._objectList.append(obj)
        
    @classmethod
    def mineAdd (cls , obj):
        cls._mineList.append(obj)
        
        
    @classmethod        
    def BulletAdd (cls , obj):
        cls._BulletList.append(obj)
        
    @classmethod    
    def GetNumber(cls):
        cls._IDNumber += 1
        return cls._IDNumber
    
    @classmethod
    def UseScanSkill(cls, Time):
        cls._isScanSkill = True
        cls._currentTime = pygame.time.get_ticks()
        cls.time = Time
        
        
    @classmethod
    def ScanSkillUpdate(cls):  
        if cls._isScanSkill == True:
            if (pygame.time.get_ticks() - cls._currentTime) > cls.time * 1000:
                cls._isScanSkill = False
    
    @classmethod
    def BulletUpdate(cls):
        DestroyList = []
        for bullet in cls._BulletList:
            bullet.Update()
            if bullet._isDead:
                DestroyList.append(bullet)
        
        for DestroyValue in DestroyList:
            cls._BulletList.remove(DestroyValue)
            
    @classmethod
    def ObjUpdate(cls , events):
        DestroyList = []
        for obj in cls._objectList:
            obj.Update(events)
            if obj._isDead:
                DestroyList.append(obj)
        
        for DestroyValue in DestroyList:
            cls._objectList.remove(DestroyValue)
            
    @classmethod
    def mineUpdate(cls , events):
        DestroyList = []
        for obj in cls._mineList:
            obj.Update(events)
            if obj._isDead:
                DestroyList.append(obj)
        
        for DestroyValue in DestroyList:
            cls._mineList.remove(DestroyValue)
            
    @classmethod
    def BulletRender(cls):        
        for bullet in cls._BulletList:
            bullet.Render()
            
    @classmethod
    def ObjRender(cls):        
        for obj in cls._objectList:
            obj.Render()       
        
    @classmethod
    def mineRender(cls):        
        for obj in cls._mineList:
            obj.Render()
    
    

    @classmethod    
    def ClearValue(cls):
        cls._objectList.clear() 
        cls._BulletList.clear()
        cls._mineList.clear()
        cls._WinPlayerName = None
        
    
        
    

        
    
    
    
    