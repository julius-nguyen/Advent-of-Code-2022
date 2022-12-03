import string

shared = []

def halves(s):
    pos = int(len(s)/2)
    return s[:pos],s[pos:]

def shared_letters(stup):
    s1,s2 = stup
    
    return set([c for c in s1]) & set([c for c in s2])
    
def priorities(c):
    if c in list(string.ascii_lowercase):
        return list(string.ascii_lowercase).index(c)+1
    
    elif c in list(string.ascii_uppercase):
        return list(string.ascii_uppercase).index(c)+27
    
    else:
        return 0
    
with open('day03input.txt', encoding='utf-8') as f:

    for line in f.read().split('\n'):

        if line == '':
            continue
        
        shared += list(shared_letters(halves(line)))
    
#print(shared)

print(sum([priorities(c) for c in shared]))
