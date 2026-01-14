import numpy as np
from math import cos, sin

#Player Eye for viewing and moving around 3D world
class Player:
    def __init__(self, game, screen, c=None, theta=None):
        self.game = game
        self.screen, self.screen_width, self.screen_height = screen

        self.c = c if c is not None else np.array([0.0, 30, -100])
        self.theta = theta if theta is not None else np.array([0.0, 0.0, 0.0])
        self.speed = 0.5
        self.look_speed = 0.03
        return

    def get_rotation(self):
        cx, cy, cz = cos(self.theta[0]), cos(self.theta[1]), cos(self.theta[2])
        sx, sy, sz = sin(self.theta[0]), sin(self.theta[1]), sin(self.theta[2])

        Rx = np.array([[1, 0, 0],
                       [0, cx, sx],
                       [0, -sx, cx]])

        Ry = np.array([[cy, 0, -sy],
                       [0, 1, 0],
                       [sy, 0, cy]])

        Rz = np.array([[cz, sz, 0],
                       [-sz, cz, 0],
                       [0, 0, 1]])

        return Rx @ Ry @ Rz

    def update(self):
        #self.game.draw.ellipse(self.screen, self.game.Color(255,255,255), self.game.Rect(self.screen_width / 2 - 10, self.screen_height / 2 - 10, 10, 10), 10)

        #4-Directional movement
        if self.game.key.get_pressed()[self.game.K_a]:
            self.c[0] += self.speed * (sin(self.theta[1] - np.pi / 2));
            self.c[2] += self.speed * cos(self.theta[1] - np.pi / 2);
        if self.game.key.get_pressed()[self.game.K_d]:
            self.c[0] -= self.speed * (sin(self.theta[1] - np.pi / 2));
            self.c[2] -= self.speed * cos(self.theta[1] - np.pi / 2);
        if self.game.key.get_pressed()[self.game.K_s]:
            self.c[0] -= self.speed * sin(self.theta[1]);
            self.c[2] -= self.speed * cos(self.theta[1]);
        if self.game.key.get_pressed()[self.game.K_w]:
            self.c[0] += self.speed * sin(self.theta[1]);
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

        self.rotation = self.get_rotation()
        print(self.rotation)

    def get_pos(self):
        return self.c

    def get_theta(self):
        return self.theta

