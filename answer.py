import sys
 
S = input()
T = input()
 
if S[0] != T[0] or S[1] != T[1]:
    print('No')
    sys.exit()
 
t_index = 2
for i in range(1, len(S)-1):
    if S[i+1] != T[t_index]:
        if S[i] == S[i-1]:
            focus_char = S[i]
            while True:
                if focus_char != T[t_index]:
                    break
                t_index += 1
        else:
            print('No')
            sys.exit()
    else:
        t_index += 1
 
if S[-1] != S[-2] and len(T[t_index:]) != 1:
    print('No')
    sys.exit()
 
print('Yes')