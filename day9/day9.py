class Heatmap:
    def __init__(self, map):
        self.heatmap = map
    
    def get_heatmap(self):
        return self.heatmap
    
    def get_risklevel(self,pos):
        x, y = pos
        return self.heatmap[x][y] + 1
    
    def get_lowpoints(self):
        x = 0
        lowpoints = []
        for row in self.heatmap:
            for y in range(0,len(row)):
                if y < len(row)-1:
                    if row[y] >= row[y+1]:
                        continue

                if y > 0:
                    if row[y] >= row[y-1]:
                        continue
                
                if x < len(self.heatmap) - 1:
                    if row[y] >= self.heatmap[x+1][y]:
                        continue
                
                if x > 0:
                    if row[y] >= self.heatmap[x-1][y]:
                        continue
                
                lowpoints.append((x,y))
            x += 1
        return lowpoints
    
    def get_neighbors(self, basin, pos):
        x,y = pos
        print(x)
        print(y)
        if x < 0 or y < 0 or x >= len(self.heatmap) or y >= len(self.heatmap[0]):
            return basin
        elif self.heatmap[x][y] == 9:
            return basin
        elif (x,y) in basin:
            return basin
        else:
            basin.append((x,y))
            basin = self.get_neighbors(basin, (x+1,y))
            basin = self.get_neighbors(basin, (x-1,y))
            basin = self.get_neighbors(basin, (x,y+1))
            basin = self.get_neighbors(basin, (x,y-1))
            return basin
        
        
    def get_basin_size(self, start):
        x,y = start
        basin = [start]
        print(basin)
        basin = self.get_neighbors(basin,(x+1,y))
        basin = self.get_neighbors(basin,(x-1,y))
        basin = self.get_neighbors(basin,(x,y+1))
        basin = self.get_neighbors(basin,(x,y-1))
        print(basin)
        return len(basin)

def day9(input):
    numbers = []
    with open(input) as inputfile:
        for line in inputfile:
            #numbers = line.rstrip()
            row = [int(x) for x in line.rstrip()]
            numbers.append(row)
    
    heatmap = Heatmap(numbers)
    lowpoints = heatmap.get_lowpoints()
    basin_sizes = [heatmap.get_basin_size(lp) for lp in lowpoints]
    basin_sizes.sort(reverse = True)
    result = 1
    for x in basin_sizes[:3]:
        result = result * x
    return (sum([heatmap.get_risklevel(x) for x in lowpoints]),result)
    
input = 'day9_input.txt'
print(day9(input))