def backwards(string):
    return " ".join(string.split()[::-1])


def backwards_string(string):
    return string[::-1]


def rovar_sprak(
    string, vokal_symbol_list=("a", "e", "o", "u", "e", "i", "y", "ä", "ö", "?", "!")
):
    return "".join(
        [
            letter + "o" + letter if letter not in vokal_symbol_list else letter
            for letter in string
        ]
    )


print(backwards("Hej på dig!"))
print(backwards_string("hello world"))

my_list = [1, 2, 3]

my_list.reverse()
