#Day 1.1

#returns 1 if y is larger than x, else 0
def has_inc(x,y):
    if x < y:
        return 1
    else:
        return 0

#return sum of a, b and c 
def sum_of_three(a,b,c):
    return a+b+c

def inc_counter(input):
    inc_count = 0
    
    with open(input) as inputfile:
        old_dept = int(inputfile.readline().rstrip())
        for line in inputfile:
            current_dept = int(line.rstrip())
            inc_count = inc_count + has_inc(old_dept,current_dept)
            old_dept = current_dept
            
    
    return inc_count
    
def inc_windows(input):
    inc_count = 0
    numbers = []
    with open(input) as inputfile:
        
        for line in inputfile:
            numbers.append(int(line.rstrip()))
            
    for i in range(0,len(numbers)-3):
        inc_count = inc_count + has_inc(sum_of_three(numbers[i],numbers[i+1],numbers[i+2]),sum_of_three(numbers[i+1],numbers[i+2],numbers[i+3]))
           
    return inc_count

input = 'day1_input.txt'

print('Result 1.1: ' + str(inc_counter(input)))
print('Result 1.2: ' + str(inc_windows(input)))