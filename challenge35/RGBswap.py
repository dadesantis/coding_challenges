# Organizes the characters in the array using swaps, such
# that they end up in the order RGB
def swap(letters):
    # Keep track of the R and G indexes
    r_index = 0

    # First, place all the Rs in the beginning
    # at the appropriate index. Keep track of the last r_index.
    for i in range(0, len(letters)):
        if letters[i] is 'R':
            letters[i], letters[r_index] = letters[r_index], letters[i]
            if r_index + 1 < len(letters):
                r_index += 1

    # Next, place all Gs after the Rs. Pick up at the index after
    # the last r_index.
    g_index = r_index + 1
    for i in range(g_index, len(letters)):
        if letters[i] is 'G':
            letters[i], letters[g_index] = letters[g_index], letters[i]
            if g_index + 1 < len(letters):
                g_index += 1

    # The Bs have been sorted as a result of the other swaps, so return the sorted array.
    return letters
