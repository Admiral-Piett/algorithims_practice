import random

class GenerateUnsortedArray():

    def generate_sameple(self, lower, upper):
        # This generates all unique numbers anyway so the total should always be the length of the range
        return random.sample(range(lower, upper), upper)