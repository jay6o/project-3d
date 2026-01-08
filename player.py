import numpy as np
from math import cos, sin

#Player Eye for viewing and moving around 3D world
class Player:
    def __init__(self, game, screen, c=[0, 10, -100], theta=[0,0,0]):
        self.game = game
        self.screen, self.screen_width, self.screen_height = screen

        self.c = c
        self.theta = theta
        self.speed = 1
        self.look_speed = 0.05
        return

    def update(self):
        #self.game.draw.ellipse(self.screen, self.game.Color(255,255,255), self.game.Rect(self.screen_width / 2 - 10, self.screen_height / 2 - 10, 10, 10), 10)

        #4-Directional movement
        if self.game.key.get_pressed()[self.game.K_a]:
            self.c[0] += self.speed * (sin(self.theta[1] - np.pi / 2));
            self.c[1] = self.c[1];
            self.c[2] += self.speed * cos(self.theta[1] - np.pi / 2);
        if self.game.key.get_pressed()[self.game.K_d]:
            self.c[0] -= self.speed * (sin(self.theta[1] - np.pi / 2));
            self.c[1] = self.c[1];
            self.c[2] -= self.speed * cos(self.theta[1] - np.pi / 2);
        if self.game.key.get_pressed()[self.game.K_s]:
            self.c[0] -= self.speed * sin(self.theta[1]);
            self.c[1] = self.c[1];
            self.c[2] -= self.speed * cos(self.theta[1]);
        if self.game.key.get_pressed()[self.game.K_w]:
            self.c[0] += self.speed * sin(self.theta[1]);
            self.c[1] = self.c[1];
            self.c[2] += self.speed * cos(self.theta[1]);

        # Pitch, yaw, no roll camera rotations
        if self.game.key.get_pressed()[self.game.K_LEFT]:
            self.theta[1] -= self.look_speed
        if self.game.key.get_pressed()[self.game.K_UP]:
            self.theta[0] += self.look_speed
        if self.game.key.get_pressed()[self.game.K_RIGHT]:
            self.theta[1] += self.look_speed
        if self.game.key.get_pressed()[self.game.K_DOWN]:
            self.theta[0] -= self.look_speed

    def get_pos(self):
        return self.c

    def get_theta(self):
        return self.theta
