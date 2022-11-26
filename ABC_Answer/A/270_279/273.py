def f(n):
    if n==0:
        return 1
    else:
        return n * f(n-1)

def main(N):
    ans = f(N)
    print(ans)
    
 
if __name__ == '__main__':
    N = int(input())
    main(N)