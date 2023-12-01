import tkinter as tk
import random as rn

def main():
    color='green'
    window = tk.Tk()
    window.title('Snake')

    c_draw = tk.Canvas(window,width=600,height=400)
    c_draw.pack()
    texta=tk.StringVar()
    a = tk.Label(window, textvariable = texta, font = ("Times New Roman", 20))
    a.pack()
    texta.set("Zjedzone jabłka:")
    
    class Snake:
        def __init__(self, width, height):
            self.theme=0
            self.grid=0
            self.dt=200
            self.zjedzonejablka=0
            self.bcolor='green'
            self.textb=tk.StringVar()
            self.b = tk.Label(window, textvariable = self.textb, fg=self.bcolor, font = ("Times New Roman", 15))
            self.width=int(width)
            self.height=int(height)
            self.msnake=[[self.width/2, self.height/2],
                         [self.width/2+1, self.height/2],
                         [self.width/2+2, self.height/2]]
            self.move=0
            self.tmove=[[0,1],
                        [1,0],
                        [0,-1],
                        [-1,0]]
            self.size=10
            self.col=False
            self.food=[rn.randint(1,self.width-2), rn.randint(1,self.height-2)]
            self.bomb=[rn.randint(1,self.width-2), rn.randint(1,self.height-2)]
            if self.food[0]==self.bomb[0] or self.food[1]==self.bomb[1]:
                self.bomb=[rn.randint(1,self.width-2), rn.randint(1,self.height-2)]

        def drawBox(self, x , y, color=color):
            c_draw.create_rectangle([x,y,
                                     x+self.size,y+self.size],
                                     fill=color)
            
        def drawOval(self, x , y, color=color):
            c_draw.create_oval([x,y,
                                     x+self.size,y+self.size],
                                     fill=color)

        def drawbackground(self, color='white'):
            c_draw.create_rectangle([0,0,600,400],fill=color)

        def drawgrid(self, x1, y1, x2, y2,color):
            c_draw.create_line([x1, y1, x2, y2],fill=color)
            
        def draw(self):
            c_draw.delete('all')

            if self.col:
                c_draw.create_text([self.width/2*self.size,self.height/2*self.size],
                                   text='Tu ma być tekst przegranej')
            else:
                if self.theme==0:
                    self.drawbackground()
                    self.b.pack()
                    self.textb.set(self.zjedzonejablka)
                    self.b.config(fg=self.bcolor) 
                    if self.grid==1:
                        for i in range(self.width):
                            self.drawgrid(i*self.size, 0, i*self.size, 400, "orange")

                        for i in range(self.height):
                            self.drawgrid(0, i*self.size, 600, i*self.size, "orange")
                    
                    if self.zjedzonejablka<8:
                        self.bcolor='green'
                    elif self.zjedzonejablka<16:
                        self.bcolor='gold'
                    elif self.zjedzonejablka<24:
                        self.bcolor='orange'
                    elif self.zjedzonejablka<32:
                        self.bcolor='red'
                    else:
                        self.bcolor='black'
                    for i in range(self.width):
                        self.drawBox(i*self.size, 0)
                        self.drawBox(i*self.size, (self.height-1)*self.size)

                    for i in range(self.height):
                        self.drawBox(0, i*self.size)
                        self.drawBox((self.width-1)*self.size, i*self.size)
                    
                    for i in self.msnake:
                        self.drawBox(i[0]*self.size,i[1]*self.size)
                    self.drawBox(self.food[0]*self.size, self.food[1]*self.size, color='red')
                    self.drawOval(self.bomb[0]*self.size, self.bomb[1]*self.size, color='gray')

                if self.theme==1:
                    self.drawbackground(color='gray')
                    self.b.pack()
                    self.textb.set(self.zjedzonejablka)
                    self.b.config(fg=self.bcolor)
                    if self.grid==1:
                        for i in range(self.width):
                            self.drawgrid(i*self.size, 0, i*self.size, 400, "darkgray")

                        for i in range(self.height):
                            self.drawgrid(0, i*self.size, 600, i*self.size, "darkgray")
                            
                    if self.zjedzonejablka<8:
                        self.bcolor='green'
                    elif self.zjedzonejablka<16:
                        self.bcolor='gold'
                    elif self.zjedzonejablka<24:
                        self.bcolor='orange'
                    elif self.zjedzonejablka<32:
                        self.bcolor='red'
                    else:
                        self.bcolor='black'
                    for i in range(self.width):
                        self.drawBox(i*self.size, 0, color='black')
                        self.drawBox(i*self.size, (self.height-1)*self.size, color='black')

                    for i in range(self.height):
                        self.drawBox(0, i*self.size, color='black')
                        self.drawBox((self.width-1)*self.size, i*self.size, color='black')
                    
                    for i in self.msnake:
                        self.drawBox(i[0]*self.size,i[1]*self.size, color='black')
                    self.drawBox(self.food[0]*self.size, self.food[1]*self.size, color='silver')
                    self.drawOval(self.bomb[0]*self.size, self.bomb[1]*self.size, color='black')

                
        def eat(self):
            if self.msnake[0][0]==self.food[0] and self.msnake[0][1]==self.food[1]:
                self.msnake.append([0,0])
                self.food=[rn.randint(1,self.width-2), rn.randint(1,self.height-2)]
                self.bomb=[rn.randint(1,self.width-2), rn.randint(1,self.height-2)]
                if self.food[0]==self.bomb[0] or self.food[1]==self.bomb[1]:
                    self.bomb=[rn.randint(1,self.width-2), rn.randint(1,self.height-2)]
                self.zjedzonejablka=self.zjedzonejablka+1

        def move_snake(self):
            for i in range(len(self.msnake) -1,0,-1):
                self.msnake[i][0]=self.msnake[i-1][0]
                self.msnake[i][1]=self.msnake[i-1][1]

            self.msnake[0][0]+= self.tmove[self.move][0]
            self.msnake[0][1]+= self.tmove[self.move][1]

            self.Colision()
            self.eat()
            self.draw()

        
        def turnLeft(self):
            self.move=(self.move+1)%len(self.tmove)

        def turnRight(self):
            self.move=(self.move-1) if self.move>0 else len(self.tmove)-1

        def Colision(self):
            if self.msnake[0][0] == 0 or self.msnake[0][1] == 0 or self.msnake[0][0] == self.width-1 or self.msnake[0][1] == self.height -1:
                 self.col = True

            if self.msnake[0][0]==self.bomb[0] and self.msnake[0][1]==self.bomb[1]:
                self.col = True

            for i in self.msnake[1:]:
                if self.msnake[0][0] == i[0] and self.msnake[0][1] == i[1]:
                    self.col = True
            
        def reset(self):
            self.msnake=[[self.width/2, self.height/2],
                         [self.width/2+1, self.height/2],
                         [self.width/2+2, self.height/2]]
            self.move=0
            self.tmove=[[0,1],
                        [1,0],
                        [0,-1],
                        [-1,0]]
            self.size=10
            self.zjedzonejablka=0
            self.food=[rn.randint(1,self.width-2), rn.randint(1,self.height-2)]
            self.bomb=[rn.randint(1,self.width-2), rn.randint(1,self.height-2)]
            if self.food[0]==self.bomb[0] or self.food[1]==self.bomb[1]:
                self.bomb=[rn.randint(1,self.width-2), rn.randint(1,self.height-2)]
            if self.col == True:
                window.after(self.dt,move)
            else:
                window.after(self.dt)
            self.col=False
            
        def sttheme(self):
            self.theme=0

        def gbtheme(self):
            self.theme=1
            
        def bforget(self):
            self.b.pack_forget()
            
        def gs1(self):
            self.dt=300
        def gs2(self):
            self.dt=150
        def gs3(self):
            self.dt=75
            
        def grd(self):
            if self.grid==0:
                self.grid=1
            else:
                self.grid=0
            
    sn=Snake(600/10,400/10)
    menubar=tk.Menu(window)
    menu=tk.Menu(menubar,tearoff=0)
    theme=tk.Menu(menubar,tearoff=0)
    gs=tk.Menu(menubar,tearoff=0)
    menubar.add_cascade(label='Program',menu=menu)
    menubar.add_cascade(label='Motyw',menu=theme)
    menubar.add_cascade(label='Szybkość gry',menu=gs)
    menu.add_command(label='Od nowa',command=sn.reset)
    menu.add_command(label='Wyjście',command=window.destroy)
    theme.add_command(label='Standardowy',command=sn.sttheme)
    theme.add_command(label='Game Boy',command=sn.gbtheme)
    theme.add_command(label='Siatka', command=sn.grd)
    gs.add_radiobutton(label='Wolne', command=sn.gs1)
    gs.add_radiobutton(label='Normalne', command=sn.gs2)
    gs.add_radiobutton(label='Szybkie', command=sn.gs3)
    window.config(menu=menubar)
    
    sn.draw()
    sn.bforget()

    def move():
        sn.move_snake()
        if not sn.col:
            window.after(sn.dt,move)
            

    def turnLeft(event):
        sn.turnLeft()
    def turnRight(event):
        sn.turnRight()
    
    
    window.after(sn.dt,move)
    window.bind_all('<KeyPress-Left>',turnLeft)
    window.bind_all('<KeyPress-Right>',turnRight)
    window.mainloop()
    return 0



if __name__ == '__main__':
    main()
