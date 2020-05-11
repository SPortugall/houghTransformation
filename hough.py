from sys import exit
import numpy as np
import pygame

Screen_Width = 800
Screen_Height = 400
GRAY = pygame.Color(128, 128, 128)
BLACK = pygame.Color(0, 0, 0)
GREEN = pygame.Color(0, 255, 0)


def get_angles(step_size):
    return list(np.arange(0, 180, step_size))

def akkumulatePoint(x, y):
    if x < 0 or y < 0:
        return

    # houghRaum is represented by pygame screen

    for a in angles:
        a_r = np.deg2rad(a)
        d = x * np.cos(a_r) + y * np.sin(a_r)
        # draw (a,d) ++

        s = a + (Screen_Width * 0.75)
        s = int(s)
        r = Screen_Height - d
        r = int(r)
        if 0 < r < Screen_Height:
            if 500 <= s < Screen_Width:
                color = screen.get_at((s, r))
                # count color towards white
                if color[0] + 20 <= 255:
                    color[0] += 10
                pygame.draw.circle(screen, color, (s, r), 1)


pygame.init()
pygame.display.set_caption("Hough-Transformation")
screen = pygame.display.set_mode((Screen_Width, Screen_Height))
screen.fill(BLACK)


# divider line
pygame.draw.line(screen, GREEN, (Screen_Width / 2, 0), (Screen_Width / 2, Screen_Height), 5)
pygame.display.flip()
pygame.display.update()

angle_step_size_in_degrees = 1
angles = get_angles(angle_step_size_in_degrees)

running = True
while running:
    # get all events
    ev = pygame.event.get()

    # proceed events
    for event in ev:
        # handle MOUSEBUTTONUP
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print(pos)
            pygame.draw.circle(screen, GRAY, pos, 2)
            akkumulatePoint(pos[0], pos[1])
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.flip()
    pygame.display.update()
