import pygame
from mymap import Map2
import random

random.seed(1)

def floodfill():
    groups = []

    while not all(all(l) for l in map.map):
        start = None
        for y, row in enumerate(map.map):
            done = True
            for x, v in enumerate(row):
                if not map.map[y][x]:
                    start = [x, y]
                    break
            else:
                done = False
            if done:
                break
        open_set = set([tuple(start)])
        # tuples are like lists (list == array in most other languages)
        # except tuples cannot have their items changed. Look up how
        # sets and dictionaries work if you want to understand why it
        # needs to have tuples not lists.
        
        closed_set = set()
        while len(open_set) > 0:
            draw(open_set, closed_set, groups)
            # It should return out of the while loop before then, but just in case there isn't
            # a path.

            new_open_set = set()
            for o in open_set:
                for n in map.get(o):
                    if map.map[n[1]][n[0]]:
                        continue

                    map.map[n[1]][n[0]] = True
                    new_open_set.add(tuple(n))
                    
            closed_set |= open_set
            open_set = new_open_set
        
        groups.append(closed_set)
    
    draw(open_set, closed_set, groups)
    return groups

global colors
colors = [[random.randint(0, 255) for i in range(3)] for j in range(100)]
def draw(open_set, closed_set, groups):
    pygame.time.delay(250)
    reset()
    for pos in open_set:
        rect.x = pos[0]*50
        rect.y = pos[1]*50
        screen.fill((255, 255, 0), rect)
    for pos in closed_set:
        rect.x = pos[0]*50
        rect.y = pos[1]*50
        screen.blit(closedsurf, rect)
    for color, group in zip(colors[:len(groups)], groups):
        for pos in group:
            rect.x = pos[0]*50
            rect.y = pos[1]*50
            screen.fill(color, rect)
    
    pygame.display.update()
    pygame.event.pump()

def draw_path(pos):
    pygame.time.delay(100)
    rect.x = pos[0]*50
    rect.y = pos[1]*50
    screen.fill((0, 0, 255), rect)
    pygame.display.update()
    pygame.event.pump()

def reset():
    screen.blit(mapsurf, (0, 0))
    

global map, screen, rect, surf, mapsurf, closedsurf
map = Map2()
screen = pygame.display.set_mode((500, 500))
rect = pygame.Rect(0, 0, 50, 50)
surf = pygame.Surface((50, 50))
surf.fill((0, 0, 255))
closedsurf = pygame.Surface((50, 50))
closedsurf.fill((255, 0, 0))
for x in range(20):
    pygame.draw.line(closedsurf, (0, 0, 0), (5*x, 0), (0, 5*x))
    pygame.draw.line(closedsurf, (0, 0, 0), (50-5*x, 0), (50, 5*x))
    pygame.draw.rect(closedsurf, (0, 0, 0), (0, 0, 50, 50), 1)

mapsurf = pygame.Surface((500, 500))
mapsurf.fill((255, 255, 255))
for y, row in enumerate(map.map):
    for x, value in enumerate(row):
        if value == 1:
            rect.x = x*50
            rect.y = y*50
            mapsurf.fill((0, 0, 0), rect)

reset()
pygame.display.update()

floodfill()

