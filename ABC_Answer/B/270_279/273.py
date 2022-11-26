from decimal import Decimal, ROUND_HALF_UP

def main(X, K):
    for i in range(1, K+1):
        X = str(X)
        X = int(Decimal(X).quantize(Decimal('1E'+str(i)), rounding=ROUND_HALF_UP))
    
    print(X)

 
if __name__ == '__main__':
    X, K = map(int, input().split())
    main(X, K)