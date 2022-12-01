import sys
sys.setrecursionlimit(10**6)

N = int(input())
A = list((map(int, input().split())))
ans = [0] * 10
depth = 1

def f(a,b,d):
  if d == N-1:
    ans[(a+b)%10] += 1
    ans[(a*b)%10] += 1
    return ans
  else:
    F = (a+b)%10
    G = (a*b)%10
    d += 1
    return f(F, A[d], d), f(G, A[d], d)

f()