def judge_B(S):
    judge_set = set()
    for i, s in enumerate(S):
        if s == 'B':
            judge_set.add(i%2)

    if len(judge_set) == 2:
        return True
    else:
        return False


def judge_KR(S):
    R = []
    k = -1
    for i, s in enumerate(S):
        if s == 'K':
            k = i
        if s == 'R':
            R.append(i)

    if R[0] < k < R[1]:
        return True
    else:
        return False           


S = input()

if judge_B(S) and judge_KR(S):
    print('Yes')
else:
    print('No')