def judge(s):
    seq_num = 1
    judge_num = 0
    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            seq_num += 1
        else:
            judge_num = max(judge_num, seq_num)
            seq_num = 1
    judge_num = max(judge_num, seq_num)

    if judge_num >= 3:
        return True
    else:
        return False


N = int(input())
S = input()

if judge(S):
    print('Yes')
else:
    print('No')