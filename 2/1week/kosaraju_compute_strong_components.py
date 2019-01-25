import sys
import os
import random

# from depth_first_search import DepthFirstSearch

sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '../..')))
from helpers.generate_graph_dict import GenerateGraphDict


class DepthFirstSearch():

    def __init__(self, graph, start=False):
        self.graph = graph
        self.start = self.handle_start(start)
        # print('start', self.start, '\n')
        self.explored = list()
        # This is more how many steps it took to get there rather than the actual distance from the start
        # self.distance = dict()
        self.rank = 0
        self.finishing_times = dict()


    def handle_start(self, start):
        if start is False:
            return random.randint(1, len(self.graph))
        else:
            return start

    def search(self, graph, vert):
        # self.explored.add(vert)
        self.explored.append(vert)
        for i in graph[vert]:
            # print('Checking - {0}'.format(i))
            if i not in self.explored:
                # print(list(self.explored))
                self.search(graph, i)
                self.rank += 1
                self.finishing_times[self.rank] = i
        #     else:
        #         print('ALREADY EXPLORED - {0}'.format(i))
        # if int(vert) not in self.finishing_times.values():
        #     self.rank += 1
        #     self.finishing_times[self.rank] = int(vert)

    def run_me(self, mode):
        if mode == 'loop':
            self.loop_mode(True)
        else:
            self.normal_mode()

        return self.finishing_times

    def normal_mode(self):
        self.search(self.graph, self.start)
        return self.finishing_times

    def loop_mode(self, reverse=False):
        if reverse is True:
            for i in range(len(self.graph), 0, -1):
                print('running dfs on - ', i)
                if i not in self.explored:
                    self.search(self.graph, i)
                
                if int(i) not in self.finishing_times.values():
                    self.rank += 1
                    self.finishing_times[self.rank] = i

        else:
            for i in range(1, len(self.graph)):
                print('running dfs on - ', i)
                if i not in self.explored:
                    self.search(self.graph, i)

# 1. Reverse edges on the graph
#     1. Either create a new graph going in the opposite direction
#     2. OR traverse the graphs backward


# 2. Run DFSW on graph

# Additions:
# Finishing Time - attributed by reverse DFSW
    # A dictionary with values being vertexes and keys being the rank in which the points got "suck" (couldn't find an unexplored point to go to)
# 2. will go search the graph in decreasing order of these Finishing Times
    # Label nodes in the second pass with a leader node.
        # Strongly Connected Components will have same leader - AKA leader = starting node, all who form a continuous chain from the same starting node are strongly conencted

dic = dict()
for i in range(10, 1, -1):
    dic[i] = []
print(dic)

class StronglyConnectedComponents():

    def __init__(self, graph):
        self.graph = graph

    def reverse_graph(self, graph):
        reversed_graph = {}
        # Reverses the edges for every point in the graph
        for k, v in graph.items():
            for i in v:
                reversed_graph[i] = reversed_graph.get(i, list())
                reversed_graph[i].append(k)

        # Plugs in empty edge arrays for any vertexes missing in the graph
        for i in range(1, len(reversed_graph)+1):
            reversed_graph[i] = reversed_graph.get(i, [])

        print('Reversed Graph')
        for k, v in reversed_graph.items():
            print('key', k, 'value', v)
        print('\n\n')
        
        return reversed_graph

    def run_me(self):
        # return self.reverse_graph(self.graph)
        self.reversed_graph = self.reverse_graph(self.graph)
        
        # for i in range(len(self.reversed_graph), 0, -1):
        #     print('running dfs on - ', i)
        dfs = DepthFirstSearch(self.reversed_graph, i)
        result = dfs.run_me('loop')
        print(result)
        # print(len(result))
        # exit()


# JSON Printing of the Strongly Connected Components SCC
    # {
    #     leader: [
    #         list of connected Components
    #     ]
    # }

if __name__ == '__main__':
    # g = GenerateGraphDict(20, 5)
    # graph = g.generate_graph()
    # print(graph)

    # Reversed Trial Graph
    # graph = {
    #     1: [7],
    #     2: [5],
    #     3: [9],
    #     4: [1],
    #     5: [8],
    #     6: [3, 8],
    #     7: [4, 9],
    #     8: [2],
    #     9: [6]
    # }

    graph = {
        1: [4],
        2: [8],
        3: [6],
        4: [7],
        5: [2],
        6: [9],
        7: [1],
        8: [5, 6],
        9: [3, 7]
    }

    print('Original Graph')
    for k, v in graph.items():
        print('key', k, 'value', v)
    print('\n\n')

    scc = StronglyConnectedComponents(graph)
    scc.run_me()
