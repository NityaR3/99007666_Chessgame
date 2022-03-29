class Game:
    def __init__(self):
     self.gameboard = {}
        self.Pieces()
        print("chess program. enter moves in algebraic notation separated by space")
        self.main()
         def Pieces(self):

    for i in range(0,8):
            self.gameboard[(i,1)] = Pawn(WHITE,uniDict[WHITE][Pawn],1)
            self.gameboard[(i,6)] = Pawn(BLACK,uniDict[BLACK][Pawn],-1)
            
        placers = [Rook,Knight,Bishop,Queen,King,Bishop,Knight,Rook]
        
    for i in range(0,8):
            self.gameboard[(i,0)] 
            self.gameboard[((7-i),7)] 
           reverse() 
 " # board should be defined"         
 def main(self):
 def Check(self):
 " # check mate should be defined"
 def playerinput(self): 
   a,b = input().split()
 def Board(self):
        print("  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |")
        for i in range(0,8)
        
class Piece:
  
    def isValid(self,startposition,endposition):    
    def availableMoves(self,x,y,gameboard):
        print("ERROR: no movement ") 
    def isInBounds(self,x,y):
        "checks if a position is on the board"
        if x >= 0 and x < 8 and y >= 0 and y < 8:

class Knight(Piece):
    def availableMoves(self,x,y,gameboard, Color = None):
      
        
class Rook(Piece):
    def availableMoves(self,x,y,gameboard ,Color = None):
       
        
class Bishop(Piece):
    def availableMoves(self,x,y,gameboard, Color = None):
    
        
class Queen(Piece):
    def availableMoves(self,x,y,gameboard, Color = None):
  
class King(Piece):
    def availableMoves(self,x,y,gameboard, Color = None):
       
class Pawn(Piece):
    def __init__(self,color,name,direction):
        
            