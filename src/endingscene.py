import sceneac as sca
import pygame

class EndScene(sca.AbstractScene):

    def __init__(self, screen, _scene_id):
        super().__init__(screen, _scene_id)
        self.exit_button = (350, 350, 20, 20)

    def logic(self):
        active_scene = self._scene_id
        crashed = False

        for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.dict['button'] == 1:
                    # checks button boundaries
                    if 350 < event.dict['pos'][0] < 370 and 350 < event.dict['pos'][1] < 370:
                        crashed = True

        return crashed, active_scene

    def draw(self):
        self.background.fill((255, 255, 255))

        pygame.draw.rect(self.background, (250, 50, 50), self.exit_button)

        return self.background
