import sys

def make_ranlength(str):
    focus_char = str[0]
    cnt = 1
    return_list = []
    for i in range(1,len(str)):
        if focus_char == str[i]:
            cnt += 1
        else:
            return_list.append((focus_char, cnt))
            cnt = 1
            focus_char = str[i]
    return_list.append((focus_char, cnt))

    return return_list


S = input()
T = input()

s_list = make_ranlength(S)
t_list = make_ranlength(T)

if len(s_list) != len(t_list):
    print('No')
    sys.exit()
else:
    for i in range(len(s_list)):
        if s_list[i][0] != t_list[i][0]:
            print('No')
            sys.exit()
        if s_list[i][1] > t_list[i][1]:
            print('No')
            sys.exit()
        if s_list[i][1] == 1 and t_list[i][1] >= 2:
            print('No')
            sys.exit()

print('Yes')