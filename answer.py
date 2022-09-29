from bisect import bisect_left, bisect_right


N = int(input())

X_list = []
for i in range(10**2+1):
    X_list.append((2*i)*(2*(i**2)))

if N in X_list:
    start_idx = bisect_left(X_list, N)
else:
    start_idx = bisect_left(X_list, N) - 1
print(start_idx)

ans_candidate_list = []
for i in range(start_idx+1):
    val = (2*start_idx)*(i**2 + (2*start_idx-i)**2)
    ans_candidate_list.append(val)

for i in range(2*start_idx):
    val = (2*start_idx+1)*(i**2 + (2*start_idx-i+1)**2)
    ans_candidate_list.append(val)

ans_candidate_list = sorted(ans_candidate_list)

if N in ans_candidate_list:
    ans_idx = bisect_left(ans_candidate_list, N) - 1
else:
    ans_idx = bisect_left(ans_candidate_list, N) 

print(ans_candidate_list)
print(ans_candidate_list[ans_idx])