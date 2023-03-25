correct_list = ["and", "not", "that", "the", "you"]

N = int(input())
W = input().split()
for w in W:
    if w in correct_list:
        print('Yes')
        exit()
print('No')
    