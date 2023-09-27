def main():
    n = int(input())
    temperatures = input().split()

    print(len([x for x in temperatures if int(x) < 0]))


main()
