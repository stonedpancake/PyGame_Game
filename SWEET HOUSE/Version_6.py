import pygame
import pygame_gui
from pygame import *
from pygame_gui import *
from pygame.image import *

SIZE = WIDTH, HEIGHT = 1920, 1080


class Menu:

    def __init__(self):

        init()
        display.set_caption('Sweet House')

        self.menu_screen = display.set_mode(SIZE)

        self.menu_image = image.load('./Materials/Bg Pictures/image.png')
        self.menu_surface = Surface(SIZE)

        self.level_1_surface = Surface(SIZE)
        self.spaceship = image.load('./Materials/Bg Pictures/spaceship.png')

    def menu(self):

        self.menu_surface.blit(self.menu_image, (0, 0))
        self.menu_screen.blit(self.menu_surface, (0, 0))

    def start_game(self):

        self.level_1_surface.blit(self.spaceship, (0, 0))
        self.menu_screen.blit(self.level_1_surface, (0, 0))

    def main_loop(self):

        exit_ = False

        while not exit_:

            self.menu()
            display.flip()

            for event_ in pygame.event.get():  # main events

                if event_.type == QUIT:
                    exit_ = True

                if event_.type == MOUSEBUTTONDOWN:
                    self.start_game()
                    display.flip()
                    # StartGame().level_1()


'''class StartGame:

    def __init__(self):

        # self.level_1_screen = display.set_mode(SIZE)
        self.level_1_surface = Surface(SIZE)

        self.spaceship = image.load('./Materials/Bg Pictures/spaceship.png')

    def level_1(self):

        self.level_1_surface.blit(self.spaceship, (0, 0))
        # self.level_1_screen.blit(self.level_1_surface, (0, 0))

    def main_loop(self):

        exit_ = False

        while not exit_:

            self.level_1()
            display.flip()
'''

if __name__ == '__main__':
    Menu().main_loop()
