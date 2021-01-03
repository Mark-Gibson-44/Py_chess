from tkinter import *
import tkinter.font as tkFont
import math as m
from Board import *
"""Class concerned with the Gui of the game
Will use a Board class to act as a model for the location of the pieces
"""
class View():


    """
    Initialises all possible Gui events
    """
    def init_events(self):
        pass
    """
    Will generate the starting pieces done via the board Initialisation
    """
    def init_pieces(self):
        for i in self.b.white:
            col = 'white'
            x = (i.coords[0] + 1) * 75 - 37
            y = (i.coords[1] + 1) * 75 - 37
            t = i.name
            p = self.canvas.create_text(x, y, text=t, font=self.fontStyle, fill=col)
            self.pieces_img.append(p)
        for k in self.b.black:
            col = 'black'
            x = (k.coords[0] + 1) * 75 - 37
            y = (k.coords[1] + 1) * 75 - 37
            t = k.name
            p = self.canvas.create_text(x, y, text=t, font=self.fontStyle, fill=col)
            self.pieces_img.append(p)
       

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
        self.init_pieces()
        self.canvas.pack()
    """
    Will need a boolean to determine whether a piece is being moved or selected
    Could be useful when considering takes
    """
    def select_piece(self, event):
        
        if self.highlighted_move[0] is not None:
            
            self.canvas.delete(self.highlighted_move[0])
            self.highlighted_move = None, None
            return
        
       
        x = m.floor((event.x /75 +  1)) * 75 - 37
        y = m.floor((event.y /75 +  1)) * 75 - 37
        self.select_piece = self.b.piece_colour((m.floor(event.x/75), m.floor(event.y/75)))
        occupied, position = (self.b.piece_at(m.floor((event.x /75)),m.floor((event.y /75))))
        if occupied:
            self.highlighted_move = self.canvas.create_text(x, y, text=position.name, font=self.fontStyle, fill='red'),position
        

    def logger(self):
        self.b.dump_pieces()

    def move_piece(self ,event):
        
        
        if self.highlighted_move[0] is not None:
            self.logger()
            x = m.floor((event.x /75))
            y = m.floor((event.y /75))
           
            self.b.take((x,y), self.select_piece)
            
            self.b.gui_move_piece(self.select_piece, self.highlighted_move[1], (x,y))
            self.canvas.delete('all')
            self.draw_pieces()
            

        
      
        
        

    

    def __init__(self):
        self.b = Board()
        self.top = Tk()
        self.w = 600#Width of Board
        self.h = 600#Height of Board
        self.bgr = 'green'
        self.positions =[(0,1) ]#Temp for testing
        self.canvas = Canvas(self.top, bg=self.bgr, width = self.w, height = self.h)
        self.pieces_img = []#Will be a list of canvas texts maybe not
        self.fontStyle = tkFont.Font(family="Lucida Grande", size=50) #Font
        self.draw_pieces()
        self.init_pieces()
        #TODO eventually develop function that inits all binds
        self.canvas.bind('<Button-1>',self.move_piece)
        self.canvas.bind('<Button-1>',self.select_piece, add=True)
        
        self.highlighted_move = None, None
        self.selected_piece = None

    def play(self):
        
        
        self.canvas.pack()
        self.top.mainloop()

v = View()
v.play()