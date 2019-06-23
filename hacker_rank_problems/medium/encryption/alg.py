import math


def encryption(sentence: str) -> str:
    sqrt_len: float = math.sqrt(len(sentence))
    num_col: int = math.ceil(sqrt_len)
    s_no_space: str = sentence.replace(' ', '')
    rows: list = [""] * num_col
    for i in range(num_col):
        i = i * num_col
        new_row = s_no_space[i: i+num_col]
        for i in range(len(new_row)):
            rows[i] += new_row[i]
    return ' '.join(rows)
