from python_algs_book.functools.lru_cache_playing import playing_with_lru_cache


def test_lru_func():
    from timeit import timeit
    playing_with_lru_cache(5)
    playing_with_lru_cache(5)
