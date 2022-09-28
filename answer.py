N = input()
keta = len(N)

ans_option = []
for i in range(2**keta):
    r = []
    l = []
    for j in range(keta):
        if((i >> j) & 1):
            r.append(int(N[j]))
        else:
            l.append(int(N[j]))
    
    if len(r) != 0 and len(l) != 0:
        r = sorted(r)
        r_num = 0
        for k in range(len(r)):
            r_num += r[k] * (10 ** k)
        
        l = sorted(l)
        l_num = 0
        for k in range(len(l)):
            l_num += l[k] * (10 ** k)
        
        ans_option.append(r_num*l_num)

print(max(ans_option))