# Find the edit distance between two strings
def edit_length(first, second):
    dist = 0

    # Add the difference of the larger and smaller string
    # to account for the distance of appending chars
    larger = max(len(first), len(second))
    smaller = min(len(first), len(second))
    dist += (larger-smaller)

    # For each character that needs to be changed, add to the distance
    for l in range(0, smaller):
        if first[l] != second[l]:
            dist += 1

    return dist

# TODO: Unit testing?
def main():
    words = ['kitten', 'sitting', 'bicycle', 'since', 'kite', 'entity']

    for i in range(0, len(words)):
        print("The edit distance between {} and {} is {}".format(words[0], words[i], edit_length(words[0], words[i])))


if __name__ == '__main__':
    main()
