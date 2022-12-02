points_dict = {'X':1, 
               'Y':2, 
               'Z':3,
               'AX':3,'BY':3,'CZ':3,
               'AZ':0,'CX':6,
               'CY':0,'BZ':6,
               'BX':0, 'AY':6}

total = 0

with open('day02input.txt', encoding='utf-8') as f:

    for line in f.read().split('\n'):

        if line == '':
            continue

        move1,move2 = line.split(' ')

        total += points_dict[move2]+points_dict[move1+move2]
    
print(total)
