N = int(input())

div3 = N // 3
div5 = N // 5
div15 = N // 15

ans = (div3 + div5) - div15
print(ans)