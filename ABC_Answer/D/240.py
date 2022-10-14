from collections import deque

def main(N,A):
    stack = deque([])
    ans = 0

    for i in range(N):
        if len(stack) == 0:
            stack.append([A[i], 1])
            ans = 1
        else:
            prev = stack.pop()
            if prev[0] == A[i]:
                if prev[1] + 1 < A[i]:
                    stack.append([prev[0], prev[1]+1])
                    ans += 1
                else:
                    ans -= (A[i] - 1)
            else:
                stack.append(prev)
                stack.append([A[i], 1])
                ans += 1
    
        print(ans)
 
 
if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    main(N,A)