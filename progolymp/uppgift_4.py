def main():
    dna = input("Björns protein ? ")
    k = int(input("k ? "))
    original_dna = dna
    forbidden_letters = find_forbidden_letters(dna)
    for forbidden_letter in forbidden_letters:
        amount_of_hidden_letter = count(dna, forbidden_letter)
        while len(dna) > amount_of_hidden_letter:
            print(forbidden_letter)
            smallest_substr, index = find_smallest_substr_with_unique_letters(
                dna, forbidden_letter, k
            )
            print(smallest_substr)
            dna = dna[:index] + dna[index + len(smallest_substr) :]
            print(dna)
        dna = original_dna


def find_forbidden_letters(string):
    saved_chars = []
    forbidden = []
    for i, char in enumerate(string):
        if char in saved_chars and char not in forbidden:
            forbidden.append(char)
        else:
            saved_chars.append(char)

    return forbidden


def find_smallest_substr_with_unique_letters(string, forbidden_letter, max_length):
    # print(string)
    # print(forbidden_letters)
    substrings = []
    for i, char in enumerate(string):
        if char == forbidden_letter:
            continue
        current_substr = char
        for j, new_char in enumerate(string[i + 1 :]):
            if new_char != current_substr[-1] and new_char != forbidden_letter:
                # print(count(string, new_char))
                # print(new_char)
                current_substr += new_char
                # print(current_substr)
            else:
                # print(char)
                # print(longest_substr)
                break
        if len(current_substr) < max_length:
            substrings.append(current_substr)
    min = float("inf")
    min_str = ""
    for substring in substrings:
        if len(substring) < min:
            min = len(substring)
            min_str = substring
    # print(string, min_str)
    lowest_index = string.find(min_str)
    # highest_index = string.rfind(min_str)
    # print(lowest_index)
    return min_str, lowest_index


def count(string, char):
    sum = 0
    for character in string:
        if character == char:
            sum += 1

    return sum


# print(count("exempelfall", "e"))
# print(find_smallest_substr_with_unique_letters("exempelfall", 4))
main()

# print(find_forbidden_letters("hej")
