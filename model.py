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
        self.visible = None
        self.vt = None
        self.vn = None
        self.vp = None
        self.f = faces
        self.l = None
        self.transformed = None
        self.v_width = 5
        self.visible = True
        self.frame_loaded = 0

        if self.file is not None and self.v is None:
            filetype = self.file.split('.')[-1]
            match filetype:
                case 'obj':
                    self.v = []
                    self.vt = []
                    self.vn = []
                    self.vp = []
                    self.f = []
                    self.l = []
                    v_count = 0
                    with open(self.file, 'r') as f:
                        for line in f:
                            curr = line.strip().split()
                            if len(curr) > 0:
                                if curr[0] == 'v':
                                    x,y,z = float(curr[1]), float(curr[2]), float(curr[3])
                                    self.v.append([x, y, z])
                                    v_count += 1
                                if curr[0] == 'vt':
                                    copy = curr.copy()
                                    copy.pop(0)
                                    self.vt.append([float(i) for i in copy])
                                    pass
                                if curr[0] == 'vn':
                                    x,y,z = float(curr[1]), float(curr[2]), float(curr[3])
                                    self.vn.append([x, y, z])
                                if curr[0] == 'vp':
                                    copy = curr.copy()
                                    copy.pop(0)
                                    self.vp.append([float(i) for i in copy])
                                if curr[0] == 'f':
                                    copy = curr.copy()
                                    copy.pop(0)
                                    face = []
                                    for i in range(len(copy)):
                                        start = 0
                                        to = len(curr[i])

                                    pass
                                if curr[0] == 'l':
                                    pass
                    self.v = np.array(self.v)
                    self.vt = np.array(self.vt)
                    self.vn = np.array(self.vn)
                    self.vp = np.array(self.vp)
                    self.f = np.array(self.f)
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
            c = self.player.get_pos()
            bx, by = self.transform.project_vertices(self.v, c, self.player.get_rotation())
            size = 8
            for i in range(len(bx)):
                self.game.draw.ellipse(self.screen, (255,255,255), self.game.Rect(self.screen_width / 2 + bx[i], self.screen_height / 2 - by[i] - size/2, size, size))
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
                           [-100, 200, 100],])


class Particle(Model):

    def __init__(self, game, screen, transform, player, name="Cube", file=None, vertices=None, faces=None):
        super().__init__(game, screen, transform, player, name, file, vertices, faces)
        self.fall_rate = -random.uniform(-1, -0.01)
        self.v = np.array([[random.uniform(-100, 100),
                            random.uniform(100, 500), 
                            random.uniform(-100, 100)],])
        self.stop = False

    def update(self):
        if not self.stop:
            if self.v[0,1] -self.fall_rate <= 0.00:
                self.v[0,1] = 0
                self.stop = True
            else:
                self.v[0,1] -= self.fall_rate

        c = self.player.get_pos()
        bx, by = self.transform.project_vertices(self.v, c, self.player.get_rotation())
        if len(bx) > 0 and len(by) > 0:
            distance = math.sqrt(((self.v[0,0]-c[0]) ** 2) + ((self.v[0,1] - c[1]) ** 2) + ((self.v[0,2] - c[2]) ** 2))
            size = 200/distance
            self.game.draw.ellipse(self.screen, (255,255,255), self.game.Rect(self.screen_width / 2 + bx[0] - size/2, self.screen_height / 2 - by[0] - size/2, size, size))
        return
