from Pieces import *
import os

class Board():

    def piece_colour(self, move):
        
        for i in self.white:
            if move == i.coords:
                return True
        for k in self.black:
            if move == k.coords:
                return False

    def take(self, move, col):
        
        if col:
            
            for i in self.black:
                if i.coords == move:
                    #self.behind(i, move)
                    self.black.remove(i)
        for k in self.white:
            if k.coords == move:
                #self.behind(k, move)
                self.white.remove(k)
        return


    """
    Pawns can be added iteratively as all on same row
    """
    def add_Pawns(self):
        for i in range (8):
            pawn = Pawn(i,1, True)
            pawn2 = Pawn(i,6)
            self.white.append(pawn)
            self.black.append(pawn2)

    def add_backrow(self, colour = False):
        row_num = 0
        if colour:
            row_num = 7
        
        k1 = Knight(1,row_num, colour)
        k2 = Knight(6,row_num, colour)
        
        r1 = Rook(0,row_num, colour)
        r2 = Rook(7,row_num, colour)
        b1 = Bishop(2,row_num, colour)
        b2 = Bishop(5,row_num, colour)
        Q = Queen(3,row_num, colour)
        king = King(4,row_num, colour)
        if colour:
            self.black.append(k1)
            self.black.append(k2)
            self.black.append(b1)
            self.black.append(b2)
            self.black.append(r1)
            self.black.append(r2)
            self.black.append(king)
            self.black.append(Q)
            return

        self.white.append(k1)
        self.white.append(k2)
        self.white.append(b1)
        self.white.append(b2)
        self.white.append(r1)
        self.white.append(r2)
        self.white.append(Q)
        self.white.append(king)
        
    """
    Function To make sure that the a piece being taken isn't behind another piece
    """
    def behind(self, piece, move):
        
        
        print(piece.coords)
        print(move)
        start = piece.moves.index(move)
        it = 1
        move_val = sum(move)
        comp = sum(piece[start-it])
        while(comp < move_val):
            if self.piece_at(piece[start-it][0], piece[start-it][1]):
                return True
            it = it + 1
            comp = sum(piece[start-it])
        return False



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
    
    """
    Function used to determine if piece exists in a given position
    """
    def piece_at(self, x, y):
        
        for i in self.white:
            if i.coords == (x,y):
                
                return True, i
        for k in self.black:
            if k.coords == (x,y):
                return True, k
        return False, None
            
                
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

    #boolean Tuple Tuple
    def gui_move_piece(self, colour,  position, move_choice):
        
        
       
        if colour:
            obj = self.white.index(position)
            self.white[obj].gui_move(move_choice)
            self.pieces = self.black + self.white
            return
        obj2 = self.black.index(position)
        self.black[obj2].gui_move(move_choice)
        self.pieces = self.black + self.white
        pass

    def move_piece(self, piece_num, move_index):
        self.pieces[piece_num].move(move_index)
    def dump_pieces(self):
        for i in range(len(self.black)):
            print('Black Piece :%s at index %s at position(%s)'% (self.black[i].name, i, self.black[i].coords))

    

            
        
    



x = Board()
x.display_coords()
x.show_board()
print('\n New Board \n')
#x.move_piece(17,1)
x.show_board()
x.display_coords()
x.piece_at(1,1)
"""while 1:
    
    x.dump_pieces()
    selected = input('Which piece to move')
    m = input('Where to move piece')
    x.move_piece(int(selected), int(m))
    x.show_board()
    x.display_coords()"""
            