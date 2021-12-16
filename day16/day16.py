import math

def hex_to_bin(hex):
    if hex == '0':
        return '0000'
    if hex == '1':
        return '0001'
    if hex == '2':
        return '0010'
    if hex == '3':
        return '0011'
    if hex == '4':
        return '0100'
    if hex == '5':
        return '0101'
    if hex == '6':
        return '0110'
    if hex == '7':
        return '0111'
    if hex == '8':
        return '1000'
    if hex == '9':
        return '1001'
    if hex == 'A':
        return '1010'
    if hex == 'B':
        return '1011'
    if hex == 'C':
        return '1100'
    if hex == 'D':
        return '1101'
    if hex == 'E':
        return '1110'
    if hex == 'F':
        return '1111'


def literal_value(bin):
    i = 0
    number=''
    if bin =='':
        return([],0)
    while i < len(bin):
        if bin[i] == '0':
            number = number + bin[i+1] +bin[i+2]+bin[i+3]+bin[i+4]
            i+= 5

            return ([int(number,2)],i)
        elif bin[i] == '1':
            number = number + bin[i+1] +bin[i+2]+bin[i+3]+bin[i+4]
            i=i+4
        
        i += 1
        
    return (0,0)

def operator(bin):
    if bin == '':
        return ([],0)

    i = 0
    number = []
    versions = []
    if bin[i] == '0':
        length = int(bin[1:16],2)
        i = 16
        j= 0
        while j < length:
            version,new_number, new_packetlength = packet_header(bin[i:])
            versions = versions +version
            j+=new_packetlength
            i += new_packetlength
            number = number + new_number
    elif bin[i] == '1':
        length = int(bin[1:12],2)
        i = 12
        j = 0
        while j < length:
            version,new_number, new_packetlength = packet_header(bin[i:])
            versions = versions +version
            i += new_packetlength
            number = number + new_number
            j+= 1
    
    return (versions,number,i)

def packet_header(bin):
    if bin =='':
        return ([],0)
    number = []
    length = 0
    i = 0
    version = int(bin[:3],2)
    
    versions = [version]
    
    
    i = 3
    typeID = int(bin[i:6],2)
    i = 6
    
    if typeID == 4:
        number , length = literal_value(bin[i:])
        return (versions,number, length+i)
    
        
    else:
        if typeID == 0:
            new_version, number , length = operator(bin[i:])
            number = [sum(number)]
        if typeID == 1:
            new_version, number , length = operator(bin[i:])
            number = [math.prod(number)]
        if typeID == 2:
            new_version, number , length = operator(bin[i:])
            
            number = [min(number)]
        if typeID == 3:
            new_version, number , length = operator(bin[i:])
            
            number = [max(number)]
        if typeID == 5:
            new_version, number , length = operator(bin[i:])
            if number[0] > number[1]:
                number =[1]
            else:
                number = [0]
        if typeID == 6:
            new_version, number , length = operator(bin[i:])
            if number [0] < number[1]:
                number = [1]
                
            else:
                number = [0]
        if typeID == 7:
            new_version, number , length = operator(bin[i:])
            if number[0] == number[1]:
                number = [1]
            else:
                number=[0]
        return (versions+new_version,number, length+i)

def day16(input):
    cave=[]
    sum_v = 0
    with open(input) as inputfile:
        line = inputfile.readline().rstrip()
    bin = ''
    
    for x in line:
        bin += hex_to_bin(x)
        
    version,numbers,length = packet_header(bin)
    sum_v = sum(version)
    
    return (sum_v,numbers)
   
input = 'day16_input.txt'

print(day16(input))
