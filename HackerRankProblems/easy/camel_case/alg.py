from string import ascii_uppercase


def camel_case(string: str) -> int:
    if not string:
        return 0
    num_of_words = 1
    for letter in string:
        if letter in ascii_uppercase:
            num_of_words += 1
    return num_of_words
