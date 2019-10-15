from tkinter import *
from tkinter import messagebox
Tk().wm_withdraw()  # to hide the main window
import pygame
from PIL import Image
#import numpy
import sys
import collections
import colors
import tkinter
import os

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
neverDrew = True

#pygame.draw.rect(window, colors.BLACK, (0, 100, displayX, 100))

font = pygame.font.Font("fonts/theboldfont.ttf", 34) #Load font object.
smallerFont = pygame.font.Font("fonts/theboldfont.ttf", 20) #Load font object.

def drawingMode():
    window.fill(colors.BLACK)
    if os.path.exists('img/PaintImage.png'):
        img = Image.open("img/PaintImage.png")
        image = pygame.image.fromstring(img.tobytes(), img.size, img.mode)
        imageRect = image.get_rect()
        window.blit(image, (0, 100))
    global run, draw, color, neverDrew

    vacuum_text = font.render("Map Draw Mode", True, colors.WHITE)
    map_text = font.render("Map Draw", True, colors.WHITE)
    pygame.draw.rect(window, colors.ORANGE, (0, 0, displayX, 100))
    pygame.draw.rect(window, colors.PURPLE, (0, 0, displayX, 50))

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

    next_text = smallerFont.render(" Next", True, colors.WHITE)
    next_rect = pygame.Rect(420, 10, 52, 30)
    pygame.draw.rect(window, colors.BLACK, next_rect, 3)
    window.blit(next_text, (420, 15))

    window.blit(vacuum_text, (5, 60))
    # window.blit(map_text, (15, 25))
    savedMode = False
    while run:
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

        if savedMode:
            neverDrew = False
            break

    clock.tick(60)

if neverDrew:
    drawingMode()

##### SAVED IMAGE! #####

#### LOADING IMAGE! ####

img = Image.open("img/PaintImage.png")
pixels = img.load()

newWindow = pygame.display.set_mode((displayX, displayY))
pygame.display.set_caption("Running Algorithm")

pygame.draw.rect(window, colors.ORANGE, (0, 0, displayX, 100))
map_text = font.render("Running Algorithm", True, colors.WHITE)
#window.blit(vacuum_text, (5, 5))
window.blit(map_text, (15, 25))

start_text = smallerFont.render(" Start", True, colors.WHITE)
start_rect = pygame.Rect(430, 50, 62, 25)
pygame.draw.rect(window, colors.BLACK, start_rect, 3)
window.blit(start_text, (430, 55))

back_text = smallerFont.render(" Back", True, colors.WHITE)
back_rect = pygame.Rect(360, 50, 62, 25)
pygame.draw.rect(window, colors.BLACK, back_rect, 3)
window.blit(back_text, (360, 55))

image = pygame.image.fromstring(img.tobytes(), img.size, img.mode)
imageRect = image.get_rect()
newWindow.blit(image, (0, 100))

vacuum_big = pygame.image.load("img/vacuum.png")
vacuum = pygame.transform.smoothscale(vacuum_big, (50, 30))

def setupAgain():
    global img, newWindow, map_ext, start_text, map_text, start_rect, back_rect, image_rect, image, back_text, pixels, vacuum, imageRect, vacuum_big
    window.fill(colors.BLACK)
    img = Image.open("img/PaintImage.png")
    pixels = img.load()

    newWindow = pygame.display.set_mode((displayX, displayY))
    pygame.display.set_caption("Running Algorithm")

    pygame.draw.rect(window, colors.ORANGE, (0, 0, displayX, 100))
    map_text = font.render("Running Algorithm", True, colors.WHITE)
    # window.blit(vacuum_text, (5, 5))
    window.blit(map_text, (15, 25))

    start_text = smallerFont.render(" Start", True, colors.WHITE)
    start_rect = pygame.Rect(430, 50, 62, 25)
    pygame.draw.rect(window, colors.BLACK, start_rect, 3)
    window.blit(start_text, (430, 55))

    back_text = smallerFont.render(" Back", True, colors.WHITE)
    back_rect = pygame.Rect(360, 50, 62, 25)
    pygame.draw.rect(window, colors.BLACK, back_rect, 3)
    window.blit(back_text, (360, 55))

    image = pygame.image.fromstring(img.tobytes(), img.size, img.mode)
    imageRect = image.get_rect()
    newWindow.blit(image, (0, 100))

    vacuum_big = pygame.image.load("img/vacuum.png")
    vacuum = pygame.transform.smoothscale(vacuum_big, (50, 30))

placingVacuumMode = True
draw = False
havePlacedVacuum = False
backToDrawing = False
start = (0, 0)

while placingVacuumMode:

    if backToDrawing:
        backToDrawing = False
        drawingMode()
        setupAgain()

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

        if back_rect.collidepoint(pos):
            print("Clicked back")
            backToDrawing = True

        if pos[1]>105:
            newWindow.blit(image, (0, 100))
            newWindow.blit(vacuum, (pos[0]-10, pos[1]-10))
            start = pos[0], pos[1]-105
            havePlacedVacuum = True

    clock.tick(60)

width, height = displayX, displayY-100
queue = collections.deque([[start]])
bfsRunSpeed = 500

while run:

    image = pygame.image.fromstring(img.tobytes(), img.size, img.mode)
    newWindow.blit(image, (0, 100))

    # BFS
    if len(queue) > 0:
        speed = 0
        while(speed < bfsRunSpeed and queue):
            speed += 1
            path = queue.popleft()
            x, y = path[-1]

            #for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1), (x+1, y+1), (x-1, y-1), (x+1, y-1), (x-1, y+1)):
                if 0 <= x2 < width and 0 <= y2 < height and (x2, y2):

                    if pixels[x2, y2] == colors.BLACK:
                        queue.append(path + [(x2, y2)])
                        pixels[x2, y2] = colors.GREY

                    elif pixels[x2, y2] == colors.BROWN:
                        queue.append(path + [(x2, y2)])
                        pixels[x2, y2] = colors.GREY
                        newWindow.blit(vacuum, (x2 - 10, y2 + 75))

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()
    clock.tick(60)
