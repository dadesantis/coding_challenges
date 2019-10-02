# Encode a sequence of letters by counting their occurrences
def encode(sequence):
    code = ''
    count = 0

    # Count the occurrences of a letter until the next letter comes up
    # Add the count and letter to the code
    for i in range(0, len(sequence)):
        count += 1
        if i == len(sequence)-1:
            code += str(count) + sequence[i]
        elif sequence[i] != sequence[i+1]:
            code += str(count) + sequence[i]
            count = 0
    return code


# Decode the alphanumeric string
def decode(code):
    sequence = ''

    # Print the given letter (always in the 2i+1 spot) a number (in the 2i spot) of times
    for i in range(0, len(code)-1, 2):
        letter = code[i+1]
        multiplier = int(code[i])
        sequence += str(letter*multiplier)
    return sequence


def main():
    seq = ['AAAABBBCCDDD', 'ABCABCABC', 'AAB', 'A']

    for it in seq:
        code = encode(it)
        print('encoded:', code)
        print('decoded:', decode(code), '\n')


if __name__ == '__main__':
    main()
