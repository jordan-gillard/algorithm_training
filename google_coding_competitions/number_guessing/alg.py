num_test_cases = int(input())

for _ in range(num_test_cases):
    lower_b, upper_b = [int(s) for s in input().split(" ")]
    upper_b += 1
    guesses = 0
    max_guesses = int(input())
    response = ''
    while response != 'CORRECT' and guesses <= max_guesses:
        if response == 'TOO_SMALL':
            lower_b = ((upper_b + lower_b) // 2)
        elif response == 'TOO_BIG':
            upper_b = ((upper_b + lower_b) // 2)
        guess = (upper_b + lower_b) // 2
        print(guess, flush=True)
        guesses += 1
        response = input()
