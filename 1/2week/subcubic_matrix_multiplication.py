import random

def generate_matrix_sameple(lower, upper, row_length, row_number):
    arr = []
    # This generates all unique numbers anyway so the total should always be the length of the range
    for i in range(0, row_number):
        arr.append(random.sample(range(lower, upper), row_length))

    return arr

sample = generate_matrix_sameple(0, 10, 10, 10)
print(sample)

