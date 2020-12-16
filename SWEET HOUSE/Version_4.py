import pygame
import pygame_gui
from pygame import *
from pygame_gui import *


class Main:

    def __init__(self):

        init()
        display.set_caption('Sweet House')

        self.size = self.width, self.height = 1920, 1080
        display.set_mode(self.size)

        self.menu_color = '#48C9B0'
        self.chr_btn_color = '#E67E22'
        self.scr_btn_color = '#E67E22'
        self.drm_btn_color = '#E67E22'

        self.screen = Surface(self.size)
        self.screen.fill(Color(self.menu_color))

        self.fps = 60
        self.clock = time.Clock()

    def set_bg_color(self, change_color):
        self.screen.fill(Color(change_color))
        time.delay(2000)

    def start_menu(self):
        exit_ = False

        while not exit_:

            for event_ in pygame.event.get():

                if event_.type == QUIT:
                    exit_ = True

                self.set_bg_color(self.menu_color)
                display.flip()
        quit()


if __name__ == '__main__':
    Main().start_menu()
