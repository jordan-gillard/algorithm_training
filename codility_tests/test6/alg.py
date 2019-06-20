def solution(word: str):
    last_index = len(word) - 1
    for i in range(len(word)):
        if (word[i] != word[last_index - i] and ((word[i] == word[last_index - i].lower()) or
                                                 (word[i].lower() == word[last_index - i]))) is False:
            return False
    return True
