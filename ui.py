class UI:
    def __init__(self, game, screen, player):
        self.game = game
        self.screen, self.screen_width, self.screen_height = screen
        self.player = player
        self.rect_x = 2
        self.rect_y = 2
        self.rect_w = self.screen_width / 18
        self.rect_h = self.screen_height / 18
        self.ui_rect = None

        if not self.game.font.get_init():
            self.game.font.init()
        return

    def update(self):
        text = self.game.font.SysFont(None, 16)
        self.ui_rect = self.game.Rect(self.rect_x, self.rect_y, self.rect_w, self.rect_h)
        pos = self.player.get_pos()
        theta = self.player.get_theta()
        surface = text.render(f"({pos[0]}, {pos[1]}, {pos[2]})\n({theta[0]}, {theta[1]}, {theta[2]})", True, "antiquewhite4")
        text_rect = surface.get_rect(center=self.ui_rect.center)
        self.game.draw.rect(self.screen, "gray12", self.ui_rect)
        self.screen.blit(surface, text_rect)

