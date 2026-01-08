import pygame as pg
import tkinter
from item import Square, Item, Particle
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


player = Player(pg, (screen, screen_width, screen_height))
ui = UI(pg, (screen, screen_width, screen_height), player)

particles = []
for i in range(1000):
    particle = Particle(pg, (screen, screen_width, screen_height), transform, player)
    particles.append(particle)

square = Square(pg, (screen, screen_width, screen_height), transform, player)

#kseg = Item(pg, (screen, screen_width, screen_height), transform, player, "car", "assets/obj/kseg.obj", None, None) # Too many vertices, will lag
#gift = Item(pg, (screen, screen_width, screen_height), transform, player, "giftbox", "assets/obj/gift.obj", None, None)

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill("gray16")

    ## RENDER HERE
    player.update()
    ui.update()
    for particle in particles:
        particle.update()

    #gift.update()

    ## END RENDER
    
    pg.display.flip()
