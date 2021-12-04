
class Board:
    #self.board = [[00,01,02,03,04],[10,11,12,13,14],[20,21,22,23,24],[30,31,32,33,34],[40,41,42,43,44]]
    
    def __init__(self, numbers):
        self.board=numbers
        self.marked = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        self.has_won = False
        
    def get_row(self, x):
        return self.board[x]
    
    def get_marked_row(self,x):
        return self.marked[x]
    
    def get_column(self, x):
        return [self.board[0][x],self.board[1][x],self.board[2][x],self.board[3][x],self.board[4][x]]
        
    def get_marked_column(self, x):
        return [self.marked[0][x],self.marked[1][x],self.marked[2][x],self.marked[3][x],self.marked[4][x]]
    
    def get_board(self):
        return self.board
        
    def get_marked_board(self):
        return self.marked
    
    def get_gamestat(self):
        return self.has_won
        
    def set_gamestat(self):
        self.has_won=True
    
    def mark_number(self, n):
        for x in range(0,5):
            for y in range(0,5):
                if self.board[x][y] == n:
                    self.marked[x][y] = 1

    def check_board(self):
        for x in range(0,5):
            if 0 not in self.get_marked_column(x):
                return True
            if 0 not in self.get_marked_row(x):
                return True
        return False
    
    def get_unchecked_sum(self):
        sum = 0
        for x in range(0,5):
            for y in range(0,5):
                if self.marked[x][y] == 0:
                    sum = sum + int(self.board[x][y])
        return sum

def get_input(input):
    temp_board = []
    boards = []
    
    with open(input) as inputfile:
        numbers_line = inputfile.readline().rstrip().split(',')
        inputfile.readline()
        i=0
        for line in inputfile:
        
            str_row = line.rstrip()
            row = str_row.split()
            
            if row == []:
                continue
            temp_board.append(row)
            
            if i==4:
                i = 0
                boards.append(Board(temp_board))
                temp_board=[]
                
                continue
            
            i += 1
    return numbers_line , boards
    
def day4(input):
    numbers, boards = get_input(input)
    
    first = 0
    second = 0
    
    for number in numbers:
        for board in boards:
            board.mark_number(number)
            if board.check_board() == True:
                if board.get_gamestat() == False:
                    second =  board.get_unchecked_sum() * int(number)
                    board.set_gamestat()
    
    numbers, boards = get_input(input)
    
    for number in numbers:
        for board in boards:
            board.mark_number(number)
            if board.check_board() == True:
                first =  board.get_unchecked_sum() * int(number)
                return (first,second)
    
    return (first,second)

input = 'day4_input.txt'
print(day4(input))