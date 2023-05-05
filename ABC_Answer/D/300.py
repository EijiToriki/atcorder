import math

def sieve_of_eratosthenes(n):
    prime = [True for i in range(n+1)]
    prime[0] = False
    prime[1] = False

    sqrt_n = math.ceil(math.sqrt(n))
    for i in range(2, sqrt_n):
        if prime[i]:
            for j in range(2*i, n+1, i):
                prime[j] = False

    return prime

maxC = 3*(10**5)
N = int(input())

seg_prime = sieve_of_eratosthenes(maxC)
prime = []
for p in range(maxC):
    if seg_prime[p]:
        prime.append(p)


sz = len(prime)
ans = 0

for i in range(sz):
    for j in range(i+1, sz):
        for k in range(j+1, sz):
            v = prime[i] * prime[i] * prime[j]
            if v > N:
                break
            v *= prime[k]
            if v > N:
                break
            v *= prime[k]
            if v > N:
                break
            ans += 1

print(ans)


