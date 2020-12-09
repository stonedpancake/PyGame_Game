import pygame
from pygame import camera, image, time
from random import choice
from pygame import mixer

# Функция градиента
'''def gradientRect(window, left_colour, right_colour, target_rect):
    """ Draw a horizontal-gradient filled rectangle covering <target_rect> """
    colour_rect = pygame.Surface((2, 2))  # tiny! 2x2 bitmap
    pygame.draw.line(colour_rect, left_colour, (0, 0), (0, 1))  # left colour line
    pygame.draw.line(colour_rect, right_colour, (1, 0), (1, 1))  # right colour line
    colour_rect = pygame.transform.smoothscale(colour_rect, (target_rect.width, target_rect.height))  # stretch!
    window.blit(colour_rect, target_rect)  # paint it'''


class Main:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Sweet house')
        self.size = self.width, self.height = 800, 800
        self.screen = pygame.display.set_mode(self.size)
        self.fps = 6
        self.clock = pygame.time.Clock()
        self.image = image.load("4-19.jpg")

    def lsd_corridor(self):

        self.screen.fill((0, 0, 0))

        font = pygame.font.Font("BAUHS93.TTF", 50)

        text = font.render("Welcome to the Sweet house!", True,
                           (choice(range(255)), choice(range(255)), choice(range(255))))

        text_x = self.width // 2 - text.get_width() // 2
        text_y = self.height // 2 - text.get_height() // 2
        text_w = text.get_width()
        text_h = text.get_height()
        self.screen.blit(text, (text_x, text_y - 50))

        pygame.draw.rect(self.screen, (choice(range(255)), choice(range(255)), choice(range(255))),
                         (text_x - 10, text_y - 60, text_w + 20, text_h + 20), 1)

    def lsd_room_1(self):

        self.screen.fill((0, 0, 0))

        font = pygame.font.Font("BAUHS93.TTF", 48)

        text = font.render("Loading room 1, please wait...", True,
                           (choice(range(255)), choice(range(255)), choice(range(255))))

        text_x = self.width // 2 - text.get_width() // 2
        text_y = self.height // 2 - text.get_height() // 2
        text_w = text.get_width()
        text_h = text.get_height()
        self.screen.blit(text, (text_x, text_y - 50))

        pygame.draw.rect(self.screen, (choice(range(255)), choice(range(255)), choice(range(255))),
                         (text_x - 10, text_y - 60, text_w + 20, text_h + 20), 1)
        self.clock.tick(15)
        # Level().main()

    def lsd_room_2(self):

        self.screen.fill((0, 0, 0))

        font = pygame.font.Font("BAUHS93.TTF", 48)

        text = font.render("Loading room 2, please wait...", True,
                           (choice(range(255)), choice(range(255)), choice(range(255))))

        text_x = self.width // 2 - text.get_width() // 2
        text_y = self.height // 2 - text.get_height() // 2
        text_w = text.get_width()
        text_h = text.get_height()
        self.screen.blit(text, (text_x, text_y - 50))

        pygame.draw.rect(self.screen, (choice(range(255)), choice(range(255)), choice(range(255))),
                         (text_x - 10, text_y - 60, text_w + 20, text_h + 20), 1)

    def lsd_room_3(self):

        self.screen.fill((0, 0, 0))

        font = pygame.font.Font("BAUHS93.TTF", 48)

        text = font.render("Loading room 3, please wait...", True,
                           (choice(range(255)), choice(range(255)), choice(range(255))))

        text_x = self.width // 2 - text.get_width() // 2
        text_y = self.height // 2 - text.get_height() // 2
        text_w = text.get_width()
        text_h = text.get_height()
        self.screen.blit(text, (text_x, text_y - 50))

        pygame.draw.rect(self.screen, (choice(range(255)), choice(range(255)), choice(range(255))),
                         (text_x - 10, text_y - 60, text_w + 20, text_h + 20), 1)

    def main(self):

        active = True
        while active:

            # Вызов отрисовки корридора

            self.lsd_corridor()
            self.clock.tick(self.fps)
            pygame.display.flip()

            # Основной цикл

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    active = False

                elif event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_1:

                        lsd_1_active = True

                        while lsd_1_active:

                            for event_2 in pygame.event.get():

                                if event_2.type == pygame.QUIT:
                                    lsd_1_active = False

                            # Вызов отрисовки 1-й комнаты

                            self.lsd_room_1()
                            self.clock.tick(self.fps)
                            pygame.display.flip()

                            # Вызов отрисовки 1-ого уровня

                            time.delay(2000)

                            Level().first_level()
                            pygame.display.flip()
                            # time.delay(30000)

                    elif event.key == pygame.K_2:

                        start_ticks = time.get_ticks()  # starter tick

                        lsd_2_active = True

                        while lsd_2_active:

                            for event_2 in pygame.event.get():

                                if event_2.type == pygame.QUIT:
                                    lsd_2_active = False

                            # Вызов отрисовки 2-й комнаты

                            self.lsd_room_2()
                            self.clock.tick(self.fps)
                            pygame.display.flip()

                            # Вызов отрисовки 2-ого уровня

                            seconds = (time.get_ticks() - start_ticks) / 1000  # calculate how many seconds
                            if seconds > 2:
                                Level().second_level()
                                pygame.display.flip()

                    elif event.key == pygame.K_3:

                        start_ticks = time.get_ticks()  # starter tick

                        lsd_3_active = True

                        while lsd_3_active:
                            for event_2 in pygame.event.get():
                                if event_2.type == pygame.QUIT:
                                    lsd_3_active = False

                            # Вызов отрисовки 3-й комнаты

                            self.lsd_room_3()
                            self.clock.tick(self.fps)
                            pygame.display.flip()

                            # Вызов отрисовки 3-его уровня

                            seconds = (time.get_ticks() - start_ticks) / 1000  # calculate how many seconds
                            if seconds > 2:
                                Level().third_level()
                                pygame.display.flip()
        pygame.quit()


class Rooms(Main):
    class ScaryRoom(Main):
        def __init__(self):
            super().__init__()
            print('hi')

        def first_level(self):
            self.screen.fill((0, 0, 0))

            mixer.music.load("Song_1.mp3")
            mixer.music.play()

            time.delay(30000)

    class ChristmasRoom(Main):
        def __init__(self):
            super().__init__()
            print('hi')

        def first_level(self):
            self.screen.fill((0, 0, 0))

            mixer.music.load("Song_1.mp3")
            mixer.music.play()

            time.delay(30000)

    class DreamsRoom(Main):
        def __init__(self):
            super().__init__()
            print('hi')

        def first_level(self):
            self.screen.fill((0, 0, 0))

            mixer.music.load("Song_1.mp3")
            mixer.music.play()

            time.delay(30000)

    def main(self):
        active = True
        while active:

            # Основной цикл

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    active = False

                elif event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_1:
                        pass

                    elif event.key == pygame.K_2:
                        pass

                    elif event.key == pygame.K_3:
                        pass
        pygame.quit()


if __name__ == '__main__':
    Main().main()
