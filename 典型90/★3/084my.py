from bisect import bisect_left

N = int(input())
S = input()

maru = []
batu = []

for i in range(N):
    if S[i] == 'o':
        maru.append(i)
    else:
        batu.append(i)

ans = 0
for i in range(N):
    try:
        if S[i] == 'o':
            index = bisect_left(batu, i)
            ans += N - batu[index]
        else:
            index = bisect_left(maru, i)
            ans += N - maru[index]
    except IndexError:
        pass

print(ans)

