import pygame
import os
from pygame import transform
from pygame import math
from pygame import Vector2
from pygame import Rect

class pygameUtill:
    
    _instance = None
    _filePath = os.getcwd() + "/Resource/"


#pygame 초기화
    @classmethod
    def pygameInit (cls , width , height):
        
        pygame.init()
        cls._size = [width , height]
        cls._gameTitle = "GameProject"
        cls._clock = pygame.time.Clock()
        cls._clockDT = 0;
        cls._screen = pygame.display.set_mode(cls._size)
        cls._width = width
        cls._height = height
        pygame.display.set_caption(cls._gameTitle);
        
        
    #원형 충돌
    @classmethod
    def CircleCrush(cls , vec1  : Vector2, vec2  : Vector2, size1, size2):
        dist = Vector2.distance_to (vec1 , vec2)
        if dist < size1 + size2:
            return True
        return False
    
    #UI원형 충돌
    @classmethod
    def UICircleCrush(cls , vec1  : Vector2, vec2  : Vector2, Size):
        dist = Vector2.distance_to(vec1, vec2)
        if dist < Size:
            return True
        return False
    
    
    #박스 충돌
    @classmethod
    def BoxCrush(cls , vec1 : Vector2, vec2 : Vector2 ,  Rect1 : Rect, Rect2: Rect):
        if not (vec1[1] + Rect1.top > vec2[1] + Rect2.height and
                vec1[1] + Rect1.height < vec2[1] + Rect2.top):
            return False
        
        if not(vec1[0] + Rect1.width > vec2[0] + Rect2.left and 
               vec1[0] + Rect1.left < vec2[0] + Rect2.width):
            return False
        
        return True
    
    
    #맵 충돌 
    @classmethod
    def XMapCrush(cls , vec1 : Vector2, Rect: Rect):               
        if (vec1[0] + Rect.width < cls._width  and 
               vec1[0] + Rect.left > 0):
            return True        
        return False
    
    @classmethod    
    def YMapCrush(cls , vec1 : Vector2, Rect: Rect):
        if (vec1[1] + Rect.top < cls._height and vec1[1] + Rect.height > 0):
              return True
        return False
    
        
    
    
    
    @classmethod
    def UIBoxCrush (cls , vec1 : Vector2,  vec2 : Vector2 , rect : Rect):
        if not (vec1[1] + rect.top > vec2[1] and vec1[1] + rect.height < vec2[1]):
            return False
        
        if not(vec1[0] + rect.width > vec2[0] and vec1[0] + rect.left < vec2[0]):
            return False
        
        return True      
    
    
        
    #이미지 중간부터 그리기(피봇이 다름)
    @classmethod
    def DrawImage(cls , img , pos : Vector2, rect : Rect):
        
        tempRact =  Rect(
            rect.left + pos[0] , 
             pos[1] - rect.top,                                                          
            rect.width + pos[0],
            pos[1] - rect.height
            )       
        
        cls._screen.blit(img , tempRact)
        
        
    #이미지 좌측상단부터 그리기 (피봇이 다름)
    @classmethod
    def DrawImageNormal(cls , img , pos : Vector2):
        cls._screen.blit(img , pos)        
        
    
    @classmethod
    def GetFont (cls, FontType , FontSize , Bold = False, italic = False):
        return pygame.font.SysFont(FontType , FontSize, Bold ,italic )
    
    @classmethod
    def FontRender (cls, Font ,Text , Pos ,  antialias = True, Color = (255,255,255)):
        text = Font.render(Text , antialias , Color)
        cls._screen.blit(text, Pos)
        
    @classmethod
    def ClockTick(cls , Data):
        cls._clockDT = cls._clock.tick(Data)
    