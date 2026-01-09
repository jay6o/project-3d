import pygame as pg
import tkinter
from model import Square, Particle
from player import Player
import transform
from ui import UI


root = tkinter.Tk()
root.withdraw() # hide Tkinter window

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

pg.init()
screen = pg.display.set_mode((screen_width, screen_height),)
pg.display.set_caption("3D Engine")
pg.display.toggle_fullscreen()
pg.mouse.set_visible(False)
clock = pg.time.Clock()
running = True


updatables = []

player = Player(pg, (screen, screen_width, screen_height))
updatables.append(player)
ui = UI(pg, (screen, screen_width, screen_height), player)
updatables.append(ui)


for i in range(1000):
    particle = Particle(pg, (screen, screen_width, screen_height), transform, player)
    updatables.append(particle)

#square = Square(pg, (screen, screen_width, screen_height), transform, player)
#updatables.append(square)

#kseg = Model(pg, (screen, screen_width, screen_height), transform, player, "car", "assets/obj/kseg.obj", None, None) # Too many vertices, will lag
#gift = Model(pg, (screen, screen_width, screen_height), transform, player, "giftbox", "assets/obj/gift.obj", None, None)

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        pass

    screen.fill("gray16")

    ## RENDER HERE
    for item in updatables:
        item.update()

    #gift.update()

    ## END RENDER
    
    pg.display.flip()
