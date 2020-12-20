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

        self.error_sound = './Materials/Bg Pictures/erro.mp3'

        # mixer.Sound(self.error_sound)

    def menu(self):

        self.menu_surface.blit(self.menu_image, (0, 0))
        self.menu_screen.blit(self.menu_surface, (0, 0))

    def main_loop(self):

        exit_ = False

        while not exit_:

            self.menu()
            display.flip()

            for event_ in pygame.event.get():  # main events

                if event_.type == QUIT:
                    exit_ = True

                if event_.type == MOUSEBUTTONDOWN:

                    mixer.music.load('./Materials/Bg Pictures/erro.mp3')
                    mixer.music.play()

                    exit_2 = False

                    while not exit_2:

                        StartGame().level_1()
                        display.flip()

                        for event_2 in pygame.event.get():  # main events

                            if event_2.type == QUIT:
                                exit_ = True


class StartGame:

    def __init__(self):
        self.level_1_screen = display.set_mode(SIZE)
        self.level_1_surface = Surface(SIZE)

        self.windows_error = image.load('./Materials/Bg Pictures/bsod_2.jpg')

    def level_1(self):
        self.level_1_surface.blit(self.windows_error, (0, 0))
        self.level_1_screen.blit(self.level_1_surface, (0, 0))

    def main_loop(self):
        exit_ = False

        while not exit_:
            self.level_1()
            display.flip()


if __name__ == '__main__':
    Menu().main_loop()
