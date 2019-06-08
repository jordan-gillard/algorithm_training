"""Taken from www.hackerrank.com/challenges/reduced-string/"""


def reduced_string(string: str) -> str:
    done = True
    starter = 1
    while not done or starter == 1:
        i: int = 0
        done = True
        starter += 1
        while i < (len(string)-1):
            if string[i] == string[i + 1]:
                string = string[:i] + string[i+2:]
                done = False
            else:
                i += 1
    return string if string else 'Empty String'
