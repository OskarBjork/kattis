def find_earth_value_from_language(alien_number, alien_language):
    earth_language = "0123456789"

    base_in_alien_language = len(alien_language)

    value_in_earth_numbers = 0
    for i, char in enumerate(alien_number[::-1]):
        value_in_earth_numbers += (
            alien_language.index(char) * base_in_alien_language**i
        )

    return value_in_earth_numbers


def convert_earth_number_in_n_base_to_target_language(num, target_language):
    alien_value = ""  # De är båda i samma bas nu

    for i, digit in enumerate(num):
        alien_value += target_language[int(digit)]

    return alien_value


def convert_earth_number_to_target_base(earth_number, target_language):
    target_language_base = len(target_language)

    number_in_n_base = ""

    while earth_number >= 1:
        digit = str(earth_number % target_language_base)
        number_in_n_base += digit
        earth_number //= target_language_base

    return number_in_n_base[::-1]


def alien_language():
    T = int(input())
    case_outputs = []
    for i in range(T):
        value = 0

        alien_number, source_language, target_language = tuple(input().split())
        source_language = list(source_language)

        earth_value = find_earth_value_from_language(alien_number, source_language)

        earth_value_in_n_base = convert_earth_number_to_target_base(
            earth_value, target_language
        )

        case_outputs.append(
            convert_earth_number_in_n_base_to_target_language(
                earth_value_in_n_base, target_language
            )
        )

    for i, output in enumerate(case_outputs):
        print(f"Case #{i+1}: {output}")
    pass


alien_language()
