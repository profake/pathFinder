from tkinter import *
from tkinter import messagebox
Tk().wm_withdraw()  # to hide the main window
import pygame
from PIL import Image
import numpy
import sys
import collections
import colors
import tkinter

pygame.init()

displayX = 500
displayY = 500
topMenuBarSize = 100

window = pygame.display.set_mode((displayX, displayY))
pygame.display.set_caption("Vacuum Cleaner")
run = True
color = colors.BLACK
pos = (0, 0)
clock = pygame.time.Clock()
draw = False
#pygame.draw.rect(window, colors.BLACK, (0, 100, displayX, 100))
pygame.draw.rect(window, colors.WHITE, (0, 0, displayX, 100))

font = pygame.font.SysFont("Ubuntu", 18, bold=True)
vacuum_text = font.render("Vacuum Cleaner", True, colors.RED)
map_text = font.render("Map Draw", True, colors.RED)

eraser_big = pygame.image.load("img/eraser.png")
eraser = pygame.transform.smoothscale(eraser_big, (50, 30))
eraser_rect = pygame.Rect(250, 5, 50, 40)
pygame.draw.rect(window, colors.BLACK, eraser_rect, 3)
window.blit(eraser, eraser_rect)

paintBrush_big = pygame.image.load("img/paintbrush.png")
paintBrush = pygame.transform.smoothscale(paintBrush_big, (40, 30))
paintBrush_rect = pygame.Rect(310, 5, 40, 40)
pygame.draw.rect(window, colors.BLACK, paintBrush_rect, 3)
window.blit(paintBrush, paintBrush_rect)

dirt_big = pygame.image.load("img/dirt.png")
dirt = pygame.transform.smoothscale(dirt_big, (40, 30))
dirt_rect = pygame.Rect(360, 5, 40, 40)
pygame.draw.rect(window, colors.BLACK, dirt_rect, 3)
window.blit(dirt, dirt_rect)

next_text = font.render(" Next", True, colors.RED)
next_rect = pygame.Rect(420, 10, 50, 25)
pygame.draw.rect(window, colors.BLACK, next_rect, 3)
window.blit(next_text, next_rect)

window.blit(vacuum_text, (5, 5))
window.blit(map_text, (15, 25))
savedMode = False

while(run):
    #pygame.time.delay(100)
    pygame.display.update()

    if paintBrush_rect.collidepoint(pygame.mouse.get_pos()):
        color = colors.RED
    if eraser_rect.collidepoint(pygame.mouse.get_pos()):
        color = colors.BLACK
    if dirt_rect.collidepoint(pygame.mouse.get_pos()):
        color = colors.BROWN

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            draw = True
        if event.type == pygame.MOUSEBUTTONUP:
            draw = False

    if draw and not savedMode:

        pos = pygame.mouse.get_pos()
        if(pos[1]>105):
            pygame.draw.circle(window, color, (pos[0], pos[1]), 10)

        if next_rect.collidepoint(pos):
            print("Clicked next")
            save_surface = pygame.Surface((displayX, displayY-100))
            save_surface.blit(window, (0, 0), (0, 100, 500, 400))
            pygame.image.save(save_surface, "img/PaintImage.png")
            savedMode = True

    if (savedMode):
        break
clock.tick(60)

##### SAVED IMAGE! #####

#### LOADING IMAGE! ####

img = Image.open("img/PaintImage.png")
pixels = img.load()

newWindow = pygame.display.set_mode((displayX, displayY))
pygame.display.set_caption("Running Algorithm")

pygame.draw.rect(window, colors.WHITE, (0, 0, displayX, 100))
map_text = font.render("Running Algorithm", True, colors.RED)
window.blit(vacuum_text, (5, 5))
window.blit(map_text, (15, 25))

start_text = font.render(" Start", True, colors.RED)
start_rect = pygame.Rect(420, 50, 50, 25)
pygame.draw.rect(window, colors.BLACK, start_rect, 3)
window.blit(start_text, start_rect)

image = pygame.image.fromstring(img.tobytes(), img.size, img.mode)
imageRect = image.get_rect()
newWindow.blit(image, (0, 100))

vacuum_big = pygame.image.load("img/vacuum.png")
vacuum = pygame.transform.smoothscale(vacuum_big, (50, 30))

placingVacuumMode = True
draw = False
havePlacedVacuum = False
start = (0, 0)

while placingVacuumMode :
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            draw = True
        if event.type == pygame.MOUSEBUTTONUP:
            draw = False

    if draw:
        pos = pygame.mouse.get_pos()
        if start_rect.collidepoint(pos):
            print("Clicked start")
            if havePlacedVacuum:
                placingVacuumMode = False
            else:
                tkinter.messagebox.showinfo('Warning', 'Please place a vacuum cleaner')

        if pos[1]>105:
            newWindow.blit(image, (0, 100))
            newWindow.blit(vacuum, (pos[0]-10, pos[1]-10))
            start = pos[0], pos[1]-105
            havePlacedVacuum = True

    clock.tick(60)

width, height = displayX, displayY-100
queue = collections.deque([[start]])
print(start)

while run:

    image = pygame.image.fromstring(img.tobytes(), img.size, img.mode)
    newWindow.blit(image, (0, 100))

    # BFS
    if len(queue) > 0:
        speed = 0
        while(speed < 500 and queue):
            speed += 1
            path = queue.popleft()
            x, y = path[-1]

            #for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1), (x+1, y+1), (x-1, y-1), (x+1, y-1), (x-1, y+1)):
                if 0 <= x2 < width and 0 <= y2 < height:
                    if pixels[x2, y2] == colors.BLACK:
                        queue.append(path + [(x2, y2)])
                        pixels[x2, y2] = colors.GREY
                    elif pixels[x2, y2] == colors.BROWN:
                        queue.append(path + [(x2, y2)])
                        pixels[x2, y2] = colors.GREEN



    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()
    clock.tick(60)
