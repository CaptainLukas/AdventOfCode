#p...current position t...target position
def need_of_fuel(p,t):
    return abs(p - t)

def need_of_fuel2(p, t):
    return sum(range(0,abs(p-t)+1))

def get_input(input):
    with open(input) as inputfile:
        numbers = [int(x) for x in inputfile.readline().rstrip().split(',')]
    return numbers
def day7(input):

    numbers = get_input(input)

    numbers.sort()
    i = numbers[round(len(numbers)/2)]
    fast = sum([need_of_fuel(x,i) for x in numbers])
    
    last = sum([need_of_fuel2(x,min(numbers)) for x in numbers])
    
    for i in range(min(numbers)+1,max(numbers)):
        result = sum([need_of_fuel2(x,i) for x in numbers])
        if last < result:
            break
        
        last = result
    return (fast,last)

input = 'day7_input.txt'
print(day7(input))
