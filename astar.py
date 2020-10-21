import pygame
from mymap import Map
import bisect
import time

def taxicab_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def astar(start, end):
    open_set = [[taxicab_dist(start, end), tuple(start)]]
    # tuples are like lists (list == array in most other languages)
    # except tuples cannot have their items changed. Look up how
    # sets and dictionaries work if you want to understand why it
    # needs to have tuples not lists.
    
    closed_set = set([tuple(start)])

    dirs = [[[[], None] for x in range(len(map.map[0]))] for y in range(len(map.map))]
    # dirs[y][x] should give a list of places it could have come from and how far it is
    # from the start.
    dirs[start[1]][start[0]][1] = 0

    def path_distance(point, start_distance):
        return start_distance/4 + taxicab_dist(point, end)

    while len(open_set) > 0:
        # It should return out of the while loop before then, but just in case there isn't
        # a path.

        
        o = open_set.pop(0)[1]
        draw(open_set, closed_set, o)

        distance = dirs[o[1]][o[0]][1] + 1
        for n in map.get(o):
            if tuple(n) in closed_set and dirs[n[1]][n[0]][1] <= distance:
                continue

            item = [path_distance(n, distance), tuple(n)]
            bisect.insort(open_set, item)
            closed_set.add(tuple(n))
            if dirs[n[1]][n[0]][1] is None or dirs[n[1]][n[0]][1] == distance:
                dirs[n[1]][n[0]][0].append(o)
                dirs[n[1]][n[0]][1] = distance
            elif dirs[n[1]][n[0]][1] > distance:
                dirs[n[1]][n[0]][0] = [o]
                dirs[n[1]][n[0]][1] = distance

            if n == end:
                return reconstruct_path(start, end, dirs)
                

    # No path from start to end.
    return None

def reconstruct_path(start, end, dirs):
    path = []
    while end != start and dirs[end[1]][end[0]][0] != []:
        draw_path(end)
        path.append(end)
        end = dirs[end[1]][end[0]][0][0]
    return path[::-1]

def draw(open_set, closed_set, o):
    pygame.time.delay(100)
    reset()
    for pos in closed_set:
        rect.x = pos[0]*50
        rect.y = pos[1]*50
        screen.blit(closedsurf, rect)
    for dist, pos in open_set:
        rect.x = pos[0]*50
        rect.y = pos[1]*50
        screen.fill((255, 255, 0), rect)
    rect.x = o[0]*50
    rect.y = o[1]*50
    screen.fill((255, 0, 0), rect)
    rect.x = map.start[0]*50
    rect.y = map.start[1]*50
    screen.fill((0, 255, 0), rect)
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
map = Map()
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
        if (x, y) == map.start:
            rect.x = x*50
            rect.y = y*50
            mapsurf.fill((0, 255, 0), rect)
        if (x, y) == map.end:
            rect.x = x*50
            rect.y = y*50
            mapsurf.fill((255, 0, 0), rect)

reset()
pygame.display.update()

astar(map.start, map.end)
