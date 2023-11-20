def main():
    dna = input("Björns protein ? ")
    k = int(input("k ? "))
    original_dna = dna
    forbidden_letters = find_forbidden_letters(dna)
    smallest_moves = float("inf")
    for forbidden_letter in forbidden_letters:
        # print("\n")
        # print("Forbidden letter: ", forbidden_letter, "\n")
        current_moves = 0
        amount_of_hidden_letter = count(dna, forbidden_letter)
        while len(dna) > amount_of_hidden_letter:
            # print("DNA: ", dna)
            smallest_substr, index = find_smallest_substr_with_unique_letters(
                dna, forbidden_letter, k
            )
            # print("Smallest substr: ", smallest_substr)
            dna = dna[:index] + dna[index + len(smallest_substr) :]
            current_moves += 1

        if current_moves < smallest_moves:
            smallest_moves = current_moves
        dna = original_dna

    print(smallest_moves)


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

        if len(current_substr) <= max_length and len(current_substr) > 1:
            substrings.append(current_substr)

        if len(
            current_substr
        ) == 1 and not list_contains_element_that_is_longer_than_one(substrings):
            substrings.append(current_substr)
        # if list_contains_element_that_is_longer_than_one(substrings):
        #     substrings = [x for x in substrings if len(x) > 1]
    max = float("-inf")
    max_str = ""
    for substring in substrings:
        if len(substring) > max:
            max = len(substring)
            max_str = substring
    # print(string, min_str)
    lowest_index = string.find(max_str)
    # highest_index = string.rfind(min_str)
    # print(lowest_index)
    return max_str, lowest_index


def allowed_to_remove_forbidden_letter(string, forbidden_letter, index):
    try:
        if string[index + 1] != forbidden_letter:
            return True
        else:
            return False
    except IndexError:
        return False


def list_contains_element_that_is_longer_than_one(list):
    for i in list:
        if len(i) > 1:
            return True
    return False


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
