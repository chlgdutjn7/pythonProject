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


class GameManager:
    
    _objectList = []
    _BulletList = []
    _IDNumber = 0
    @classmethod
    def ObjectAdd (cls , obj):
        cls._objectList.append(obj)
        
    @classmethod        
    def BulletAdd (cls , obj):
        cls._BulletList.append(obj)
        
    @classmethod    
    def GetNumber(cls):
        cls._IDNumber += 1
        return cls._IDNumber
    
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
    def BulletRender(cls):        
        for bullet in cls._BulletList:
            bullet.Render()
        
        
    
    
    
    