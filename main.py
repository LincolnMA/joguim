from tkinter import *
import random
##Functions
def verify_collision():
    global enemies
    index_colision = -1
    for i in range(0,len(enemies)):
        if enemies[i][0] <= position.x <= enemies[i][0]+enemy_size.get():
            if enemies[i][1] <= position.y <= enemies[i][1]+enemy_size.get():
                drops.set(int(drops.get()) + 1)
                index_colision = i
    if(index_colision > 0): del(enemies[index_colision])
def render_enemies():
    global enemies
    screen.delete("all")
    for i in range(0,len(enemies)):
        r = hex(random.randint(16,255))
        g = hex(random.randint(16,255))
        b = hex(random.randint(16,255))
        color = "#" + r[2:] + g[2:] + b[2:]
        enemies[i][1] = enemies[i][1] + 1
        screen.create_rectangle(enemies[i][0],
                                enemies[i][1],
                                enemies[i][0]+enemy_size.get(),
                                enemies[i][1]+enemy_size.get(),
                                fill = color)
def generate_enemy():
    global enemies
    if run == True:
        for i in range(0,n.get()):
            enemies.append([random.randint(0,300),0])
        for i in range(0,n.get()):
            if(enemies[i][1] > 300): del(enemies[i])
        screen.after(delay_enemy.get(),generate_enemy)
def update():
    if run == True:
        render_enemies()
        verify_collision()
        screen.after(delay.get(),update)
def on(event):
    global position
    global run
    position = event
    if run == False:
        run = True
        generate_enemy()
        update()
def off(event):
    global run
    run = False
##Variables
window = Tk()
run = False
position = []
enemies = []
delay = IntVar()
n = IntVar()
delay_enemy = IntVar()
enemy_size = IntVar()
drops = StringVar()
drops.set("0")
##SideBar
sidebar = Frame(window)
sidebar.grid(row = 0, column = 0)
#Title
lb1 = Label(sidebar,text = "RainDrops",font = ('Times', '24', 'bold italic'))
lb1.grid(row = 0,column = 0)
#Scale to refresh in ms
scL1 = Scale(sidebar,orient = HORIZONTAL,from_ = 1000,to = 1,
             length = 150,label = "Refresh",variable = delay)
scL1.grid(row = 1,column = 0)
#Scale to number of enemies
scL2 = Scale(sidebar,orient = HORIZONTAL,from_ = 50,to = 1,
             length = 150,label = "Number of Enemies",variable = n)
scL2.grid(row = 2,column = 0)
#Scale to delay of enemies
scL3 = Scale(sidebar,orient = HORIZONTAL,from_ = 1000,to = 1,
             length = 150,label = "Delay of Enemies",variable = delay_enemy)
scL3.grid(row = 3,column = 0)
#Scale to size of enemies
scL4 = Scale(sidebar,orient = HORIZONTAL,from_ = 50,to = 1,
             length = 150,label = "Size of Enemies",variable = enemy_size)
scL4.grid(row = 4,column = 0)
#Label of Counter drops
lb2 = Label(sidebar,text = "Score",font = ('Times', '15', 'bold italic'))
lb2.grid(row = 5,column = 0)
#Counter of drops
ent = Entry(sidebar,textvariable = drops)
ent.grid(row = 6,column = 0)

##Tela
screen = Canvas(window,bg = "white",cursor = "man",width = 300,height = 300)
screen.grid(row = 0,column = 1)
screen.bind("<Motion>",on)
screen.bind("<Leave>",off)
##MainLoop
window.mainloop()