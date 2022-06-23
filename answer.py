N = int(input())

cr_brackets_list = []

if N%2 == 0:
    for i in range(2**N):
        ans_list = []
        for j in range(N):
            if(i>>j & 1):
                ans_list.append(')')
            else:
                ans_list.append('(')

        if ans_list[0] == '(':
            left = 0
            right = 0
            ans_flag = True
            for j in range(N):
                if ans_list[j] == '(':
                    left += 1
                else:
                    right += 1
                if left < right:
                    flag = False
                    break
            if ans_flag and left == right:
                cr_brackets_list.append(''.join(ans_list))

cr_brackets_list = sorted(cr_brackets_list)

for cr_branket in cr_brackets_list:
    print(cr_branket)


