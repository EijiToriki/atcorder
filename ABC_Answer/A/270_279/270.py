A, B = map(int, input().split())

score_dict = {0:'000', 1:'001', 2:'010', 3:'011', 4:'100', 5:'101', 6:'110', 7:'111', }

Abit = score_dict[A]
Bbit = score_dict[B]

i = 0
ans = 0
for abit, bbit in zip(Abit, Bbit):
    if abit == '1' or bbit == '1':
        ans += 2**(2-i)
    i+=1

print(ans)