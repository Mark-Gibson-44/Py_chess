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
        
    """
    Will take in a tuple for the move that is trying to be made
    Returns true if its within the list
    """
    def valid_move(self, move):
        return move in self.moves
        
    """
    Logging
    """
    def print_moves(self):
        for move in self.moves:
            print(move)
    """
    More Logging
    """
    def dump_coords(self):
        print(self.coords)
    
    """
    Currently mainly for console version
    """
    def move(self, num):
        
        
        self.coords = tuple(map(operator.add,  self.coords, self.moves[num]))
        
    def gui_move(self, num):
        
        
        self.coords = tuple(num)
    
        

        
class Pawn(Piece):

    def __init__(self,x,y):
        Piece.__init__(self,x,y)
        self.moves = [(0,1),(-1,1),(1,1), (2,0)]
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
    """
    Will need to evaluate if an attack is on the king
    """
    def in_check(self):
        pass


    



