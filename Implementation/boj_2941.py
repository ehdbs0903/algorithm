c = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

s = input()

for i in c:
    s = s.replace(i, '.')
    
print(len(s))
