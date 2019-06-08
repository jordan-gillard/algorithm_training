from typing import List


def grading_students(grades: List[int]) -> List[int]:
    rounded_grades: List[int] = []
    for i in grades:
        if i < 38 or i % 5 < 3:
            pass
        else:
            i += 5 - (i % 5)
        rounded_grades.append(i)
    return rounded_grades
