#  a
# b c
#  d
# e f
#  g
# [a,b,c,d,e,f,g]

def count1_4_7_8(wires):
    sum = 0
    for x in wires:
        for i in x:
            if len(i) == 2 or len(i) == 4 or len(i) == 3 or len(i) == 7:
                sum += 1

def decoder(entry):
    input, output = entry
    dic={}
    
    eins = [x for x in input if len(x) == 2][0]
    dic[''.join(sorted(eins))] = '1'
    input.remove(eins)
    
    sieben = [x for x in input if len(x) == 3][0]
    dic[''.join(sorted(sieben))] = '7'
    input.remove(sieben)
    
    vier = [x for x in input if len(x) == 4][0]
    dic[''.join(sorted(vier))] = '4'
    input.remove(vier)
    
    acht = [x for x in input if len(x) == 7][0]
    dic[''.join(sorted(acht))] = '8'
    input.remove(acht)
    
    null_drei_neun =[]
    
    for x in input:
        if sum([c in list(set(eins)) for c in x]) == 2:
            null_drei_neun.append(x)
    
    for x in null_drei_neun:
        if sum([c in list(set(vier)) for c in x]) == 4:
            neun = x
            dic[''.join(sorted(neun))] = '9'
            input.remove(neun)
    null_drei_neun.remove(neun)
    
    drei = [x for x in null_drei_neun if len(x) == 5][0]
    dic[''.join(sorted(drei))] = '3'
    null_drei_neun.remove(drei)
    input.remove(drei)
    
    null = null_drei_neun[0]
    dic[''.join(sorted(null))] = '0'
    input.remove(null)
    
    vier_minus_eins = ''.join([c for c in vier if c not in set(eins)])
    
    fünf_sechs = []
    for x in input:
        if sum([c in list(set(vier_minus_eins)) for c in x]) == 2:
            fünf_sechs.append(x)
        else:
            zwei = x
    
    dic[''.join(sorted(zwei))] = '2'
    
    acht_minus_eins = ''.join([c for c in acht if c not in set(eins)])
    
    for x in fünf_sechs:
        if sum([c in list(set(acht_minus_eins)) for c in x]) == 5:
            sechs = x
        else:
            fünf = x
            
    dic[''.join(sorted(fünf))] = '5'
    dic[''.join(sorted(sechs))] = '6'
    
    numb = ''
    for x in output:
        numb = numb + dic[''.join(sorted(x))]
    return int(numb)
    
def day8(input):
    wires = []
    sum = 0
    with open(input) as inputfile:
        for line in inputfile:
            new_in, new_out = line.rstrip().split('|')
            new_in = list(filter(lambda x: x != '' , new_in.split(' ')))
            new_out = list(filter(lambda x: x != '' , new_out.split(' ')))

            wires.append(new_out)
            sum = sum + decoder((new_in, new_out))
        result = count1_4_7_8(wires)
            
        return (result,sum)
input = 'day8_input.txt'
print(day8(input))