import argparse


def main(args):
    print(f'Args are {args}')
    print(f'Args type is {type(args)}')
    num_test_cases, guess_range_low, guess_range_high, max_guesses = args
    while True:
        guess = (guess_range_low + guess_range_high) // 2
        print(guess)
        parser = argparse.ArgumentParser()
        parser.add_argument('response')
        args = parser.parse_args()
        if args.response == 'TOO_BIG':
            guess_range_high = (guess_range_low + guess_range_high) // 2
        elif args.response == 'TOO_SMALL':
            guess_range_low = (guess_range_low + guess_range_high) // 2
        else:
            break


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('num_of_tests')
    parser.add_argument('guess_low')
    parser.add_argument('guess_high')
    parser.add_argument('max_guesses')
    args = parser.parse_args()
    print(f'args are {args}')
    main(args)
