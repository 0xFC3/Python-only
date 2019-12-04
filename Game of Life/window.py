import pygame, sys
import random
from pygame.locals import *
from cell import Cell
from Button import Button


def determine_mouseOver(rect, valx, valy):
  if rect.collidepoint(valx, valy):
    return True
  else:
    return False

def mousebuttondown():
  pos = pygame.mouse.get_pos()
  for button in buttons:
    if button.rect.collidepoint(pos):
      button.call_back()

def randomGen(rects):
  for rect in rects:
    if random.randint(0,1) == 0:
      rect.c = (0,0,0)
    else:
      rect.c = (255,255,255)
  return rects

def clear(rects):
  for rect in rects:
    rect.c = (0,0,0)
  return rects

def start(sims):
  global sim
  print('st')
  sim = True
  return sim

def stop(sims):
  global sim
  sim = False
  return sim

def setTime(time):
  global waittime
  waittime = time
  return time

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

running = True
sim = False
waittime = 250

# GUI elements
button01 = Button("RanGen", (1100, 200), randomGen, rects, screen)
button02 = Button("Clear", (1100, 275), clear, rects, screen)
button03 = Button("Start", (1100, 50), start, sim, screen, (0, 125, 0))
button04 = Button("Stopp", (1100, 125), stop, sim, screen, (125, 0, 0))
button05 = Button("1x", (1070, 350), setTime, 250, screen, size=(40, 40))
button06 = Button("2x", (1130, 350), setTime, 125, screen, size=(40, 40))
button07 = Button("4x", (1070, 425), setTime, 50, screen, size=(40, 40))
button08 = Button("8x", (1130, 425), setTime,  1, screen, size=(40, 40))
buttons = [button01, button02, button03, button04, button05, button06, button07, button08]
mousex = 0
mousey = 0


while running:
  mouseClicked = False
  # events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == MOUSEMOTION:
      mousex, mousey = event.pos
    elif event.type == MOUSEBUTTONUP:
      mousex, mousey = event.pos
      mouseClicked = True
      mousebuttondown()

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
    pygame.time.wait(waittime)

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
  for button in buttons:
    button.draw()

  pygame.display.update()
  clock.tick(50)

