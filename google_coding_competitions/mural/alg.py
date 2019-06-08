import math


num_test_cases = int(input())
for case in range(num_test_cases):
    size_of_wall = int(input())
    wall = [int(i) for i in input()]
    max_mural_size = math.ceil(size_of_wall / 2)
    highest_so_far = 0
    for i in range(max_mural_size):
        highest_so_far += wall[i]
    highest = highest_so_far
    for i in range(max_mural_size, len(wall)):
        highest += wall[i]
        highest -= wall[i - max_mural_size]
        highest_so_far = max(highest_so_far, highest)
    case_num = case + 1
    print('Case #{}: {}'.format(case_num, highest_so_far))
