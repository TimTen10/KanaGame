import pygame
from gamescene import GameScene as GS
from endingscene import EndScene as ES

_SIZE = (400, 400)
_scenes = []

def main():
    pygame.init()
    screen = pygame.display.set_mode(_SIZE)
    pygame.display.set_caption('Hiragana Trainer V1')
    crashed = False

    # init scenes
    _scenes.append(GS(screen=screen, _scene_id=0))
    _scenes.append(ES(screen=screen, _scene_id=1))

    _active_scene_id = 0

    _scenes[_active_scene_id].draw()

    while not crashed:

        crashed, _active_scene_id = _scenes[_active_scene_id].logic()

        background = _scenes[_active_scene_id].draw()
        screen.blit(background, (0, 0))
        pygame.display.flip()

    pygame.quit()
    quit()

if __name__ == '__main__':
    main()
