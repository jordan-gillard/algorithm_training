from functools import lru_cache
from time import sleep


@lru_cache(maxsize=None)
def playing_with_lru_cache(n):
    sleep(5)
    print("I slept!")
    return n


if __name__ == '__main__':
    print(playing_with_lru_cache(5))
    print(playing_with_lru_cache(5))
