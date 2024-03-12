import pygame
import random

'''↓↓↓ YOUR CODE HERE ↓↓↓'''
screen_width = 700
screen_hight = 700
'''↑↑↑ YOUR CODE HERE ↑↑↑'''

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_hight))
done = False

'''↓↓↓ YOUR CODE HERE ↓↓↓'''
number_of_stars = 100
speed = 0.5
stars = []
'''↑↑↑ YOUR CODE HERE ↑↑↑'''


def new_star() -> list:
    star = [random.randint(0, screen_width) - screen_width // 2, random.randint(0, screen_hight) - screen_hight // 2, 256, 0]
    return star

for i in range(0, number_of_stars):
    stars.append(new_star())

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((0, 0, 0))

    for i in range(0, number_of_stars):
        s = stars[i]

        x = s[0] * 256 / s[2]
        y = s[1] * 256 / s[2]
        s[2] -= speed

        if s[2] <= 0 or x <= -screen_width // 2 or x >= screen_width // 2 or y <= -screen_hight // 2 or y >= screen_hight // 2:
            s = new_star()

        if s[3] < 256:
            s[3] += 0.15

        if s[3] >= 256:
            s[3] = 255

        stars[i] = s

        x = round(s[0] * 256 / s[2]) + screen_width // 2
        y = round(s[1] * 256 / s[2]) + screen_hight // 2

        import random

        a = lambda: random.randint(0, 255)
        colors = '#%02X%02X%02X' % (a(), a(), a())


        pygame.draw.circle(screen, colors, (x, y), 3)

    pygame.display.flip()
pygame.quit()
