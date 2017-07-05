from collections import defaultdict
graph = defaultdict(list)

graph1 = {'A': ['B', 'C'],
     'B': ['E', 'D'],
     'C': ['F', 'G'],
     'D': ['H','I'],
     'E': ['I'],
     'F': ['I'],
     'G': ['J'],
     'J': ['I'],
     'I': ['H']}


#DFS
#count connected nodes

graph2 = {
        1: [2, 3],
        2: [1, 3, 4, 7],
        3: [1, 2, 4],
        4: [2, 3],
        5: [6],
        6: [5],
        7: [2]
    }

def dfs(graph, start, mark):
    print('got', start)
    visited[start] = mark
    count = 1
    for adjNode in graph[start]:
        if not visited[adjNode]:
            print('visiting', adjNode)
            visited[adjNode] = mark
            count += dfs(graph, adjNode, mark)
    return count

visited = defaultdict(lambda:0)
mark = 1
for node in graph2:
    if not visited[node]:
        count = dfs(graph2, node, mark)
        print(visited)
        mark += 1
        print('count for', node, count)
'''
#mark all nodes in same connected component with same mark

def dfs(graph, start, mark):
    visited[start] = mark
    for adjNode in graph[start]:
        if not visited[adjNode]:
            visited[adjNode] = mark
            dfs(graph, adjNode, mark)

visited = defaultdict(lambda:0)
mark = 0
for node in graph:
    if not visited[node]:
        dfs(graph, start, mark)
        mark += 1



#find all paths b/w start and end using dfs
def find_path_dfs(graph, start, end, path=[]):
    path = path + [start] #see comment at bottom
    if start == end:
        return path
    if start not in graph:
        return None
    for next_node in graph[start]:
        if next_node not in path:
            new_path = find_path(graph, next_node, end, path)
            if new_path:
                return new_path
    return None

def find_all_paths_bfs(graph, start, end, stack=[]):
    temp_path = [start]
    stack.append(temp_path)
    while stack:
        temp_path = stack.pop(0)
        last_node = temp_path[-1]
        if last_node==end:
            print("Valid Path", temp_path)
        children = graph[last_node]
        for i in children:
            if i not in temp_path:
                new_path = temp_path + [i]

                stack.append(new_path)




def find_all_paths(graph, start, end, path=[]):
    path = path + [start] #see comment at bottom
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for next_node in graph[start]:
        if next_node not in path:
            new_paths = find_all_paths(graph, next_node, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths



print(find_all_paths_bfs(graph, 'A', 'I'))

# print(find_path(graph, 'A', 'D'))
# print(find_all_paths(graph, 'A', 'D '))

'''
'''
If we had written "path.append(start)" instead, we would have
modified the variable 'path' in the caller, with disastrous results.
'''
