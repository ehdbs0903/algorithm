import sys

input = sys.stdin.readline

n = int(input())
 
_set = set() 
for _ in range(n):
	s = input()
	
	if s[-2] == 'r':
		_set.add(s[:-7])
	else:
		_set.remove(s[:-7])

print('\n'.join(sorted(_set, reverse=True)))
