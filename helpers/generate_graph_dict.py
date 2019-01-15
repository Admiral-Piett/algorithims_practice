# NOTE: This is a directional graph
# Need more logic for a unidirectional graph - need to copy edges into both graphs

import random

class GenerateGraphDict():

    def __init__(self, verticies, max_edges=False):
        self.verticies = verticies

        if max_edges is False:
            self.max_edges = verticies
        else:
            self.max_edges = max_edges
    
    def generate_graph(self):
        graph = dict()
        for i in range(1, self.verticies+1):
            edges = set()
            for j in range(1, random.randint(3, self.max_edges)):
                random_int = random.randint(1, self.verticies)
                if random_int != i:
                    edges.add(random_int)
            graph[i] = list(edges)

        # for k, v in graph.items():
        #     print('key', k, 'value', v)

        return graph