class Item:
    def  __init__(self, game, screen, transform, player, name, vertices: dict[str, list[int]] | None, faces=None):
        self.game = game
        self.screen, self.screen_width, self.screen_height = screen
        self.transform = transform
        self.player = player
        self.name = name
        self.vertices = vertices
        self.faces = faces
        self.transformed = None
        self.v_width = 5
        self.visible = False

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
                    self.game.draw.ellipse(self.screen, (255,255,255), self.game.Rect(self.screen_width / 2 + b[0], self.screen_height / 2 + b[1], 5, 5))

        return

    def read_obj():
        pass



class Square(Item):
    def __init__(self, game, screen, transform, player, name="Cube", vertices={"v0":[-100, -100, -100], 
                                              "v1": [-100, -100, 100], 
                                              "v2": [-100, 100, -100], 
                                              "v3": [-100, 100, 100],
                                              "v4": [100, -100, -100],
                                              "v5": [100, -100, 100],
                                              "v6": [100, 100, -100],
                                              "v7": [100, 100, 100]}, faces=None):
        super().__init__(game, screen, transform, player, name, vertices, faces)
        self.v_coords = None

    def get_vertices(self):
        return self.vertices

