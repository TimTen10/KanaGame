import pygame
from syllables import syl
from menuscene import MenuScene as MS
from gamescene import GameScene as GS
from endingscene import EndScene as ES

_SIZE = (400, 400)
_scenes = []

def main():
    pygame.init()
    screen = pygame.display.set_mode(_SIZE)
    pygame.display.set_caption('Hiragana Trainer')
    crashed = False

    # init scenes
    _scenes.append(MS(screen=screen, _scene_id=0))
    _scenes.append(GS(screen=screen, _scene_id=1, syllables_list = syl))
    _scenes.append(ES(screen=screen, _scene_id=2))

    _active_scene_id = 0

    _scenes[_active_scene_id].draw()

    while not crashed:

        active_scene = _active_scene_id

        crashed, _active_scene_id, scene_info = _scenes[_active_scene_id].logic()

        if active_scene < _active_scene_id and active_scene == 1:
            _scenes[2].mistake_dict = _scenes[1].mistake_dict

        background = _scenes[_active_scene_id].draw()

        screen.blit(background, (0, 0))
        pygame.display.flip()

    pygame.quit()
    quit()

if __name__ == '__main__':
    main()
