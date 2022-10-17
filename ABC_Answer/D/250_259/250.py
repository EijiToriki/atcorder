from bisect import bisect_left, bisect_right


def sieve_of_eratosthenes(x):
    nums = [i for i in range(x+1)]

    root = int(pow(x,0.5))
    for i in range(2,root + 1):
        if nums[i] != 0:
            for j in range(i, x+1):
                if i*j >= x+1:
                    break
                nums[i*j] = 0

    primes = sorted(list(set(nums)))[2:]

    return primes


N = int(input())
primes = sieve_of_eratosthenes(int(N ** (1/3)))

ans = 0

for prime in primes[1:]:
    candidate_p = N // (prime**3)
    if candidate_p >= prime:
        ans += bisect_left(primes, prime)
    else:
        ans += bisect_right(primes, candidate_p)

print(ans)