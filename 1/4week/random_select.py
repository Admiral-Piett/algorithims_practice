import random

def generate_sameple(lower, upper, length):
    # This generates all unique numbers anyway so the total should always be the length of the range
    # return random.sample(range(lower, upper), upper)
    return random.sample(range(lower, upper), length)

class RandomSelect():

    def run_me(self, sample, element_index):
        self.element_index = element_index
        return self.random_select(sample)
    
    def pick_pivot(self, low, high):
        return random.randint(low, high)

    def random_select(self, arr):
        if len(arr) <= 1:
            return arr
        else:
            # print('element_index', self.element_index)

            # Partioning
            pivot = arr.pop(self.pick_pivot(0, len(arr)-1))
            
            i = 0
            # print('start', arr)
            for j in range(0, len(arr)):
                if arr[j] < pivot:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
                else:
                    continue
            arr.insert(i, pivot)
            # print(arr)


            if i == self.element_index:
                return pivot
            elif i < self.element_index:
                # If the element index that we're looking for is still greater than i, we need to chop off everything less that i (including i)
                # and account for that in the new index.  So would be my original index minus i.
                self.element_index -= i
                return self.random_select(arr[i:])
            else:
                # If the element index is less than i, the index will still be fine, since we're only removing things that are coming after the index.
                # So just chop off the i and everything greater than it and recurse
                return self.random_select(arr[:i])



if __name__ == '__main__':
    sample = generate_sameple(0, 1000, 100)
    print(sample)

    r_select = RandomSelect()
    print(r_select.run_me(sample, 43))