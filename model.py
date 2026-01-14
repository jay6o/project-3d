import random
import math
import numpy as np

class Model:
    def  __init__(self, game, screen, transform, player, name, file: str | None, vertices: np.ndarray | None, faces=None):
        self.game = game
        self.screen, self.screen_width, self.screen_height = screen
        self.transform = transform
        self.player = player
        self.name = name
        self.file = file
        self.v = vertices
        self.vt = None
        self.vn = None
        self.vp = None
        self.f = faces
        self.transformed = None
        self.v_width = 5
        self.visible = True

        if self.file is not None and self.v is None:
            filetype = self.file.split('.')[-1]
            match filetype:
                case 'obj':
                    self.v = {}
                    v_count = 0
                    with open(self.file, 'r') as f:
                        for line in f:
                            curr = line.split()
                            if curr[0] == 'v':
                                x,y,z = float(curr[1]), float(curr[2]), float(curr[3])
                                self.v[v_count] = [x, y, z]
                                v_count += 1
                    return
                case _:
                    print("Unsupported file format, use a .obj")
                    return
            
    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def update(self):
        if self.v is not None:
            for v in self.v:
                print(v)
                c = self.player.get_pos()
                b = self.transform.project(v, c, self.player.get_theta())

                # Draw vertices
                self.visible = True if b is not None else False
                if self.visible:
                    distance = math.sqrt((v[0]-c[0]) ** 2 + (v[1] - c[1]) ** 2 + (v[2] - c[2]) ** 2)
                    self.game.draw.ellipse(self.screen, (255,255,255), self.game.Rect(self.screen_width / 2 + b[0,0], self.screen_height / 2 + b[0,1], 300/distance, 300/distance))
        return

    def draw_faces(self):
        pass

    def get_vertices(self):
        return self.v



class Cube(Model):
    def __init__(self, game, screen, transform, player, name="Cube", file=None, vertices=None, faces=None):
        super().__init__(game, screen, transform, player, name, file, vertices, faces)
        self.v = np.array([[-100, 0, -100],
                           [100, 0, -100],
                           [100, 0, 100],
                           [-100, 0, 100],
                           [-100, 200, -100],
                           [100, 200, -100],
                           [100, 200, 100],
                           [-100, 200, 100]])


class Particle(Model):

    def __init__(self, game, screen, transform, player, name="Cube", file=None, vertices=None, faces=None):
        super().__init__(game, screen, transform, player, name, file, vertices, faces)
        self.fall_rate = -random.uniform(-1, -0.01)
        self.v = np.array([[random.uniform(-100, 100), random.uniform(100, 500), random.uniform(-100, 100)]])
        self.stop = False
        self.b = None
    
    def update(self):
        if not self.stop:
            if self.v[0,1] -self.fall_rate <= 0.00:
                self.v[0,1] = 0
                self.stop = True
            else:
                self.v[0,1] -= self.fall_rate

        c = self.player.get_pos()
        self.b = self.transform.project(self.v, c, self.player.get_theta())
        if self.b is None:
            self.visible = False

        # Draw vertices
        if self.visible:
            distance = math.sqrt(((self.v[0,0]-c[0]) ** 2) + ((self.v[0,1] - c[1]) ** 2) + ((self.v[0,2] - c[2]) ** 2))
            size = 1/0.9 * 200/distance
            self.game.draw.ellipse(self.screen, (255,255,255), self.game.Rect(self.screen_width / 2 + self.b[0,0] - size/2, self.screen_height / 2 + self.b[0,1] - size/2, size, size))
        self.visible = True
        return
