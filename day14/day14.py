def insert_str(string, str_to_insert, index):
    return string[:index] + str_to_insert + string[index:]

def insert_step(polymer, rules):
    inserts = []
    for i in range(len(polymer)-1,0,-1):
        if polymer[i-1] +polymer[i] in rules:
            polymer = insert_str(polymer, rules[polymer[i-1] +polymer[i]], i)
        
    return polymer

def insert_step_two(polymer, letters, rules):
    temp_poly = polymer.copy()
    
    for c in temp_poly:
        if temp_poly[c] == 0:
            continue

        if rules[c] in letters:
            letters[rules[c]] += temp_poly[c]
        else:
            letters[rules[c]] = temp_poly[c]
        polymer[c[0]+rules[c]] += temp_poly[c]
        polymer[rules[c]+c[1]]+= temp_poly[c]
        polymer[c] = polymer[c] - temp_poly[c]

    return (polymer,letters)

def day14(input):
    rules={}
    polymer = {}
    letters = {}
    with open(input) as inputfile:
        polymer_template = inputfile.readline().rstrip()
        for x in polymer_template:
            if x in letters:
                letters[x] = letters[x] + 1
            else:
                letters[x] = 1
        
        for line in inputfile:
            if line == '\n':
                continue
            match, insert = line.rstrip().split(' -> ')
            polymer[match] = 0
            rules[match] = insert
            
        for i in range(0,len(polymer_template)-1):
            if polymer_template[i] + polymer_template[i+1] in polymer:
                polymer[polymer_template[i] + polymer_template[i+1]] += 1
        
    for i in range (0,10):
        polymer_template = insert_step(polymer_template, rules)

    result = [polymer_template.count(x) for x in polymer_template]
    
    for i in range(0,40):

        polymer,letters = insert_step_two(polymer,letters,rules)
    

    return (max(result)-min(result),max(letters.values())-min(letters.values()))
    
input = 'day14_input.txt'
print(day14(input))