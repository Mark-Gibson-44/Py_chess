from tkinter import *
import tkinter.font as tkFont
import math as m
from Board import *
"""Class concerned with the Gui of the game
Will use a Board class to act as a model for the location of the pieces
"""
class View():

    """
    Will generate the starting pieces done via the board Initialisation
    """
    def init_pieces(self):
        pawn1 = self.canvas.create_text(37, 75 + 37, text='P', font=self.fontStyle, fill='blue')
        self.pieces_img.append(pawn1)

    """
    Draws the squares on the gui
    """
    def draw_pieces(self):
        coord = [0, 0, 75, 75]
        coord2 = [75,  75, 150, 150]
        space = 150
        for i in range (5):
    
            for j in range (5):
        
                self.canvas.create_rectangle(coord, fill='grey', outline='grey')
                coord[0] = coord[0] + space
                coord[2] = coord[2] + space
            coord[0] = 0
            coord[2] = 75
            coord[1] = coord[1] + space
            coord[3] = coord[3] + space
    
        for i in range (4):
    
            for j in range (4):
        
                self.canvas.create_rectangle(coord2, fill='grey', outline='grey')
                coord2[0] = coord2[0] + space
                coord2[2] = coord2[2] + space
            coord2[0] = 75
            coord2[2] = 150
            coord2[1] = coord2[1] + space
            coord2[3] = coord2[3] + space
        self.canvas.pack()
    """
    Will need a boolean to determine whether a piece is being moved or selected
    Could be useful when considering takes
    """
    def select_piece(self, event):
        
        self.canvas.delete(self.highlighted_move)
        x = m.floor((event.x /75 +  1)) * 75 - 37
        y = m.floor((event.y /75 +  1)) * 75 - 37
      
        if ((m.floor((event.x /75)),m.floor((event.y /75)))) in self.positions:
            
            self.highlighted_move = self.canvas.create_text(x, y, text='P', font=self.fontStyle, fill='red')


    def move_piece(self ,event):
        self.canvas.delete(self.pieces_img.pop())
        if(False):
            return
        
        x = m.floor((event.x /75 +  1)) * 75 - 37
        y = m.floor((event.y /75 +  1)) * 75 - 37
      
        new_move = self.canvas.create_text(x, y, text='P', font=self.fontStyle, fill='blue')
        self.pieces_img.append(new_move)


    def __init__(self):
        self.top = Tk()
        self.w = 600#Width of Board
        self.h = 600#Height of Board
        self.bgr = 'black'
        self.positions =[(0,1) ]#Temp for testing
        self.canvas = Canvas(self.top, bg=self.bgr, width = self.w, height = self.h)
        self.pieces_img = []#Will be a list of canvas texts maybe not
        self.fontStyle = tkFont.Font(family="Lucida Grande", size=50) #Font
        self.draw_pieces()
        self.init_pieces()
        #TODO eventually develop function that inits all binds
        self.canvas.bind('<Button-1>',self.move_piece)
        self.canvas.bind('<Button-1>',self.select_piece)
        self.highlighted_move = None

    def play(self):
        self.canvas.pack()
        self.top.mainloop()

v = View()
v.play()