def fizz_buzz():
    x, y, n = tuple(input().split())
    x, y, n = int(x), int(y), int(n)

    for num in range(1, n + 1):
        if num % x == 0 and num % y == 0:
            print("FizzBuzz")
        elif num % x == 0:
            print("Fizz")
        elif num % y == 0:
            print("Buzz")
        else:
            print(num)


fizz_buzz()
