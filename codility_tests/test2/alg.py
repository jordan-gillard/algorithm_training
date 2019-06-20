from string import ascii_letters


def solution(string: str):
    if not string:
        return 0
    in_word = False
    word_count = 0
    for letter in string.strip():
        if letter in ascii_letters and not in_word:
            word_count += 1
            in_word = True
        if letter == ' ':
            in_word = False
    return word_count
