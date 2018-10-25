def fibo(i):
    if i == 0 or i == 1:
        return i
    else:
        return fibo(i-1) + fibo(i-2)


def main():
    i = int(raw_input())
    print fibo(i)


if __name__ == "__main__":
    main()
