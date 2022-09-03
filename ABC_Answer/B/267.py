import sys

S = input()

column = [[7], [4], [2,8], [1,5], [3,9], [6], [10]]

if S[0] == '1':
    print('No')
else:
    stand_up = []
    for i in range(1, 10):
        if S[i] == '1':
            stand_up.append(i+1)
    exist_column = []
    for s in stand_up:
        for i, c in enumerate(column):
            if s in c:
                if i not in exist_column:
                    exist_column.append(i)
    
    exist_column = sorted(exist_column)
    for i in range(len(exist_column)-1):
        if exist_column[i+1] - exist_column[i] != 1:
            print('Yes')
            sys.exit()
    print('No')