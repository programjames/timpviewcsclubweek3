import pygame
from mymap import Map

def dfs(start, end, depth=0, lis=None):
    if lis == None:
        lis = [start]
    draw(lis)
    pygame.time.delay(100)
    if depth == 0:
        if start == end:
            return lis
        else:
            return []
    nexts = map.get(start)
    for next in nexts:
        if next not in lis:
            solution = dfs(next, end, depth-1, lis + [next])
            if solution != []:
                return solution
    return []

def draw(lis):
    reset()
    for pos in lis:
        rect.x = pos[0]*50
        rect.y = pos[1]*50
        screen.fill((0, 0, 255), rect)
    rect.x = map.start[0]*50
    rect.y = map.start[1]*50
    screen.fill((0, 255, 0), rect)
    pygame.display.update()
    pygame.event.pump()

def reset():
    screen.blit(mapsurf, (0, 0))
    

global map, screen, rect, surf, mapsurf
map = Map()
screen = pygame.display.set_mode((500, 500))
rect = pygame.Rect(0, 0, 50, 50)
surf = pygame.Surface((50, 50))
surf.fill((0, 0, 255))

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

depth = 1
while dfs(map.start, map.end, depth) == []:
    depth += 1
