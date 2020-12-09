import pygame
from random import choice


def lsd_corridor(screen):
    screen.fill((0, 0, 0))
    font = pygame.font.Font("BAUHS93.TTF", 50)
    text = font.render("Welcome to the LSD house!", True, (240, 95, 12))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y - 50))
    pygame.draw.rect(screen, (240, 95, 12), (text_x - 10, text_y - 60,
                                             text_w + 20, text_h + 20), 1)


def lsd_room_1(screen):
    screen.fill((0, 0, 0))
    font = pygame.font.Font("BAUHS93.TTF", 48)
    text = font.render("Loading LSD room 1, please wait...", True, (102, 24, 204))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y - 50))
    pygame.draw.rect(screen, (102, 24, 204), (text_x - 10, text_y - 60,
                                              text_w + 20, text_h + 20), 1)


def lsd_room_2(screen):
    screen.fill((0, 0, 0))
    font = pygame.font.Font("BAUHS93.TTF", 48)
    text = font.render("Loading LSD room 2, please wait...", True, (18, 39, 229))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y - 50))
    pygame.draw.rect(screen, (18, 39, 229), (text_x - 10, text_y - 60,
                                             text_w + 20, text_h + 20), 1)


def lsd_room_3(screen):
    screen.fill((0, 0, 0))
    font = pygame.font.Font("BAUHS93.TTF", 48)
    text = font.render("Loading LSD room 3, please wait...", True, (127, 138, 11))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y - 50))
    pygame.draw.rect(screen, (127, 138, 11), (text_x - 10, text_y - 60,
                                              text_w + 20, text_h + 20), 1)


def main():
    global x_pos, y_pos, width, height
    pygame.init()
    pygame.display.set_caption('New Application')
    size = width, height = 800, 800
    screen = pygame.display.set_mode(size)
    active = True
    while active:
        lsd_corridor(screen)
        pygame.display.flip()
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
                        lsd_room_1(screen)
                        pygame.display.flip()

                elif event.key == pygame.K_2:
                    lsd_2_active = True
                    while lsd_2_active:
                        for event_2 in pygame.event.get():
                            if event_2.type == pygame.QUIT:
                                lsd_2_active = False
                        lsd_room_2(screen)
                        pygame.display.flip()

                elif event.key == pygame.K_3:
                    lsd_3_active = True
                    while lsd_3_active:
                        for event_2 in pygame.event.get():
                            if event_2.type == pygame.QUIT:
                                lsd_3_active = False
                        lsd_room_3(screen)
                        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
