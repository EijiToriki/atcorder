import math

N, A, B = map(int, input().split())

sumN = N*(N+1) // 2

Acnt = N // A
Acnt = Acnt*(Acnt+1) // 2
sumA = A * Acnt

Bcnt = N // B
Bcnt = Bcnt*(Bcnt+1) // 2
sumB = B * Bcnt

lcmAB = (A*B) // math.gcd(A, B)
lcm_cnt = N // lcmAB
lcm_cnt = lcm_cnt*(lcm_cnt+1) // 2
sum_lcm = lcmAB * lcm_cnt

ans = sumN - (sumA + sumB) + sum_lcm

print(ans)