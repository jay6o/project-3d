import cProfile
import pygame as pg
import tkinter
from model import Cube, Particle, Model
from player import Player
import transform
from ui import UI


with cProfile.Profile() as pr:
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
    frame = 0
    
    updatables = []
    
    player = Player(pg, (screen, screen_width, screen_height))
    updatables.append(player)
    ui = UI(pg, (screen, screen_width, screen_height), player)
    updatables.append(ui)
    
    
    #for i in range(1000):
    #    particle = Particle(pg, (screen, screen_width, screen_height), transform, player)
    #    updatables.append(particle)
    
    cube = Cube(pg, (screen, screen_width, screen_height), transform, player)
    updatables.append(cube)
    
    #kseg = Model(pg, (screen, screen_width, screen_height), transform, player, "car", "assets/obj/kseg.obj", None, None) # Too many vertices, will lag
    #updatables.append(kseg)
    #gift = Model(pg, (screen, screen_width, screen_height), transform, player, "giftbox", "assets/obj/gift.obj", None, None)
    
    while running:
        for event in pg.event.get():
            frame += 1
            if event.type == pg.QUIT:
                running = False
                pr.print_stats(sort="time")
            pass
    
        screen.fill("gray16")
    
        ## RENDER HERE
        for item in updatables:
            item.update()
    
        #gift.update()
    
        ## END RENDER
        
        pg.display.flip()
