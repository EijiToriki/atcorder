N = int(input())
S, A = [], []
for _ in range(N):
    s, a = input().split()
    S.append(s)
    A.append(int(a))

minA_idx = A.index(min(A))

for i in range(N):
    print(S[(minA_idx+i)%N])