def main(N,A):
    ans = 0
    idx = 0
    prev = -1
    prev_cnt = 1

    while idx < N:
        ans += 1
        if A[idx] == prev:
            prev_cnt += 1
            if prev_cnt == prev:
                ans = ans - prev
        else:
            prev_cnt = 1
            prev = A[idx]
            
        print(ans)
        idx += 1
 
 
if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    main(N,A)