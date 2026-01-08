import numpy as np

#Camera for viewing
class Player:
    def __init__(self, game, screen, c=[0, 10, -100], theta=[0,0,0]):
        self.game = game
        self.screen, self.screen_width, self.screen_height = screen

        self.c = c
        self.theta = theta
        self.speed = 1
        self.look_speed = 0.01
        return

    def update(self):
        #self.game.draw.ellipse(self.screen, self.game.Color(255,255,255), self.game.Rect(self.screen_width / 2 - 10, self.screen_height / 2 - 10, 10, 10), 10)

        if self.game.key.get_pressed()[self.game.K_a]:
            pass
        if self.game.key.get_pressed()[self.game.K_d]:
            pass
        if self.game.key.get_pressed()[self.game.K_s]:
            pass
        if self.game.key.get_pressed()[self.game.K_w]:
            pass
        if self.game.key.get_pressed()[self.game.K_LEFT]:
            pass
        if self.game.key.get_pressed()[self.game.K_UP]:
            pass
        if self.game.key.get_pressed()[self.game.K_RIGHT]:
            pass
        if self.game.key.get_pressed()[self.game.K_DOWN]:
            pass

    def get_pos(self):
        return self.c

    def get_theta(self):
        return self.theta
    
    def move(self, key):
        return

    def move_camera(self, direction):
        return

    def project_2d(self, vertex):
        return
