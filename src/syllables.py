import os
import pygame
import random

dir_path = os.path.dirname(os.path.realpath(__file__))

syl = [
    'a', 'i', 'u', 'e', 'o',
    'ka', 'ki', 'ku', 'ke', 'ko',
    'sa', 'shi', 'su', 'se', 'so',
    'ta', 'chi', 'tsu', 'te', 'to',
    'na', 'ni', 'nu', 'ne', 'no',
    'ha', 'hi', 'fu', 'he', 'ho',
    'ma', 'mi', 'mu', 'me', 'mo',
    'ya', 'yu', 'yo',
    'ra', 'ri', 'ru', 're', 'ro',
    'wa', 'wo',
    'n'
]

class _Syllable:

    def __init__(self, syllable, kana_image):
        self._syllable = syllable
        self._kana_image = pygame.image.load(kana_image)

        self._xpos = 800 / 2 - 60
        self._ypos = 600 / 2 - 60
        self._spd = 1

    def get_name(self):
        return self._syllable

    def get_image(self):
        return self._kana_image

    def get_pos(self):
        return (self._xpos, self._ypos)

# TODO:
# Create a function that returns syllables like syllables in the last line does,
# but it depends on an input. That input specifies which Kana are in the rotation.

syllables = [_Syllable(x, dir_path + f'/images/syllables/{x.upper()}.png') for x in syl]
