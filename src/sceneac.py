from abc import ABC, abstractmethod
import pygame

class AbstractScene(ABC):

    def __init__(self, screen, _scene_id):
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        self.background = background
        self._scene_id = _scene_id
        super().__init__()

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def logic(self):
        pass
