import time
class Dumbo_Octopus():
    def __init__(self,value):
        self.has_flashed = False
        self.value = value
        
    def flash_status(self):
        return self.has_flashed
        
    def flash(self):
        self.has_flashed = True
    
    def clear_step(self):
        self.has_flashed = False

    def inc_value(self):
        self.value +=1
        
    def clear_value(self):
        self.value = 0
    
    def get_value(self):
        return self.value

class Dumbo():
    def __init__(self, octopuses):
        self.octos = []
        for x in range(len(octopuses)):
            self.octos.append([])
            for y in range(len(octopuses[x])):
                self.octos[x].append(Dumbo_Octopus(octopuses[x][y]))

    def get_flashes(self):
        sum = 0
        
        for x in range(len(self.octos)):
            for y in range(len(self.octos[x])):
                if self.octos[x][y].get_value() == 0:
                    sum += 1
        return sum
    
    def increase_neighbours(self,pos):
        x,y = pos
        over_nine = False
        for i in range(-1,2):
            for j in range(-1,2):
                if (x + i < 0) or (y + j < 0) or (x + i >= len(self.octos)) or (y + j >= len(self.octos[x+i])):
                    continue
                self.octos[x+i][y+j].inc_value()
                if self.octos[x+i][y+j].get_value() > 9:
                    over_nine = True
        return over_nine
    
    def step(self):
        for x in range(len(self.octos)):
            for y in range(len(self.octos[x])):
                self.octos[x][y].inc_value()
        
        over_nine = True
        while over_nine == True:
            over_nine = False
            
            for x in range(len(self.octos)):
                for y in range(len(self.octos[x])):
                    if self.octos[x][y].get_value() > 9 and self.octos[x][y].flash_status() == False:
                        temp = self.increase_neighbours((x,y))
                        if temp == True:
                            over_nine = True
                        self.octos[x][y].flash()
        
        flashcount = 0
        all_flashed= True
        for x in range(len(self.octos)):
            for y in range(len(self.octos[x])):
                if self.octos[x][y].flash_status() == False:
                    all_flashed= False
                if self.octos[x][y].get_value() > 9:
                    self.octos[x][y].clear_step()
                    self.octos[x][y].clear_value()
            
        return all_flashed
def day11(input):
    octos = []
    sum = 0
    all_flashed = False
    k = 0
    
    with open(input) as inputfile:
        for line in inputfile:
            octos.append([int(x) for x in line.rstrip()])
    
    dumbos = Dumbo(octos)
    for i in range(0,100):
        dumbos.step()
        sum = sum + dumbos.get_flashes()

    dumbos = Dumbo(octos)
    while all_flashed == False:
        all_flashed = dumbos.step()
        k += 1
    return (sum, k)
    
input = 'day11_input.txt'
print(day11(input))