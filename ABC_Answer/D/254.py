# 参考：https://qiita.com/sano192/items/d8344f9b9a7bae3a1a6e#d---together-squaredif1191

from bisect import bisect_right

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

N = int(input())
S = [i*i for i in range(1, N+1)]

ans = 0
for i in range(1, N+1):
    factors = factorization(i)
    j = 1
    for factor in factors:
        if factor[1] % 2 == 1:
            j *= factor[0]
    tansaku =  bisect_right(S, N//j)
    ans += tansaku

print(ans)