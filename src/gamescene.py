import sceneac as sca
import pygame
import random
import syllables as sy

class GameScene(sca.AbstractScene):

    def __init__(self, screen, _scene_id):
        super().__init__(screen, _scene_id)
        self.right = 0
        self.wrong = 0
        self.type_syl = random.choice(sy.syllables)
        self.floating_syl = ""
        self.locked_syl = ""

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
        self.background.blit(text, (380, 500))

    def logic(self):
        crashed = False

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                crashed = True

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
                # delete the last letter typed.
                elif event.dict['unicode'] == '\x08':
                    self.floating_syl = self.floating_syl[:-1]
                # add the given letter to the answer string.
                else:
                    self.floating_syl += event.dict['unicode']

        return crashed


    def draw(self):
        self.background.fill((255, 255, 255))
        self.handle_score()
        self.handle_syllables()
        return self.background
