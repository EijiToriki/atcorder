import math

N = int(input())

element_list = []
rem = N
for i in range(2,int(math.sqrt(N)+1)):
    while rem % i == 0:
        element_list.append(i)
        rem = rem // i

if rem != 1:
    element_list.append(rem)

print(math.ceil(math.log2(len(element_list))))

    

