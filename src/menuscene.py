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
        self.exit_button = (350, 350, 20, 20)

    def logic(self):
        active_scene = self._scene_id
        crashed = False
        scene_info = None

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                crashed = True

            if event.type == pygame.MOUSEBUTTONDOWN and event.dict['button'] == 1:
                # checks button boundaries
                if 350 < event.dict['pos'][0] < 370 and 350 < event.dict['pos'][1] < 370:
                    active_scene = 1

        return crashed, active_scene, scene_info

    def draw(self):
        self.background.fill((255, 255, 255))

        pygame.draw.rect(self.background, (250, 50, 50), self.exit_button)

        return self.background
