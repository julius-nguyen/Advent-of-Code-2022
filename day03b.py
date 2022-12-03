import string

groups = []
shared = []

def shared_letters(stup):
    s1,s2,s3 = stup
    
    return set([c for c in s1]) & set([c for c in s2]) & set([c for c in s3])
    
def priorities(c):
    if c in list(string.ascii_lowercase):
        return list(string.ascii_lowercase).index(c)+1
    
    elif c in list(string.ascii_uppercase):
        return list(string.ascii_uppercase).index(c)+27
    
    else:
        return 0
    
with open('day03input.txt', encoding='utf-8') as f:

    i = 0
    l = []
    for line in f.read().split('\n'):
        
        if line == '':
            continue
        
        if i == 2:
            l.append(line)
            groups.append(tuple(l))
            l = []
            i = 0
    
        else:
            l.append(line)
            i += 1
            
for group in groups:
    shared += list(shared_letters(group))

print(sum([priorities(c) for c in shared]))
