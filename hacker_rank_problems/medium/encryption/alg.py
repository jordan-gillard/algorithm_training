import math


def encryption(sentence: str) -> str:
    sqrt_len: float = math.sqrt(len(sentence))
    num_col: int = math.ceil(sqrt_len)
    s_no_space: str = sentence.replace(' ', '')
    rows: list = []
    for i in range(num_col):
        i = i * num_col
        new_row = s_no_space[i: i+num_col]
        rows.append(new_row)
    encrypted_sentence: str = ''
    for i in range(num_col):
        for word in rows:
            try:
                encrypted_sentence += word[i]
            except IndexError:
                continue
        encrypted_sentence += ' '
    return encrypted_sentence.rstrip()
