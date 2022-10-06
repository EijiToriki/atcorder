S = input()
Q = int(input())

for _ in range(Q):
    t, k = map(int, input().split())
    sLen = len(S)

    if t == 0:
        print(S[k-1])
    else:
        move_cnt = 0
        while True:
            if  sLen > k-1:
                break
            else:
                sLen *= 2
                move_cnt += 1
        
        one_len = 2 ** move_cnt
        base_index = (k-1) // one_len
        ans_index = (k-1) % one_len

        ans_index = bin(ans_index)[2:]

        ans = S[base_index]
        for idx in ans_index:
            if idx == '0':
                if ans == 'A':
                    ans = 'B'
                elif ans == 'B':
                    ans = 'C'
                elif ans == 'C':
                    ans = 'A'
            else:
                if ans == 'A':
                    ans = 'C'
                elif ans == 'B':
                    ans = 'A'
                elif ans == 'C':
                    ans = 'B'
        
        print(ans)
    

