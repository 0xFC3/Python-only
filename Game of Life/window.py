import pygame
import random
from pygame.locals import *
from cell import Cell


def determine_mouseOver(rect, valx, valy):
  if rect.collidepoint(valx, valy):
    return True
  else:
    return False

def randomGen(rects):
  for rect in rects:
    if random.randint(0,1) == 0:
      rect.c = (0,0,0)
    else:
      rect.c = (255,255,255)
  return rects

size = 25
background_colour = (0,0,0)
(width, height) = (1200, 600)
(numx, numy) = (int((width - 200) / size), int(height / size))

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Game of Life')
screen.fill(background_colour)
clock = pygame.time.Clock()

# drawing rects
rects = []
for d in range(numy):
  for i in range(numx):
    rects.append(Cell(pygame.Rect(i * size, d * size, size, size), i, d))

# GUI elements
ranGen = pygame.Rect(1050, 200, 100, 50)
guiBack = pygame.Rect(1000,0,200,600)
mousex = 0
mousey = 0

running = True
sim = False
while running:
  mouseClicked = False
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == MOUSEMOTION:
      mousex, mousey = event.pos
    elif event.type == MOUSEBUTTONUP:
      mousex, mousey = event.pos
      mouseClicked = True
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        sim = False
      if event.key == pygame.K_RIGHT:
        sim = True

  # the simulation
  if sim == True:
    for rect in rects:
      n = ((rect.posx - 1, rect.posy - 1), (rect.posx - 1, rect.posy), (rect.posx - 1, rect.posy + 1),
           (rect.posx, rect.posy - 1), (rect.posx, rect.posy + 1), (rect.posx + 1, rect.posy - 1),
           (rect.posx + 1, rect.posy), (rect.posx + 1, rect.posy + 1))

      for i in range((rect.posy - 1) * numx, (rect.posy + 2) * numx):
        try:
          for nei in n:
            if (rects[i].posx, rects[i].posy) == nei and rects[i].c == (255, 255, 255):
              rect.count += 1
              continue
        except: continue
      rect.iteration()
    for rect in rects:
      rect.c = rect.cnew
    pygame.time.wait(250)

  # modefying the rects
  for rect in rects:
    if determine_mouseOver(rect.rect, mousex, mousey) and mouseClicked == True:
      rect.c = (255,255,255)
      pygame.draw.rect(screen, rect.c, rect.rect)
    elif determine_mouseOver(rect.rect, mousex, mousey) and mouseClicked == False and rect.c !=(255,255,255):
      pygame.draw.rect(screen, (125, 125, 125), rect.rect)
    else:
      pygame.draw.rect(screen, rect.c, rect.rect)

  # GUI elements
  pygame.draw.rect(screen, (0, 255, 0), guiBack)
  if determine_mouseOver(ranGen, mousex, mousey) and mouseClicked == True:
    randomGen(rects)
  pygame.draw.rect(screen, (255, 0,0), ranGen)
  pygame.display.update()
  clock.tick(50)

