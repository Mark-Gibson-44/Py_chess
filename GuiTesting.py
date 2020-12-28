from tkinter import *
  
top = Tk()
h = 800
w = 800
C = Canvas(top, bg="black", width = w, height = h)

coord = [0, 0, 100, 100]
coord2 = [100,  100, 200, 200]
space = 200
i = 0
for i in range (5):
    
    for j in range (5):
        
        C.create_rectangle(coord, fill='grey', outline='grey')
        coord[0] = coord[0] + space
        coord[2] = coord[2] + space
    coord[0] = 0
    coord[2] = 100
    coord[1] = coord[1] + space
    coord[3] = coord[3] + space
    print(coord[1])
for i in range (4):
    
    for j in range (4):
        
        C.create_rectangle(coord2, fill='grey', outline='grey')
        coord2[0] = coord2[0] + space
        coord2[2] = coord2[2] + space
    coord2[0] = 100
    coord2[2] = 200
    coord2[1] = coord2[1] + space
    coord2[3] = coord2[3] + space
    print(coord[1])
    
C.create_text(50, 50, text='P', anchor='nw', font='TkMenuFont', fill='red')
#line2 = C.create_line(coord2, fill="red")

C.pack()
top.mainloop()