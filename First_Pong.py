#!/usr/bin/env python
# coding: utf-8

# In[313]:


from tkinter import *
import random
from random import choice


# ### insert the black screen in which the game will be played

# In[314]:


master = Tk()

alt=351
esp=624
pont1 = 0
pont2 = 0
l=100
w = Canvas(master, width=esp, height=alt)
w.pack()

w.create_rectangle(0, 0, 624, 351, fill="black")
i=0
while i <= alt:
    w.create_line(esp/2,i,esp/2,i+5,fill="white",width=2)
    i=i+10

w.create_text(10,5,anchor=NW, text = "Player", fill = "white")
w.create_text(esp-10,5,anchor=NE, text = "Computador", fill = "white")
w.create_text(esp/2-300, 25,anchor=NW,text = "f:facil  m:medio  d:dificil  i:impossivel", fill = "white")
dific = w.create_text(esp/2+20,25,anchor=NW,text = "facil",fill = "white")
teto = w.create_line(0,20,esp,20,fill="white",width=2)
pon1 = w.create_text(esp/2-10,5,anchor = NE, text = str(pont1) , fill = "white",width = 10)
pon2 = w.create_text(esp/2+10,5,anchor = NW, text = str(pont2), fill = "white",width = 10)


# ### insert the function of the paddle

# In[315]:


class paddle:
    def __init__(self,x):
        self.x = x
        self.h = 80
        self.wi = 20
        self.y = 351/2
        self.rec=w.create_rectangle(self.x,self.y,self.x+self.wi,self.y+self.h,fill="white")
        
    def up(self,w):
        x1,y1,x2,y2 = w.coords(self.rec)
        if y1-10>20:
            w.move(self.rec,0,-15)

    def down(self,w):
        x1,y1,x2,y2 = w.coords(self.rec)
        if y2+10<alt-5:
            w.move(self.rec,0,15)

class ball:
    def __init__(self,x,veloc):
        self.radius = x
        self.veloc = veloc
        self.create()
    def move(self,w,coord1,coord2):
        x1,y1,x2,y2 = w.coords(self.bola)
        if y1+self.diry < 20 or y2+self.diry > 351:
            self.diry = - self.diry
        if (x2 >= coord2[0] and (y1+y2)/2>coord2[1] and (y1+y2)/2<coord2[3]) or (x1 <= coord1[2] and (y1+y2)/2>coord1[1] and (y1+y2)/2<coord1[3]):
            self.dirx = - self.dirx
        w.move(self.bola,self.dirx,self.diry)
    def create(self):
        dx = choice([i for i in range(-10,11) if i not in [0]])
        dy = choice([i for i in range(-10,11) if i not in [0]])        
        mod = pow(dx*dx+dy*dy,0.5)
        self.dirx = self.veloc*(dx/mod)
        self.diry = self.veloc*(dy/mod)
        self.bola = w.create_oval(624/2-self.radius,351/2-self.radius,624/2+self.radius,351/2+self.radius,fill="white") 
    
bola = ball(10,12)#raio=10,veloc=12
player1 = paddle(26)
player2 = paddle(624-46)


# In[316]:


def points(pont1,pont2):
    global pon1
    global pon2
    w.delete(pon1)
    pon1 = w.create_text(esp/2-10,5,anchor = NE, text = str(pont1) , fill = "white",width = 10)
    w.delete(pon2)
    pon2 = w.create_text(esp/2+10,5,anchor = NW, text = str(pont2), fill = "white",width = 10)
    w.delete(bola.bola)
    bola.create()
    return pont1,pont2


# ## make the ball move

# In[317]:


def update():
    global pont1
    global pont2
    global l
    bola.move(w,w.coords(player1.rec),w.coords(player2.rec))
    if w.coords(bola.bola)[1]+l<w.coords(player2.rec)[1]:
        player2.up(w)
    if w.coords(bola.bola)[3]-l>w.coords(player2.rec)[3]:
        player2.down(w)
    if w.coords(bola.bola)[0]>w.coords(player2.rec)[0]: #ponto do player 1
        pont1,pont2 = points(pont1+1,pont2)
    if w.coords(bola.bola)[2]<w.coords(player1.rec)[2]: #ponto do player 2
        pont1,pont2 = points(pont1,pont2+1)
    w.after(50,update)

w.after(50,update)


# ## key binding and main loop

# In[318]:


def callback1(event):
    player1.up(w)
def callback2(event):
    player1.down(w)
def callback3(event):
    player2.up(w)
def callback4(event):
    player2.down(w)
def callback5(event):
    global pont1
    global pont2
    pont1,pont2 = points(0,0)

def dificul(event):
    global l
    global dific
    if event.char == 'f':
        l=100
        texto = "facil"
    if event.char == 'm':
        l=66
        texto = "medio"
    if event.char == 'd':
        l=33
        texto = "dificil"
    if event.char == 'i':
        l=0
        texto = "impossivel"
    w.delete(dific)
    dific = w.create_text(esp/2+20,25,anchor=NW,text = texto,fill = "white")
    
w.bind("w", callback1)#moveup
w.bind("s",callback2)#movedown
w.bind("p",callback5) #RESET no game
w.bind("f", dificul)
w.bind("m",dificul)
w.bind("d", dificul)
w.bind("i",dificul)
w.focus_set()
w.mainloop()

