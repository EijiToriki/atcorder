import sys

a, b, c = map(int, input().split())

c_b = 1

for _ in range(b):
    c_b *= c
    if a < c_b:
        print('Yes')
        sys.exit()
        
print('No')