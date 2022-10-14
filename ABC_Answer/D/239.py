import math

def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True

def main(A, B, C, D):
    prime_set = set()
    for i in range(2, 201):
        if is_prime(i):
            prime_set.add(i)

    for takahashi in range(A, B+1):
        takahashi_flag = False
        for aoki in range(C, D+1):
            if (takahashi + aoki) in prime_set:
                takahashi_flag = False
                break
            takahashi_flag = True
        
        if takahashi_flag:
            print("Takahashi")
            exit()
    
    print("Aoki")

 
if __name__ == '__main__':
    A, B, C, D = map(int, input().split())
    main(A, B, C, D)