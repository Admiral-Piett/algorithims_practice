import random

# @profile
def generate_sameple(lower, upper):
    # This generates all unique numbers anyway so the total should always be the length of the range
    return random.sample(range(lower, upper), upper)

sample = generate_sameple(0, 1000000)

def count_random_numbers(input):

    checked = set()

    # @profile
    def audit_list(input):
        for i in input:
            if i not in checked:
                # Sets will only add unique values so this will be an unordered list of all the unique values from the input.
                # That should be fine since we only care about how many values are unique from the input anyway.
                checked.add(i)

    audit_list(input)
    return len(checked)

print('Results:', count_random_numbers(sample))
