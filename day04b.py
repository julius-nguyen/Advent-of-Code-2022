i = 0

def intrange(s):
    n_start,n_end = s.split('-')
    return {i for i in range(int(n_start),int(n_end)+1)}

with open('day04input.txt', encoding='utf-8') as f:

    for line in f.read().split('\n'):
        
        if line == '':
            continue
        
        range1, range2 = line.split(',')
        
        if intrange(range1) & intrange(range2) != set():
            i += 1
            
        else:
            continue

print(i)
