import sys

def reverse_and_add(number_str):
    iterations = 0
    number_str_reversed = number_str[::-1]
    while number_str_reversed != number_str:
        iterations += 1
        number_str = str(int(number_str) + int(number_str_reversed))
        number_str_reversed = number_str[::-1]

    return (iterations, number_str_reversed)


if __name__ == '__main__':
    with open(sys.argv[1], "r") as test_cases:
        for test in test_cases:
            i, result = reverse_and_add(test.replace("\n", ""))
            print "%d %s" % (i, result)
