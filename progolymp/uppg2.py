def main():
    n = int(input("N ? "))
    valid_list = []
    # print([x for x in range(n)])

    for num in range(1, n):
        if num * (num + 1) * (num + 2) < n:
            valid_list.append(num)

    print(len(valid_list))
    pass


main()
