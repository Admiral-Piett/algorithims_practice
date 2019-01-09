# number of trials = n squared * natural log of n
# https://www.coursera.org/learn/algorithms-divide-conquer/lecture/4TLKM/analysis-of-contraction-algorithm 27:50
import random
import copy
import math


def read_file(file):
    sample = dict()
    with open(file) as f:
        for line in f:
            line = line.strip().split('\t')
            key = int(line.pop(0))
            value = [int(i) for i in line]
            sample[key] = value
        return sample


class MinCut():

    def __init__(self, sample):
        self.org_sample = sample
        # print(self.sample[10])
        self.min_cuts = len(sample)
    
    def run_me(self, times):
        # if times is False:
        #     times = int((len(sample) ** 2) * math.log(len(sample)))
        #     print(times)
        
        for i in range(0, times):
            self.sample = copy.deepcopy(self.org_sample)
            cuts = self.count_cuts()
            if cuts < self.min_cuts:
                self.min_cuts = cuts
            print(self.min_cuts)
        
        return self.min_cuts

    def count_cuts(self):
        # returns randomly selected vertex and edge to merge
        while len(self.sample) > 2:
            self.vert, self.edge = self.get_random_verticies_and_edge(self.sample)
            # print('self vert', self.vert)
            # print('self edge', self.edge)
            self.merge_edge(self.vert, self.edge)
        # print(self.sample)
        return len(self.sample[list(self.sample.keys())[0]])


    def get_random_verticies_and_edge(self, sample):
        key_list = list(sample.keys())
        vert = key_list[random.randint(0, len(key_list)) - 1]
        edge = sample[vert][random.randint(0, len(sample[vert]) - 1)]
        return vert, edge

    def merge_edge(self, a, b):
        # Merges the verticies a and b, extends a's edges with b's edges
        # and removes the b vertex from the dictionary
        # print(sample)
        self.sample[a].extend(self.sample.pop(b))

        for k, v in self.sample.items():
            # Replaces any edges pointing to old vertex (b) with a vertex value
            self.sample[k] = [a if i == b else i for i in self.sample[k]]

        # removes any edges pointing back at this vertex (self loops)
        self.sample[a] = [i for i in self.sample[a] if i != a]







if __name__ == '__main__':
    sample = read_file('random_contraction_min_cut_file.txt')
    # print(sample)
    # print(len(sample))

    min_cut = MinCut(sample)
    print(min_cut.run_me(100))
    # get_random_verticies_and_edge(sample)