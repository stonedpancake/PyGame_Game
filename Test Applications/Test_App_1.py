import pygame
from random import choice

x_pos = 0
y_pos = 0

x_pos_2 = 800
y_pos_2 = 0


def draw(screen):
    global x_pos, y_pos, x_pos_2, y_pos_2
    screen.fill((0, 0, 0))

    for i in range(8):
        color = (choice(range(255)), choice(range(255)), choice(range(255)))
        pygame.draw.circle(screen, color, (x_pos % 800, y_pos % 800), 20)
        x_pos += 100
        y_pos += 100

    for i in range(8):
        color = (choice(range(255)), choice(range(255)), choice(range(255)))
        pygame.draw.circle(screen, color, (x_pos_2 % 800, y_pos_2 % 800), 20)
        x_pos_2 -= 100
        y_pos_2 += 100


def main():
    global x_pos, y_pos, x_pos_2, y_pos_2
    pygame.init()
    pygame.display.set_caption('New Application')
    size = (800, 800)
    screen = pygame.display.set_mode(size)
    v = 30
    fps = 60
    clock = pygame.time.Clock()
    active = True
    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
            '''elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_pos -= 5
                elif event.key == pygame.K_RIGHT:
                    x_pos += 5
                elif event.key == pygame.K_UP:
                    y_pos -= 5
                elif event.key == pygame.K_DOWN:
                    y_pos += 5'''
        draw(screen)
        x_pos += v / fps
        y_pos += v / fps
        x_pos_2 -= v / fps
        y_pos_2 += v / fps
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
