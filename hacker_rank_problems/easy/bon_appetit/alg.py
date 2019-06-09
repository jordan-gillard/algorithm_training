"""Taken from www.hackerrank.com/challenges/bon-appetit/"""
from typing import Union, List


def bon_appetit(bill: List[int], declined: int, anna_cont: int) -> Union[str, int]:
    bill.pop(declined)
    anna_should_pay = sum(bill) / 2
    if anna_should_pay != anna_cont:
        return int(anna_cont - anna_should_pay)
    return 'Bon Appetit'
