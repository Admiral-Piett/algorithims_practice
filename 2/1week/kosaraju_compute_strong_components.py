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

import sys
import os
import random

# from depth_first_search import DepthFirstSearch

sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '../..')))
from helpers.generate_graph_dict import GenerateGraphDict


class DepthFirstSearch():

    def __init__(self, reverse_graph, orig_graph, start=False):
        self.reverse_graph = reverse_graph
        self.orig_graph = orig_graph
        self.start = self.handle_start(start)
        # print('start', self.start, '\n')
        self.explored = list()
        # This is more how many steps it took to get there rather than the actual distance from the start
        # self.distance = dict()
        
        # NOTE: Swap comments to make dictionary VS list
        self.rank = 0
        # self.finishing_times = dict()
        self.finishing_times = list()

        self.component_check = list()
        self.strong_components = dict()


    def handle_start(self, start):
        if start is False:
            return random.randint(1, len(self.orig_graph))
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
                # self.rank += 1
                # self.finishing_times[self.rank] = i
                self.finishing_times.append(i)
        #     else:
        #         print('ALREADY EXPLORED - {0}'.format(i))

    
    def search_for_components(self, graph, vert):
        self.explored.append(vert)
        for i in graph[vert]:
            if i not in self.explored:
                self.search_for_components(graph, i)
                self.component_check.append(i)
            break


    def run_me(self):
        self.loop_mode(True)
        print(self.finishing_times)

        self.explored = list()
        self.loop_mode(False, self.finishing_times)

        return self.strong_components



    def normal_mode(self, graph):
        self.search(graph, self.start)
        return self.finishing_times

    def loop_mode(self, reverse=False, iter_range=False):
        if reverse is True:
            if iter_range is False:
                iter_range = range(len(self.reverse_graph), 0, -1)
            for i in iter_range:
                print('running dfs on - ', i)
                if i not in self.explored:
                    self.search(self.reverse_graph, i)
                
                if int(i) not in self.finishing_times:
                    # self.rank += 1
                    # self.finishing_times[self.rank] = i
                    self.finishing_times.append(i)

        else:
            if iter_range is False:
                iter_range = range(1, len(self.orig_graph))
            for i in iter_range:
                print('running dfs on - ', i)
                if i not in self.explored:
                    self.component_check.append(i)
                    self.search_for_components(self.orig_graph, i)

                    self.rank += 1
                    self.strong_components[self.rank] = self.component_check
                    self.component_check = list()



# dic = dict()
# for i in range(10, 1, -1):
#     dic[i] = []

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
        reverse_dfs = DepthFirstSearch(self.reversed_graph, self.graph)
        result = reverse_dfs.run_me()
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
