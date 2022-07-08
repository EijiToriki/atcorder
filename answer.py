from bisect import bisect_left

N = int(input())
S = input()

ans = N*(N+1) // 2

focus_char = S[0]
focus_point = 1
for i in range(1,N):
    if S[i] == focus_char:
        focus_point += 1
    else:
        ans -= focus_point*(focus_point+1) // 2
        focus_char = S[i]
        focus_point = 1

ans -= focus_point*(focus_point+1) // 2

print(ans)

