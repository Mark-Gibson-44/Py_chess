import operator


class Piece():
    """
    Abstract class to be a base class for all pieces
    """
    def __init__(self, x, y):
        self.moves = []#List of tuples containing the valid moves the piece can do
        self.attacks = []#List of indexes of moves to indicate which moves are valid attacks
        self.name = '' #character for the piece
        self.coords = (x , y)
        

    def valid_move(self, move):
        if(move in self.attacks):
            return True
        return False
    def print_moves(self):
        for move in self.moves:
            print(move)
    
    def dump_coords(self):
        print(self.coords)
    
    def move(self, num):
        print(self.coords)
        self.coords = tuple(map(operator.add,  self.coords, self.moves[num]))
        

        
class Pawn(Piece):

    def __init__(self,x,y):
        Piece.__init__(self,x,y)
        self.moves = [(1,0),(1,-1),(1,1)]
        self.attacks = [1,2]
        self.name = 'P'

class Knight(Piece):

    def __init__(self,x,y):
        Piece.__init__(self,x,y)
        self.moves = [(-2,1),(2,1),(-1,2), (1,2), (-2,-1),(-1,-2),(1,-2),(-2,1)]
        self.attacks = []
        self.name = 'K'
    
class Rook(Piece):

    def __init__(self,x,y):
        Piece.__init__(self,x,y)
        self.moves = [(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,-1),(0,-2),(0,-3),(0,-4),(0,-5),(0,-6),(0,-7), (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(-1,0),(-2,0),(-3,0),(-4,0),(-5,0),(-6,0),(-7,0)]
        self.attacks = []
        self.name = 'R'

class King(Piece):

    def __init__(self,x,y):
        Piece.__init__(self,x,y)
        self.moves = [(0,1),(1,0),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]
        self.attacks = []
        self.name = 'R'
    



