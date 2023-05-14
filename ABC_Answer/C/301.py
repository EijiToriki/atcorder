from collections import defaultdict

S = input()
T = input()

s_dict, t_dict = defaultdict(int), defaultdict(int)

for s,t in zip(S, T):
    s_dict[s] += 1
    t_dict[t] += 1

atcoder = ['a', 't', 'c', 'o', 'd', 'e', 'r']
alpha = [chr(i) for i in range(97, 97+26)]

for a in alpha:
    if a not in atcoder:
        if s_dict[a] != t_dict[a]:
            print('No')
            exit()

s_diff = 0
t_diff = 0
for a in atcoder:
    if s_dict[a] > t_dict[a]:
        t_diff += s_dict[a] - t_dict[a]
    elif s_dict[a] < t_dict[a]:
        s_diff += t_dict[a] - s_dict[a]

if s_diff <= s_dict['@'] and t_diff <= t_dict['@']:
    print('Yes')
else:
    print('No')
