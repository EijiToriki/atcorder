N = input()
A = list(map(int, input().split()))

A = sorted(A, reverse=True)

A_even = [a for a in A if a%2 == 0]
A_odd = [a for a in A if a%2 == 1]

if len(A_even) == 1 and len(A_odd) == 1:
    print(-1)
else:
    ans = 0
    if len(A_even) == 1 or len(A_even) == 0:
        ans = A_odd[0] + A_odd[1]
        print(ans)
    elif len(A_odd) == 1 or len(A_odd) == 0:
        ans = A_even[0] + A_even[1]
        print(ans)
    else:
        ans = max(A_even[0] + A_even[1], A_odd[0] + A_odd[1])
        print(ans)