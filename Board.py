from Pieces import *
import os

class Board():
    """
    Pawns can be added iteratively as all on same row
    """
    def add_Pawns(self):
        for i in range (8):
            pawn = Pawn(1,i)
            pawn2 = Pawn(6,i)
            self.white.append(pawn)
            self.black.append(pawn2)

    def add_backrow(self, colour = False):
        row_num = 0
        if colour:
            row_num = 7
        
        k1 = Knight(row_num,1)
        k2 = Knight(row_num,6)
        
        r1 = Rook(row_num,0)
        r2 = Rook(row_num,7)
        if colour:
            self.black.append(k1)
            self.black.append(k2)
        
            self.black.append(r1)
            self.black.append(r2)
            return

        self.white.append(k1)
        self.white.append(k2)
        
        self.white.append(r1)
        self.white.append(r2)
        


    def __init__(self):
        self.pieces = []
        self.squares = []
        self.block = [[],[],[],[],[],[],[],[]]
        self.white = []
        self.black = []
        for i  in range (8):
            
            for j in range (8):
                self.block[i].append(' ')
                self.squares.append((i,j))
        self.add_Pawns()
        self.add_backrow()
        self.add_backrow(True)
                
    def display_coords(self):
       
        for i in reversed(self.block):
           
            print(i)
    
    def show_board(self):
        for i in self.squares:
            for p in self.white:
                
                if p.coords == i:
                    self.block[p.coords[0]][p.coords[1]] = p.name
            for k in self.black:
                
                if k.coords == i:
                    self.block[k.coords[0]][k.coords[1]] = k.name
                    
    def move_piece(self, piece_num, move_index):
        self.pieces[piece_num].move(move_index)
    def dump_pieces(self):
        for i in range(len(self.pieces)):
            print('Piece :%s at index %s at position(%s)'% (self.pieces[i].name, i, self.pieces[i].coords))
            
        
    



x = Board()
x.display_coords()
x.show_board()
print('\n New Board \n')
#x.move_piece(17,1)
x.show_board()
x.display_coords()

while 1:
    
    x.dump_pieces()
    selected = input('Which piece to move')
    m = input('Where to move piece')
    x.move_piece(int(selected), int(m))
    x.show_board()
    x.display_coords()
            