import pygame as pg
import random

pg.init()
WIDTH, HEIGHT = 330, 175
window = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Bubble Sort Visualization')

def create(size):
    arr = []
    for i in range(size):
        arr.append(random.randint(0,99))
    return arr

def sort(arr, left, right):
    return arr[left] > arr[right]

def draw_cursor(window, arr, font, left, right):
    txt = pg.font.SysFont('Arial', 15)
    x, y, s = 15, 30, 30

    ts = font.render(str(arr[left]), True, (0, 255, 0))
    window.blit(ts, (x + s*left, y))
    ts = txt.render('compare', True, (0, 0, 0))
    window.blit(ts, (x + s*left, y+y))

    ts = font.render(str(arr[right]), True, (255, 0, 0))
    window.blit(ts, (x + s*right, y))

def draw(window, arr, left, right):
    window.fill((255, 255, 255))
    font = pg.font.SysFont('Arial', 20)
    x, y, s = 15, 30, 30
    for i in range(len(arr)):
        textsurface = font.render(str(arr[i]), True, (0, 0, 0))
        window.blit(textsurface, (x + s*i, y))
    if right < len(arr):
        draw_cursor(window, arr, font, left, right)

def draw_button(window, rect):
    font = pg.font.SysFont('Arial', 20)
    pg.draw.rect(window, (0, 0, 0), rect, 3)
    ts = font.render('Restart', True, (0, 0, 0))
    window.blit(ts, (rect.x+15, rect.y+15))

def main(window):
    running = True
    clock = pg.time.Clock()
    frame, fps = 0, 60
    SIZE = 10
    arr = create(SIZE)
    isSwap, left, right = False, 0, 1
    rect = pg.Rect(115, 100, 100, 50)

    while running:
        clock.tick(fps)
        x, y = pg.mouse.get_pos()

        draw(window, arr, left, right)
        draw_button(window, rect)

        if frame >= fps:
            if right < SIZE:
                if sort(arr, left, right):
                    temp = arr[left]
                    arr[left] = arr[right]
                    arr[right] = temp
                    isSwap = True
                left += 1
                right += 1
            elif isSwap:
                left, right = 0, 1
                isSwap = False
            frame = 0
        else:
            frame += 2

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                break
            if event.type == pg.MOUSEBUTTONDOWN:
                if rect.collidepoint(x, y):
                    arr = create(SIZE)
                    isSwap, left, right = False, 0, 1

        pg.display.update()
    pg.quit()

if __name__ == '__main__':
    main(window)