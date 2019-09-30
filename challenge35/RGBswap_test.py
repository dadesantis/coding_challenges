import random
import time as t
from RGBswap import swap


def generate_rgb_list(num_items):
    options = ['R', 'G', 'B']
    items = []

    for i in range(0, num_items):
        items.append(random.choice(options))

    return items


def main():
    max_nums = 10000
    min_nums = max_nums // 10
    inc = 1000

    print("Example:")
    ex = generate_rgb_list(15)
    print(ex)
    swap(ex)
    print(ex)
    print('- '*24)

    for i in range(min_nums, max_nums+inc, inc):
        test_list = generate_rgb_list(i)
        start = t.perf_counter()
        swap(test_list)
        print('swap time for {} items: {}ms'.format(i, (t.perf_counter() - start)*10**3))
        print('- '*24)


if __name__ == '__main__':
    main()
