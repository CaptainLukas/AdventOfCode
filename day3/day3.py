def most_common_on_pos(x,pos):
    return '1' if sum([int(str(b)[pos]) for b in x]) >= (len(x)/2) else '0'

def least_common_on_pos(x,pos):
    return '0' if sum([int(str(b)[pos]) for b in x]) >= (len(x)/2) else '1'

def binary_counter(list):
    gamma = ''
    epsilon = ''

    for i in range(12):
        gamma = gamma + most_common_on_pos(list,i)
        epsilon = epsilon + least_common_on_pos(list,i)
        i+=1
    
    return (int(gamma,2),int(epsilon,2))
    
def oxygen_generator_rating(list):
    i = 0
    while len(list) > 1:
        most_common = most_common_on_pos(list,i)
        list = [x for x in list if x[i] == most_common]
        i += 1
    return int(list[0],2)

def co2_scrubber_rating(list):
    i = 0
    while len(list) > 1:
        least_common = least_common_on_pos(list,i)
        list = [x for x in list if x[i] == least_common]
        i += 1
    return int(list[0],2)

def life_support_rating(list):
    return oxygen_generator_rating(list) * co2_scrubber_rating(list)
  
def day3(input):

    with open(input) as inputfile:
        binary = inputfile.readlines()
        binary  = [b.rstrip() for b in binary]
        x,y = binary_counter(binary)
        
    return (x*y, life_support_rating(binary))

input = 'day3_input.txt'
x,y = day3(input)
print('power consumption: ' + str(x) + '\nlife support rating: ' + str(y))
