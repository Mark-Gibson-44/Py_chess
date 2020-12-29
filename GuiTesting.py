from tkinter import *
import tkinter.font as tkFont
import math as m
top = Tk()
h = 600
w = 600
C = Canvas(top, bg="black", width = w, height = h)

def motion(event):
  print("Mouse position: (%s %s)" % (event.x, event.y))
  print('Piece at: (%s %s)' % (m.floor((event.x /75 +  1)), m.floor((event.y /75 +  1))))
  return
def move(event):
    C.delete('all')
    x = m.floor((event.x /75 +  1)) * 75 - 37
    y = m.floor((event.y /75 +  1)) * 75 - 37
        
    t = C.create_text(x, y, text='P', font=fontStyle, fill='blue')
    
    #C.update()
    return

coord = [0, 0, 75, 75]
coord2 = [75,  75, 150, 150]
space = 150
i = 0
for i in range (5):
    
    for j in range (5):
        
        C.create_rectangle(coord, fill='grey', outline='grey')
        coord[0] = coord[0] + space
        coord[2] = coord[2] + space
    coord[0] = 0
    coord[2] = 75
    coord[1] = coord[1] + space
    coord[3] = coord[3] + space
    print(coord[1])
for i in range (4):
    
    for j in range (4):
        
        C.create_rectangle(coord2, fill='grey', outline='grey')
        coord2[0] = coord2[0] + space
        coord2[2] = coord2[2] + space
    coord2[0] = 75
    coord2[2] = 150
    coord2[1] = coord2[1] + space
    coord2[3] = coord2[3] + space
    print(coord[1])

fontStyle = tkFont.Font(family="Lucida Grande", size=50)
begin = C.create_text(37, 75 + 37, text='P', font=fontStyle, fill='blue')
#C.create_text(37, 487, text='P', font=fontStyle, fill='blue')
#line2 = C.create_line(coord2, fill="red")

C.bind('<Button-1>',motion)
C.bind('<Button-1>',move)
C.pack()
top.mainloop()