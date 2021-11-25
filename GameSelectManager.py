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
        
        
    
    