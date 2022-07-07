def count_number(n):
    keta = 1
    result = 0

    while True:
        under = 10**(keta-1) - 1
        top = min(n, 10**(keta)-1)
        result += keta * (top*(top+1) // 2 - under*(under+1) // 2)

        if len(str(n)) == keta:
            return result
        
        keta += 1



L,R = map(int, input().split())
MOD = 10**9+7

print((count_number(R)-count_number(L-1))%MOD)