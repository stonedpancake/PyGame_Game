import pygame
import pygame_gui
from pygame import *
from pygame_gui import *
from pygame.image import *


class Main:

    def __init__(self):

        init()
        display.set_caption('Sweet House')
        self.size = self.width, self.height = 600, 550

        self.menu_color = '#48C9B0'
        self.chr_btn_color = '#E67E22'
        self.scr_btn_color = '#ED5252'
        self.drm_btn_color = '#EC77E0'

        # self.screen = Surface(self.size)
        self.screen = display.set_mode(self.size)
        self.screen.fill(self.menu_color)
        self.manager = UIManager(self.size)

        self.fps = 60
        self.clock = time.Clock()

        # Set buttons

        self.christmas_main_btn = elements.UIButton(
            relative_rect=Rect((200, 25), (200, 100)),
            text='Christmas',
            manager=self.manager
        )

        self.scary_main_btn = elements.UIButton(
            relative_rect=Rect((200, 225), (200, 100)),
            text='Scary',
            manager=self.manager
        )

        self.dream_main_btn = elements.UIButton(
            relative_rect=Rect((200, 425), (200, 100)),
            text='Dream',
            manager=self.manager
        )

        self.chr_btn_sf = Surface(self.christmas_main_btn.get_abs_rect().size)
        self.chr_btn_sf.fill(self.chr_btn_color)

        self.scr_btn_sf = Surface(self.scary_main_btn.get_abs_rect().size)
        self.scr_btn_sf.fill(self.scr_btn_color)

        self.drm_btn_sf = Surface(self.dream_main_btn.get_abs_rect().size)
        self.drm_btn_sf.fill(self.drm_btn_color)

    def func(self):
        pass

    def start_menu(self):

        time_delta = self.clock.tick(self.fps) / 1000
        exit_ = False

        while not exit_:

            for event_ in pygame.event.get():  # main events

                if event_.type == QUIT:
                    exit_ = True

                elif event_.type == USEREVENT:  # user events

                    if event_.user_type == UI_BUTTON_PRESSED:  # button pressed

                        if event_.ui_element == self.christmas_main_btn:
                            self.screen.fill(self.chr_btn_color)

                        if event_.ui_element == self.scary_main_btn:
                            self.screen.fill(self.scr_btn_color)

                        if event_.ui_element == self.dream_main_btn:
                            self.screen.fill(self.drm_btn_color)

                    if event_.user_type == UI_BUTTON_ON_HOVERED:  # button hovered

                        if event_.ui_element == self.christmas_main_btn:
                            self.screen.blit(self.chr_btn_sf,
                                             (self.christmas_main_btn.get_abs_rect().x,
                                              self.christmas_main_btn.get_abs_rect().y))
                            self.manager.draw_ui(self.screen)
                            display.flip()

                self.manager.process_events(event_)
            self.manager.update(time_delta)

            # self.screen.blit(color, (0, 0))
            self.manager.draw_ui(self.screen)
            display.flip()

        quit()


if __name__ == '__main__':
    Main().start_menu()
