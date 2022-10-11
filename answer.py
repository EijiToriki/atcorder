

from bisect import bisect, bisect_left, bisect_right, insort_left


def main(Q):  
    A = []  
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            insort_left(A, query[1])
        if query[0] == 2:
            idx = bisect_right(A, query[1])
            if idx - query[2] < 0:
                print(-1)
            else:
                print(A[idx-query[2]])
        if query[0] == 3:
            idx = bisect_left(A, query[1])
            if idx + query[2] - 1 >= len(A):
                print(-1)
            else:
                print(A[idx+query[2]-1])



if __name__ == "__main__":
    Q = int(input())
    main(Q)