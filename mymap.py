"""
Make a map.
"""

class Map():
    def __init__(self):
        self.map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.neighbors = [[[] for a in range(10)] for b in range(10)]
        for x in range(10):
            for y in range(10):
                ns = []
                if x>0 and not self.map[y][x-1]:
                    ns.append([x-1, y])
                if y>0 and not self.map[y-1][x]:
                    ns.append([x, y-1])
                if x<9 and not self.map[y][x+1]:
                    ns.append([x+1, y])
                if y<9 and not self.map[y+1][x]:
                    ns.append([x, y+1])
                self.neighbors[y][x] = ns
        self.start = [2, 8]
        self.end = [9, 0]
    def get(self, pos):
        return self.neighbors[pos[1]][pos[0]]

class Map2():
    def __init__(self):
        self.map = [[False, False, True, False, False, False, False, False, False, False], [False, False, True, False, False, False, True, True, False, False], [False, False, True, True, True, True, True, True, True, True], [False, False, True, False, False, False, False, False, False, False], [False, False, True, False, False, False, True, True, False, False], [True, True, True, True, True, True, False, False, False, False], [False, False, False, False, False, True, True, True, True, True], [False, False, False, False, True, True, False, False, True, False], [True, True, True, True, True, False, False, True, False, False], [False, False, False, False, True, False, False, False, False, False]]
        self.neighbors = [[[] for a in range(10)] for b in range(10)]
        for x in range(10):
            for y in range(10):
                ns = []
                if x>0 and not self.map[y][x-1]:
                    ns.append([x-1, y])
                if y>0 and not self.map[y-1][x]:
                    ns.append([x, y-1])
                if x<9 and not self.map[y][x+1]:
                    ns.append([x+1, y])
                if y<9 and not self.map[y+1][x]:
                    ns.append([x, y+1])
                self.neighbors[y][x] = ns
    def get(self, pos):
        return self.neighbors[pos[1]][pos[0]]
