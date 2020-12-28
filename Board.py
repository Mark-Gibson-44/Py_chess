from Pieces import *

class Board():

    def add_Pawns(self):
        for i in range (8):
            pawn = Pawn(1,i)
            pawn2 = Pawn(6,i)
            self.pieces.append(pawn)
            self.pieces.append(pawn2)

    def add_backrow(self):
        k1 = Knight(0,1)
        k2 = Knight(0,6)
        k3 = Knight(7,6)
        k4 = Knight(7,1)
        r1 = Rook(0,0)
        r2 = Rook(0,7)
        r3 = Rook(7,0)
        r4 = Rook(7,7)
        self.pieces.append(k1)
        self.pieces.append(k2)
        self.pieces.append(k3)
        self.pieces.append(k4)
        self.pieces.append(r1)
        self.pieces.append(r2)
        self.pieces.append(r3)
        self.pieces.append(r4)


    def __init__(self):
        self.pieces = []
        self.squares = []
        self.block = [[],[],[],[],[],[],[],[]]
        for i  in range (8):
            
            for j in range (8):
                self.block[i].append(' ')
                self.squares.append((i,j))
        self.add_Pawns()
        self.add_backrow()
                
    def display_coords(self):
        
        for i in reversed(self.block):
           
            print(i)
    
    def show_board(self):
        for i in self.squares:
            for p in self.pieces:
                
                if p.coords == i:
                    self.block[p.coords[0]][p.coords[1]] = p.name
                    
    def move_piece(self, piece_num, move_index):
        self.pieces[piece_num].move(move_index)
        
    



x = Board()
x.display_coords()
x.show_board()
print('\n New Board \n')
x.move_piece(17,1)
x.show_board()
x.display_coords()
            