# Changing color
# speed = 0
# for i in range(img.size[0]):
#     for j in range(img.size[1]):
#         if pixels[i, j] == colors.BLACK:  # if pixel in location i, j is red
#             pixels[i, j] = colors.WHITE  # change it to green
#             speed+=1
#             if speed == 5: # Controls how fast to turn the pixel color
#                 speed = 0
#                 break


#data = numpy.asarray(img, dtype="int32")
#numpy.set_printoptions(threshold=sys.maxsize)
#c=0
# #for i in data:
#     for j in i:
#         if(j[0] == 255):
#             c=c+1
# print(c)


# vacuum_big = pygame.image.load("img/vacuum.png")
# vacuum = pygame.transform.smoothscale(vacuum_big, (50, 30))
# vacuum_rect = pygame.Rect(340, 5, 50, 40)
# window.blit(vacuum, vacuum_rect)
# pygame.draw.rect(window, colors.BLACK, vacuum_rect, 3)

# Tried to show a preview/hover of cursor
# if not draw:
#     surface = pygame.Surface((displayX, displayY - 100))
#     surface.blit(window, (0, 0), (0, 100, 500, 400))
#     pos = pygame.mouse.get_pos()
#     if (pos[1] > 105):
#         pygame.draw.circle(window, color, (pos[0], pos[1]), 10, 1)

