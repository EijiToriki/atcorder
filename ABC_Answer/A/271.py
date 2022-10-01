N = int(input())

N = hex(N)
N = N[2:].upper()

if len(N) == 1:
    print('0' + N)
else:
    print(N)