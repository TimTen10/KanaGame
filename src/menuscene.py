import sceneac as sca
import pygame

class MenuScene(sca.AbstractScene):

    def __init__(self, screen, _scene_id):
        super().__init__(screen, _scene_id)
        self.a_row = False
        self.ka_row = False
        self.sa_row = False
        self.ta_row = False
        self.na_row = False
        self.ha_row = False
        self.ma_row = False
        self.ya_row = False
        self.ra_row = False
        self.wa_row = False
        self.n_row = False

    def logic(self):
        crashed = False
        return crashed

    def draw(self):
        self.background.fill((255, 255, 255))
        return self.background
