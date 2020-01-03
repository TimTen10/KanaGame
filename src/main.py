import pygame
from scenes import GameScene as GS

_SIZE = (800, 600)
_scenes = []
_active_scene_id = 0

def main():
    pygame.init()
    screen = pygame.display.set_mode(_SIZE)
    crashed = False

    # init scenes
    _scenes.append(GS(screen=screen, _scene_id=0))

    _scenes[_active_scene_id].draw()

    while not crashed:

        crashed = _scenes[_active_scene_id].logic()

        background = _scenes[_active_scene_id].draw()
        screen.blit(background, (0, 0))
        pygame.display.flip()

    pygame.quit()
    quit()

if __name__ == '__main__':
    main()
