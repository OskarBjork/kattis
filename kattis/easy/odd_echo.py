def odd_echo():
    number_of_inputs = int(input())

    for i in range(number_of_inputs):
        string = input()

        if not (i - 1) % 2 == 0:
            print(string)


odd_echo()
