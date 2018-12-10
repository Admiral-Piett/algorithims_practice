from collections import deque

graph = {}
graph['Devin'] = ['Ryan','Matt','Sarah']
graph['Ryan'] = ['Matt','Bruns','Ashley']
graph['Matt'] = ['Ryan','Alecia','Jenny']
graph['Sarah'] = ['Andrea','Brittney','Bryan','Tom']
graph['Bruns'] = []
graph['Ashley'] = []
graph['Alecia'] = []
graph['Jenny'] = []
graph['Andrea'] = []
graph['Brittney'] = []
graph['Bryan'] = []
graph['Tom'] = []

def search_for_mango_seller(name):
    return name[-1] == 'm'
    
def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if search_for_mango_seller(person):
                print person + ' is a mango seller!'
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False
    
print search('Devin')
                