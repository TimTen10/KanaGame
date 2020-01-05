import sceneac as sca
import pygame
import random
import syllables as sy

class GameScene(sca.AbstractScene):

    def __init__(self, screen, _scene_id, syllables_list):
        super().__init__(screen, _scene_id)
        self.right = 0
        self.wrong = 0
        self.game_syllables = sy.get_syllables(syllables_list)
        self.type_syl = random.choice(self.game_syllables)
        self.floating_syl = ""
        self.locked_syl = ""
        self.exit_button = (350, 350, 20, 20)
        self.mistake_dict = dict()

        for syl in self.game_syllables:
            self.mistake_dict[syl.get_name()] = 0

    def handle_score(self):
        font = pygame.font.Font(None, 36)
        text = font.render(f"Right: {self.right} and Wrong: {self.wrong}", 1, (255, 10, 10))
        textpos = text.get_rect()
        textpos.centerx = self.background.get_rect().centerx
        self.background.blit(text, textpos)

    def handle_syllables(self):
        self.background.blit(self.type_syl.get_image(), self.type_syl.get_pos())
        font = pygame.font.Font(None, 36)
        text = font.render(f"{self.floating_syl}", 1, (255, 10, 10))
        self.background.blit(text, (185, 350))

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
                    active_scene = 2
                    scene_info = self.mistake_dict

            if event.type == pygame.KEYDOWN:
                # lock the current floating syllable as the answer to the current kana.
                if event.dict['unicode'] == ' ' or event.dict['unicode'] == '\r':
                    self.locked_syl = self.floating_syl.strip()
                    self.floating_syl = ""

                    if self.type_syl.get_name() == self.locked_syl:
                        self.right += 1
                        self.type_syl = random.choice(sy.syllables)
                    else:
                        self.wrong += 1
                        self.mistake_dict[self.type_syl.get_name()] += 1
                # delete the last letter typed.
                elif event.dict['unicode'] == '\x08':
                    self.floating_syl = self.floating_syl[:-1]
                # add the given letter to the answer string.
                else:
                    self.floating_syl += event.dict['unicode']

        return crashed, active_scene, scene_info


    def draw(self):
        self.background.fill((255, 255, 255))

        pygame.draw.rect(self.background, (255, 50, 50), self.exit_button)

        self.handle_score()
        self.handle_syllables()
        return self.background
