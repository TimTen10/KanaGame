import pygame
import random
import syllables as syl

_SIZE = (800, 600)

def main():

    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode(_SIZE)
    pygame.display.set_caption('Hiragana Trainer')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    clock = pygame.time.Clock()

    crashed = False

    # Scoretext on the display
    right, wrong = 0, 0
    def handle_score():
        font = pygame.font.Font(None, 36)
        text = font.render(f"Right: {right} and Wrong: {wrong}", 1, (255, 10, 10))
        textpos = text.get_rect()
        textpos.centerx = background.get_rect().centerx
        background.blit(text, textpos)

    def init_type_syl():
        return random.choice(syl.syllables)

    # Variables
    type_syl = init_type_syl()
    floating_sil = ""
    locked_sil = ""

    def handle_syllables():
        background.blit(type_syl.get_image(), type_syl.get_pos())
        font = pygame.font.Font(None, 36)
        text = font.render(f"{floating_sil}", 1, (255, 10, 10))
        background.blit(text, (380, 500))

    def draw_window():
        background.fill((255, 255, 255)) # Erases everything old
        handle_score()
        handle_syllables()
        screen.blit(background, (0, 0))
        pygame.display.flip()

    # Blit everything to the screen
    draw_window()

    while not crashed:

        for event in pygame.event.get():

            print(event)

            if event.type == pygame.QUIT:
                crashed = True

            if event.type == pygame.KEYDOWN:
                # lock the current floating syllable as the answer to the current kana.
                if event.dict['unicode'] == ' ' or event.dict['unicode'] == '\r':
                    locked_sil = floating_sil.strip()
                    floating_sil = ""

                    if type_syl.get_name() == locked_sil:
                        right += 1
                        type_syl = init_type_syl()
                    else:
                        wrong += 1
                # delete the last letter typed.
                elif event.dict['unicode'] == '\x08':
                    floating_sil = floating_sil[:-1]
                # add the given letter to the answer string.
                else:
                    floating_sil += event.dict['unicode']

            print(f"Floating syl: {floating_sil} and Locked syl: {locked_sil} and to type: {type_syl.get_name()}")

        draw_window()

        clock.tick(60)

    pygame.quit()
    quit()

if __name__ == '__main__':
    main()
