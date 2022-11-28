from bisect import bisect
from collections import defaultdict

def main(N, A):
    sort_A = list((sorted(set(A))))
    sort_A_len = len(sort_A)
    ans_dict = defaultdict(int)

    for i in range(N):
        ans = sort_A_len - bisect(sort_A, A[i])
        ans_dict[ans] += 1
    
    for i in range(N):
        print(ans_dict[i])

    

 
if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    main(N, A)