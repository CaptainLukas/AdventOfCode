class Position:
    
    def __init__(self, x=0, y=0, z = 0):
        self.horizontal = x
        self.depth = y
        self.aim = z
        
    def forward(self,x):
        self.horizontal = self.horizontal + x
        self.depth = self.depth + (self.aim * x)
        
    #inverted because of submarine    
    def down(self, x):
        self.aim = self.aim + x
    
    #inverted because of submarine
    def up(self, x):
        self.aim = self.aim - x
    
    def backward(self, x):
        self.horizontal = self.horizontal - x
    
    def move(self, move,x):
        if move == 'forward':
            self.forward(x)
        elif move == 'down':
            self.down(x)
        elif move == 'up':
            self.up(x)
        elif move == 'backwards':
            self.backward(x)
        else:
            print('invalid move')
        
    def get_position(self):
        return (self.horizontal,self.depth)
        
    def get_position_multiply(self):
        return (self.horizontal*self.depth)

def day2_1(input):

    submarine = Position()
    
    with open(input) as inputfile:
        for line in inputfile:
            move, x = line.rstrip().split(' ')
            submarine.move(move,int(x)) 
    
    print(submarine.get_position_multiply())
            

input = 'day2_input.txt'
day2_1(input)