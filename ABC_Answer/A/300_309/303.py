def judge(a,b):
    if a == b:
        return True
    elif a == '0' and b == 'o' or a == 'o' and b == '0':
        return True
    elif a == '1' and b == 'l' or a == 'l' and b == '1':
        return True
    else:
        return False

N = int(input())
S = input()
T = input()


for i in range(N):
    if not judge(S[i], T[i]):
        print('No')
        exit()

print('Yes')