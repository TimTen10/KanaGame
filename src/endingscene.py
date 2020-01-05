import sceneac as sca
import pygame

class EndScene(sca.AbstractScene):

    def __init__(self, screen, _scene_id):
        super().__init__(screen, _scene_id)
        self.exit_button = (350, 350, 20, 20)
        self.mistake_dict = None

    def handle_mistakes(self):
        counter_x = 0
        counter_y = 0
        for item in self.mistake_dict:
            if self.mistake_dict[item] > 0:
                font = pygame.font.Font(None, 25)
                text = font.render(f'{item}: {self.mistake_dict[item]}', 1, (255, 10, 10))
                textpos = text.get_rect()
                textpos.topleft = (10 + (75 * counter_y), 10 + (50 * counter_x))
                self.background.blit(text, textpos)
                counter_x += 1
                if counter_x > 7:
                    counter_x = 0
                    counter_y += 1

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
                    crashed = True

        return crashed, active_scene, scene_info

    def draw(self):
        self.background.fill((255, 255, 255))

        pygame.draw.rect(self.background, (250, 50, 50), self.exit_button)

        self.handle_mistakes()
        return self.background
