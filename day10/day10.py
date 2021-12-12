def check_line(line):
    open =['(','[','{','<']
    dec = {')':'(', ']':'[', '}':'{','>':'<'}
    opened=[]
    score = 0
    for i in range(0,len(line)):
        if line[i] in open:
            opened.append(line[i])
        elif dec[line[i]] == opened[-1]:
            opened = opened[:-1]
            continue
        elif line[i] == ')':
            return (3,score)
        elif line[i] == ']':
            return (57,score)
        elif line[i] == '}':
            return (1197,score)
        else:
            line[i] == '>'
            return (25137,score)
    
    for x in range(len(opened)-1, -1, -1):
        score = score * 5
        if opened[x] == '(':
            score = score + 1
        if opened[x] == '[':
            score = score + 2
        if opened[x] == '{':
            score = score + 3
        if opened[x] == '<':
            score = score + 4
    
    return (0,score)
    
def day10(input):
    sum = 0
    scores = []
    with open(input) as inputfile:
        for line in inputfile:
            error, closing = check_line(line.rstrip())
            sum = sum + error
            if closing != 0:
                scores.append(closing)
    scores.sort()
    return (sum, scores[int((len(scores)/2) -0.5)])
    
input = 'day10_input.txt'
print(day10(input))