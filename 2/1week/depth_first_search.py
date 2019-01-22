# This is basically breadth first search, except instead of a queue we use a stack
# stacks pull values from the back which allows it to easily retrace it's steps
# RECURSION - is naturally the way to go with depth first seach

# This works, however, it will not find unconnected verticies.
# Tested with directional graph and it will omit endpoints that are not directly connected to start
# Could adapt code if needed - ~8 minutes in, https://www.coursera.org/learn/algorithms-graphs-data-structures/lecture/BTVWn/bfs-and-undirected-connectivity 

import os
import sys
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '../..')))
from helpers.generate_graph_dict import GenerateGraphDict

class DepthFirstSearch():

    def __init__(self, graph, start=False):
        self.graph = graph
        self.start = self.handle_start(start)
        print('start', self.start, '\n')
        self.explored = list()
        # This is more how many steps it took to get there rather than the actual distance from the start
        self.distance = dict()


    def handle_start(self, start):
        if start is False:
            return random.randint(1, len(self.graph))
        else:
            return start

    def search(self, graph, vert, distance):
        # self.explored.add(vert)
        self.explored.append(vert)
        self.distance[vert] = distance
        for i in graph[vert]:
            # print('Checking - {0}'.format(i))
            if i not in self.explored:
                # print(list(self.explored))
                distance += 1
                self.search(graph, i, distance)
            # else:
                # print('ALREADY EXPLORED - {0}'.format(i))

    def run_me(self):
        self.search(self.graph, self.start, 0)
        return self.distance


class DepthFirstSearchWholistic(DepthFirstSearch):

    def run_me_wholistic(self):
        self.run_me()

        for i in range(1, len(self.graph) + 1):
            if i not in self.explored:
                self.search(self.graph, i, 0)

        return self.distance




if __name__ == '__main__':
    g = GenerateGraphDict(10, 5)
    graph = g.generate_graph()

    for k, v in graph.items():
        print('key', k, 'value', v)
    print('\n\n')

    dfs = DepthFirstSearch(graph)
    print(dfs.run_me())

    dfsw = DepthFirstSearchWholistic(graph)
    print(dfsw.run_me_wholistic())
