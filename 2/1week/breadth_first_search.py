# Thoughts
# 1. pass in first point to queue
# 2. Queue mark entries as explored (if unexplored) and pop them from queue (need a loop for all the entries passed in)
#     2.1 append all connected endpoints of entry to queue and recurse.

import os
import sys
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '../..')))
from helpers.generate_graph_dict import GenerateGraphDict

class BreadthFirstSearch():

    def __init__(self, graph, start=False, end=False):
        self.graph = graph
        self.explored_verticies = set()
        self.distance = dict()
        self.queue = []
        self.start = start
        self.end = end

    def run_me(self):
        self.queue.append(self.pick_start_vertex())

        print('START', self.queue[0], '\n')
        self.search()

        if self.end is not False:
            return {self.end: self.distance[self.end]}
        else:
            return self.distance

    def search(self):

        # for i in self.queue:
        while len(self.queue) >= 1:
            i = self.queue.pop(0)
            # print('cur_int', i)
            # print('queue before loop', self.queue)
            for j in self.graph[i]:
                if j not in self.explored_verticies:
                    # i isn't getting set properly, some values that haven't been seen before are getting set to i and they have no distance because of that
                    self.distance[j] = self.distance[i] + 1

                    self.explored_verticies.add(j)
                    self.queue.append(j)
                    # print('explored', self.explored_verticies)
                    # print('queue', self.queue, '\n')
                else:
                    # print('already explored, queue -', self.queue)
                    continue



    def pick_start_vertex(self):
        if self.start is not False:
            self.queue.append(self.start)
            self.distance[self.start] = 0
            self.explored_verticies.add(self.start)
            return self.start
        else:
            vert = random.randint(1, len(graph))
            self.distance[vert] = 0
            self.explored_verticies.add(vert)
            return vert

if __name__ == '__main__':
    g = GenerateGraphDict(1000, 5)
    graph = g.generate_graph()

    for k, v in graph.items():
        print('key', k, 'value', v)
    print('\n\n')

    bSearch = BreadthFirstSearch(graph, start=1, end=650)
    distances = bSearch.run_me()
    print('DISTANCES')
    for k, v, in distances.items():
        print('key', k, 'value', v)

