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
        self.stack = []
        self.reverse_graph = reverse_graph
        self.orig_graph = orig_graph
        self.start = self.handle_start(start)
        self.explored = list()

        self.finishing_times = list()

        # list of currently connected components
        self.current_connection = []
        # final list of strongly connected components
        self.strong_components = dict()

    def handle_start(self, start):
        if start is False:
            return random.randint(1, len(self.orig_graph))
        else:
            return start

    def search(self, graph):
        while len(self.stack) > 0:
            vert = self.stack.pop()
            # print('vert', vert)
            self.explored.append(vert)
            for i in graph[vert]:
                if i not in self.explored:
                    self.stack.append(i)
                    self.search(graph)
            self.finishing_times.append(vert)

    def compute_connections(self, graph, vert):
        # print('vert', vert)
        self.explored.append(vert)
        self.current_connection.append(vert)
        for i in graph[vert]:
            if i not in self.explored:
                self.compute_connections(graph, i)
            else:
                break



    def run_me(self):
        for i in range(len(self.orig_graph), 0, -1):
            if i not in self.explored:
                # print('starting DFS with', i)
                self.stack.append(i)
                self.search(self.reverse_graph)
        # self.run_loop(self.reverse_graph, range(len(self.orig_graph), 0, -1))
        
        print(self.finishing_times)


        # Resetting for current loop
        self.explored = []

        for i in self.finishing_times:
            if i not in self.explored:
                # print('second DFS with', i)
                self.compute_connections(self.orig_graph, i)
                self.strong_components[i] = self.current_connection
                self.current_connection = []
        # print(self.strong_components)
        return self.strong_components
        

    def run_loop(self, graph, iter_range, ):
        for i in iter_range:
            if i not in self.explored:
                print('starting DFS with', i)
                self.stack.append(i)
                self.search(graph)
#         self.loop_mode(True)
#         print('FINISHING TIMES -', self.finishing_times)    



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
        for i in range(1, len(graph)+1):
            # print('checking', i)
            reversed_graph[i] = reversed_graph.get(i, [])

        print('Reversed Graph')
        for k, v in reversed_graph.items():
            print('key', k, 'value', v)
        print('\n\n')
        
        return reversed_graph


    def run_me(self):
        self.reversed_graph = self.reverse_graph(self.graph)
        
        reverse_dfs = DepthFirstSearch(self.reversed_graph, self.graph)
        result = reverse_dfs.run_me()
        print(result)
        return result



if __name__ == '__main__':
    g = GenerateGraphDict(10, 5)
    graph = g.generate_graph()
    print(graph)

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

    # graph = {
    #     1: [4],
    #     2: [8],
    #     3: [6],
    #     4: [7],
    #     5: [2],
    #     6: [9],
    #     7: [1],
    #     8: [5, 6],
    #     9: [3, 7]
    # }

    print('Original Graph')
    for k, v in graph.items():
        print('key', k, 'value', v)
    print('\n\n')

    scc = StronglyConnectedComponents(graph)
    strongly_connected_components = scc.run_me()
    r_graph = scc.reversed_graph
    print(r_graph)

    # for k, v in strongly_connected_components.items():
    #     print('key', k, 'value', v)
    # print('\n\n')

    g = Graph(r_graph)
    g.printSCCs()
    



# class DepthFirstSearch():

#     def __init__(self, reverse_graph, orig_graph, start=False):
#         self.reverse_graph = reverse_graph
#         self.orig_graph = orig_graph
#         self.start = self.handle_start(start)
#         self.explored = list()


#         self.finishing_times = list()

#         self.component_check = list()
#         self.strong_components = dict()


#     def handle_start(self, start):
#         if start is False:
#             return random.randint(1, len(self.orig_graph))
#         else:
#             return start

#     def search(self, graph, vert):
#         self.explored.append(vert)
#         for i in graph[vert]:
#             if i not in self.explored:
#                 self.search(graph, i)
#                 self.finishing_times.append(i)


    
#     def search_for_components(self, graph, vert):
#         self.explored.append(vert)
#         for i in graph[vert]:
#             print('checking', i)
#             # print(self.component_check)
#             if i == self.leader:
#                 self.strong_components[self.component_check[0]] = self.component_check
#                 print('FOUND IT', self.component_check)
#                 # self.component_check = list()
#                 return
#             elif i not in self.explored:
#                 self.component_check.append(i)
#                 self.search_for_components(graph, i)
#                 if len(self.component_check) > 0:
#                     print('popping', self.component_check.pop())
            



#     def run_me(self):
#         self.loop_mode(True)
#         print('FINISHING TIMES -', self.finishing_times)

#         self.explored = list()
#         self.loop_mode(False, self.finishing_times)

#         # self.strong_components[1].append(2000)

#         return self.strong_components



#     def normal_mode(self, graph):
#         self.search(graph, self.start)
#         return self.finishing_times

#     def loop_mode(self, reverse=False, iter_range=False):
#         if reverse is True:
#             if iter_range is False:
#                 iter_range = range(len(self.reverse_graph), 0, -1)
#             for i in iter_range:
#                 # print('running dfs on - ', i)
#                 if i not in self.explored:
#                     self.search(self.reverse_graph, i)
                
#                 if int(i) not in self.finishing_times:
#                     self.finishing_times.append(i)

#         else:
#             if iter_range is False:
#                 iter_range = range(1, len(self.orig_graph))
#             for i in iter_range:
#                 # print('running dfs on - ', i)
#                 if i not in self.explored:
#                     self.leader = i
#                     self.component_check.append(i)
#                     self.search_for_components(self.orig_graph, i)

#                     self.component_check = list()