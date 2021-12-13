import matplotlib.pyplot as plt

def fold_paper(dots,dir,fold):
    new_dots = []
    if dir not in [0,1]:
        return []
    for dot in dots:
        if dot[dir] < fold:
            new_dots.append(dot)
            continue
        if dot[dir] > fold:
            temp = dot[dir]-((dot[dir]-fold) *2)
            if dir == 0:
                new_dots.append((temp,dot[1]))
            else:
                new_dots.append((dot[0],temp))
    return list(set(new_dots))

def print_dots(dots):
    x = []
    y=[]
    for dot in dots:
        x.append(dot[0])
        y.append(-1* dot[1])
    
    #plot ein bissl zusammenschieben lol
    plt.scatter(x,y, marker ='*')
    plt.show()

def day13(input):
    dots = []
    dic ={'x':0,'y':1}
    with open(input) as inputfile:
        for line in inputfile:
            if line == '\n':
                break
            dot = line.rstrip().split(',')
            dots.append((int(dot[0]),int(dot[1])))
        
        dots_one = fold_paper(dots,0,655)
        
        for line in inputfile:
            fold = line.rstrip().replace('fold along ', '').split('=')
            dots = fold_paper(dots,dic[fold[0]],int(fold[1]))
        
        print_dots(dots)
        
    return len(dots_one)
    
input = 'day13_input.txt'
print(day13(input))