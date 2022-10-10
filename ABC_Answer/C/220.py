def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())

    A_sum = sum(A)
    ans = (X // A_sum) * N
    val = (X // A_sum) * A_sum
    for a in A:
        if val > X:
            break
        val += a
        ans += 1
    
    print(ans)


if __name__ == "__main__":
    main()