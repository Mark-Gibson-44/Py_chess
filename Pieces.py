import operator


class Piece():
    """
    Abstract class to be a base class for all pieces
    """
    def __init__(self, x, y, c):
        self.moves = []#List of tuples containing the valid moves the piece can do
        self.attacks = []#List of indexes of moves to indicate which moves are valid attacks
        self.name = '' #character for the piece
        self.coords = (x , y)
        self.colour = c#Should simplify things


   


    """
    Every piece Other than pawns has every move as its attack
    Instead of filling a list with all its moves simply check whether
    the list is empty as no matter what providing its a valid move
    its a valid attack
    Otherwise just  check whether its an attack
    """
    def valid_attack(self,attack):
        if len(self.attacks) == 0:
            return True
        return attack in self.attacks

    """
    Will take in a tuple for the move that is trying to be made
    Returns true if its within the list
    """
    def valid_move(self, move):
        #Some Maths to determine the type of attack by subtracting where the piece is being placed
        #As well as  where the piece was
        actual_move = tuple(map(operator.sub,  self.coords, move))
        actual_move = tuple(map(operator.abs,  actual_move))
        
        print(actual_move)
        return actual_move in self.moves
        
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
        
        assert(self.valid_move(num))
        self.coords = tuple(num)
    
        

        
class Pawn(Piece):

    def __init__(self,x,y, c =False):
        Piece.__init__(self,x,y,c)
        self.moves = [(0,1),(-1,1),(1,1), (0,2)]
        self.attacks = [1,2]
        self.name = 'P'

class Knight(Piece):

    def __init__(self,x,y,c =False):
        Piece.__init__(self,x,y,c)
        self.moves = [(-2,1),(2,1),(-1,2), (1,2), (-2,-1),(-1,-2),(1,-2),(-2,1)]
        self.attacks = []
        self.name = 'K'
    
class Rook(Piece):

    def __init__(self,x,y,c =False):
        Piece.__init__(self,x,y,c)
        self.moves = [(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,-1),(0,-2),(0,-3),(0,-4),(0,-5),(0,-6),(0,-7), (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(-1,0),(-2,0),(-3,0),(-4,0),(-5,0),(-6,0),(-7,0)]
        self.attacks = []
        self.name = 'R'

class King(Piece):

    def __init__(self,x,y,c =False):
        Piece.__init__(self,x,y,c)
        self.moves = [(0,1),(1,0),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]
        self.attacks = []
        self.name = 'G'
    """
    Will need to evaluate if an attack is on the king
    """
    def in_check(self):
        pass
class Queen(Piece):

    def __init__(self,x,y,c =False):
        Piece.__init__(self,x,y,c)
        self.moves = [(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),\
                        (-1,-1),(-2,-2),(-3,-3),(-4,-4),(-5,-5),(-6,-6),(-7,-7),(-8,-8),\
                            (-1,1),(-2,2),(-3,3),(-4,4),(-5,5),(-6,6),(-7,7),(-8,8),\
                                (1,-1),(2,-2),(3,-3),(4,-4),(5,-5),(6,-6),(7,-7),(8,-8),\
                                    (0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,-1),(0,-2),\
                                        (0,-3),(0,-4),(0,-5),(0,-6),(0,-7), (1,0),(2,0),(3,0),\
                                            (4,0),(5,0),(6,0),(7,0),(-1,0),(-2,0),(-3,0),(-4,0),\
                                                (-5,0),(-6,0),(-7,0)]
        self.attacks = []
        self.name = 'Q'
    """
    Will need to evaluate if an attack is on the king
    """
    def in_check(self):
        pass

class Bishop(Piece):

    def __init__(self,x,y,c =False):
        Piece.__init__(self,x,y,c)
        self.moves = [(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),\
                        (-1,-1),(-2,-2),(-3,-3),(-4,-4),(-5,-5),(-6,-6),(-7,-7),(-8,-8),\
                            (-1,1),(-2,2),(-3,3),(-4,4),(-5,5),(-6,6),(-7,7),(-8,8),\
                                (1,-1),(2,-2),(3,-3),(4,-4),(5,-5),(6,-6),(7,-7),(8,-8)]
        self.attacks = []
        self.name = 'B'


    



