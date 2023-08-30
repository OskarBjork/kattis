import math

my_set = {"one", "two", "three"}

for i in my_set:
    pass
    # print(i)

dic = {"Sverige": "Stockholm", "Norge": "Oslo", "Finland": "Helsingfors"}


def tal_under_tusen_delbart_med_sju():
    for i in range(1000):
        if not i % 7:
            print(i)


def antal_siffror(string):
    return_value = 0
    for char in string:
        if char in list(map(lambda x: str(x), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])):
            return_value += 1
    return return_value


def is_prime(n):
    if n == 1 or n == 2:
        return True

    for num in range(2, n):
        if n % num == 0:
            return False
    return True


def thousand_prime():
    primes = [1, 2]
    current_number = 2
    while len(primes) < 1002:
        if is_prime(current_number):
            primes.append(current_number)
        current_number += 1
    return primes[-1]


def product_ten_digits_prime():
    primes = [1, 2]
    current_number = 2
    while True:
        if is_prime(current_number):
            primes.append(current_number)
            if len(str(primes[-1] * primes[-2])) >= 10:
                return primes[-1], primes[-2]

        current_number += 1


# print(thousand_prime())

print(product_ten_digits_prime())

# print("Före")
# for i in range(2, 3):
#     print(i)
# # end for
# print("Efter")
# print(antal_siffror("dwd2921nd729"))


# tal_under_tusen_delbart_med_sju()
