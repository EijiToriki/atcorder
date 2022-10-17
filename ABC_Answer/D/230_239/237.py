from collections import deque
import sys

sys.setrecursionlimit(10**6)

N = int(input())
S = input()
ans = deque([N])

def f(n):
    if n-1 == 0:
        if S[0] == 'R':
            ans.appendleft(0)
        else:
            ans.append(0)
    elif S[n-1] == 'R':
        ans.appendleft(n-1)
        return f(n-1)
    else:
        ans.append(n-1)
        return f(n-1)


def main():
    f(N)
    print(*ans)

if __name__ == '__main__':
    main()