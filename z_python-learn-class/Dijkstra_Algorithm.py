infinity = float('inf')

# graph = {}
# graph['start'] = {}
# graph['a'] = {}
# graph['b'] = {}
# graph['start']['a'] = 6
# graph['start']['b'] = 2
# graph['a']['fin'] = 1
# graph['b']['a'] = 3
# graph['b']['fin'] = 5
# graph['fin'] = {}
# 
# costs = {}
# costs['a'] = 6
# costs['b'] = 2
# costs['fin'] = infinity
# 
# parents = {}
# parents['a'] = 'start'
# parents['b'] = 'start'
# parents['fin'] = None

graph = {}
graph['start'] = {}
graph['a'] = {}
graph['b'] = {}
graph['c'] = {}
graph['d'] = {}
graph['start']['a'] = 5
graph['start']['b'] = 2
graph['a']['c'] = 4
graph['a']['d'] = 2
graph['b']['a'] = 3
graph['b']['d'] = 7
graph['c']['fin'] = 3
graph['c']['d'] = 6
graph['d']['fin'] = 1
graph['fin'] = {}

costs = {}
costs['a'] = 6
costs['b'] = 2
costs['c'] = infinity
costs['d'] = infinity
costs['fin'] = infinity

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['c'] = None
parents['d'] = None
parents['fin'] = None

processed = []

def path_finder(parents):
    path = []
    parent = 'fin'
    path.append(parent)
    while 'start' not in path:
        path.append(parents[parent])
        parent = parents[parent]
    return path
#         for key, value in parents.iteritems():
# #             print value
#             if value == parent:
#                 path.append(key)
#                 parent = key
        

# def path_finder(costs):
#     less = {}
#     more = {}
#     processed = {}
#     if len(costs) < 2:
#         return costs
#     for key, value in costs.iteritems():
#         pivot = costs.values()[len(costs) / 2]
#         if value < pivot:
# #             less = {}
#             less[key] = value
#             print less
#         elif value > pivot:
# #             more = {}
#             more[key] = value
#             print more
#         else:
# #             processed = {}
#             processed[key] = value
#     path = {}
#     for d in (less, more, processed):
#         path.update(d)
#     return path
def find_lowest_cost(costs):
    lowest_cost = infinity
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node
    
def al():
    node = find_lowest_cost(costs)
    while node is not None:
       cost = costs[node]
       neighbors = graph[node]
       for n in neighbors.keys():
           new_cost = cost + neighbors[n]
           if costs[n] > new_cost:
               costs[n] = new_cost
               parents[n] = node
       processed.append(node)
       node = find_lowest_cost(costs)
    print parents
    return path_finder(parents)
    return costs
#        node = find_lowest_cost(costs)
#     print node
#     print costs[n]
#     print parents[n]
    
print al()

