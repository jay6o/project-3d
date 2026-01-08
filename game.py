import pygame as pg
import tkinter
from item import Square
from player import Player
import transform


root = tkinter.Tk()
root.withdraw() # hide Tkinter window

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

pg.init()
screen = pg.display.set_mode((screen_width, screen_height),)
pg.display.toggle_fullscreen()
pg.mouse.set_visible(False)
clock = pg.time.Clock()
running = True

player = Player(pg, (screen, screen_width, screen_height))
square = Square(pg, (screen, screen_width, screen_height), transform, player, "")

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill("BLACK")

    ## RENDER HERE
    player.update()
    square.update()


    ## END RENDER
    
    pg.display.flip()
