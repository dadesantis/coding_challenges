import time as t

# Returns the only non-repeating digit in a list of integers
# TODO: do this w/o help from Python
def find_singleton(nums):
    num_set = set(nums)
    for num in num_set:
        if nums.count(num) == 2 or nums.count(num) > 3:
            return "Invalid sequence"
        elif nums.count(num) == 1:
            return num
    return "Invalid sequence"


def main():
    cases = [[1, 1, 1, 2, 3, 3, 3],
             [4, 4, 1, 1, 4, 1, 5, 1],
             [5, 1, 5, 1, 3, 1, 5, 4, 4, 4],
             [4, 5, 1, 2, 5, 5, 9, 1, 4, 4, 2, 2, 1],
             []]

    for test in cases:
        start = t.perf_counter()
        result = find_singleton(test)
        print('result = {} in {}s'.format(result, t.perf_counter() - start))


if __name__ == '__main__':
    main()
