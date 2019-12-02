import pygame
from pygame.locals import *
from cell import Cell

def determine_mouseOver(rect, valx, valy):
  if rect.collidepoint(valx, valy):
    return True
  else:
    return False

size = 50
background_colour = (0,0,0)
(width, height) = (1000, 600)
(numx, numy) = (int(width / size), int(height / size))

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Game of Life')
screen.fill(background_colour)
clock = pygame.time.Clock()

# drawing rects
rects = []
for i in range(numx):
  rects.append([])
  for d in range(numy):
    rects[i].append(Cell(pygame.Rect(i * size, d * size, size, size), i, d))

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

  if sim == True:
    for row in rects:
      for rect in row:
        n = ((rect.posx - 1, rect.posy - 1), (rect.posx - 1, rect.posy), (rect.posx - 1, rect.posy + 1),
             (rect.posx, rect.posy - 1), (rect.posx, rect.posy + 1), (rect.posx + 1, rect.posy - 1),
             (rect.posx + 1, rect.posy), (rect.posx + 1, rect.posy + 1))
        for nrow in rects:
          for nrect in nrow:
            for nei in n:
              if (nrect.posx, nrect.posy) == nei and nrect.c == (255,255,255):
                rect.count += 1
            print(rect.count)
            rect.iteration()

    clock.tick(1000)

  for row in rects:
    for rect in row:
      if determine_mouseOver(rect.rect, mousex, mousey) and mouseClicked == True:
        rect.c = (255,255,255)
        pygame.draw.rect(screen, rect.c, rect.rect)
      elif determine_mouseOver(rect.rect, mousex, mousey) and mouseClicked == False and rect.c !=(255,255,255):
        pygame.draw.rect(screen, (125, 125, 125), rect.rect)
      else:
        pygame.draw.rect(screen, rect.c, rect.rect)

  pygame.display.update()
  clock.tick(50)

