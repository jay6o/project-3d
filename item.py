import random
class Item:
    def  __init__(self, game, screen, transform, player, name, file: str | None, vertices: dict[str, list[int]] | None, faces=None):
        self.game = game
        self.screen, self.screen_width, self.screen_height = screen
        self.transform = transform
        self.player = player
        self.name = name
        self.file = file
        self.vertices = vertices
        self.faces = faces
        self.transformed = None
        self.v_width = 5
        self.visible = False

        if self.file is not None and self.vertices is None:
            self.vertices = {}
            v_count = 0
            with open(self.file, 'r') as f:
                for line_n, line in enumerate(f, start=0):
                    if line is None or line == '\n' or line_n % 30 != 0:
                        continue
                    curr = line.split()
                    if curr[0] == 'v':
                        x,y,z = float(curr[1]), float(curr[2]), float(curr[3])
                        self.vertices[v_count] = [x, y, z]
                        v_count += 1
                    #else:
                    #    break
                    #curr = 0
                    #oid = ''
                    #while line[curr] != ' ':
                    #    oid = oid + line[curr]
                    #    curr += 1

                    #if oid != 'v':
                    #    break

                    #match oid:

                    #    case 'v':
                    #        while
                    #        break
                        #case 'vt':
                        #    break
                        #case 'vn':
                        #    break
                        #case 'vp':
                        #    break
                        #case 'f':
                        #    print("")
                        #    break
                        #case _:
                        #    break
            
    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def update(self):
        if self.vertices is not None:
            for k, v in self.vertices.items():
                c = self.player.get_pos()
                theta = self.player.get_theta()
                b = self.transform.compute_2d(v, c, theta)

                # Draw vertices
                self.visible = True if b is not None else False
                if self.visible:
                    self.game.draw.ellipse(self.screen, (255,255,255), self.game.Rect(self.screen_width / 2 + b[0], self.screen_height / 2 + b[1], 0.1, 0.1))
                    
        return

    def read_obj(self):
        pass



class Square(Item):
    def __init__(self, game, screen, transform, player, name="Cube", file=None, vertices={"v0":[-100, -100, -100], 
                                              "v1": [-100, -100, 100], 
                                              "v2": [-100, 100, -100], 
                                              "v3": [-100, 100, 100],
                                              "v4": [100, -100, -100],
                                              "v5": [100, -100, 100],
                                              "v6": [100, 100, -100],
                                              "v7": [100, 100, 100]}, faces=None):
        super().__init__(game, screen, transform, player, name, file, vertices, faces)

    def get_vertices(self):
        return self.vertices

class Particle(Item):

    def __init__(self, game, screen, transform, player, name="Cube", file=None, vertices=None, faces=None):
        super().__init__(game, screen, transform, player, name, file, vertices, faces)
        self.fall_rate = -random.uniform(-1, -0.01)
        self.vertices = {0: [random.uniform(-100, 100), random.uniform(100, 500), random.uniform(-100, 100)]}
 
    
    def update(self):
        self.vertices[0][1] -= self.fall_rate
        for k, v in self.vertices.items():
            c = self.player.get_pos()
            theta = self.player.get_theta()
            b = self.transform.compute_2d(v, c, theta)

            # Draw vertices
            self.visible = True if b is not None else False
            if self.visible:
                self.game.draw.ellipse(self.screen, (255,255,255), self.game.Rect(self.screen_width / 2 + b[0], self.screen_height / 2 + b[1], 0.1, 0.1))
        return
