class Diagram:
    def __init__(self):
        self.diag = {}
    
    def add_line(self, x1, y1, x2, y2):
    
        if x1 == x2:
            low = y1 if y1 < y2 else y2
            high = y1 if y1 > y2 else y2
            for y in range(low,high+1):
                if (x1, y) in self.diag:
                    self.diag[(x1,y)] = self.diag[(x1,y)] + 1
                else:
                    self.diag[(x1,y)] = 1
                    
        if y1 == y2:
            low = x1 if x1 < x2 else x2
            high = x1 if x1 > x2 else x2
            for x in range(low,high+1):
                if (x, y1) in self.diag:
                    self.diag[(x,y1)] = self.diag[(x,y1)] + 1
                else:
                    self.diag[(x,y1)] = 1
        
        if x1 < x2 and y1 < y2:
            for x in range(x1,x2+1):
                if (x, y1 + x - x1) in self.diag:
                    self.diag[(x,y1 + x - x1)] = self.diag[(x,y1 + x - x1)] + 1
                else:
                    self.diag[(x,y1 + x - x1)] = 1
                    
        if x1 > x2 and y1 < y2:
            x = x1
            for y in range(y1,y2+1):
                if (x, y) in self.diag:
                    self.diag[(x,y)] = self.diag[(x,y)]+1
                else:
                    self.diag[(x,y)] = 1
                x = x - 1
        
        if x1 < x2 and y1 > y2:
            y = y1
            for x in range(x1,x2+1):
                if (x, y) in self.diag:
                    self.diag[(x,y)] = self.diag[(x,y)]+1
                else:
                    self.diag[(x,y)] = 1
                y = y - 1
                
        if x1 > x2 and y1 > y2:
            for x in range(x2,x1+1):
                if (x, y2 + x - x2) in self.diag:
                    self.diag[(x,y2 + x - x2)] = self.diag[(x,y2 + x - x2)] + 1
                else:
                    self.diag[(x,y2 + x - x2)] = 1
                
        
    def return_overlaps(self):
        overlaps = 0
        for key in self.diag:
            if self.diag[key] > 1:
                overlaps += 1
        return overlaps

def day5(input):
    diagram = Diagram()
    
    with open(input) as inputfile:
        for line in inputfile:
            x1,y1,x2,y2 = line.rstrip().replace(' -> ',',').split(',')
            diagram.add_line(int(x1),int(y1),int(x2),int(y2))
    
    print(diagram.return_overlaps())
            

input = 'day5_input.txt'

day5(input)