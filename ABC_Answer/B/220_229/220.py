from unittest import result


def main():
    def k_to_10(k, x):
        result = 0
        for i, keta in enumerate(reversed(str(x))):
            result += int(keta) * (k ** i)
        return result
            
    K = int(input())
    A, B = map(int, input().split())

    A10 = k_to_10(K, A)
    B10 = k_to_10(K, B)

    print(A10 * B10)

if __name__ == "__main__":
    main()