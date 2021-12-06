def day6(input):
    fischi = []
    with open(input) as inputfile:
        for line in inputfile:
            numbers = line.rstrip().split(',')
            
    for number in numbers:
        fischi.append(int(number))
    
    for i in range(0,80):
        new_fisch=0
        fischi = list(map(lambda x: x-1, fischi))
        for x in range(0,len(fischi)):
            if fischi[x] == (-1):
                fischi[x] = 6
                new_fisch = new_fisch + 1
        for x in range(0,new_fisch):
            fischi.append(8)
    return len(fischi)

def day6_fast(input):
    #dic = [0,1,2,3,4,5,6,7,8]
    fish = [0,0,0,0,0,0,0,0,0]
    with open(input) as inputfile:
        for line in inputfile:
            numbers = line.rstrip().split(',')
    
    for i in range(0,9):
        fish[i] = numbers.count(str(i))
    
    for d in range(0,256):
        null = fish[0]
        
        fish[0] = fish[1]
        fish[1] = fish[2]
        fish[2] = fish[3]
        fish[3] = fish[4]
        fish[4] = fish[5]
        fish[5] = fish[6]
        fish[6] = fish[7] + null
        fish[7] = fish[8]
        fish[8] = null
 
    
    return sum(fish)
    
input = 'day6_input.txt'
print(day6(input))
print(day6_fast(input))