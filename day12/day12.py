def find_all_paths(graph, start, end, visited_twice, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in graph:
            return []
        paths = []
        for node in graph[start]:
            if node.islower():
                if node not in path:
                    newpaths = find_all_paths(graph, node, end,visited_twice, path)
                    for newpath in newpaths:
                        paths.append(newpath)
                #comment section for part 1
                #-
                elif not visited_twice and not node == 'start':
                    newpaths = find_all_paths(graph, node, end, True, path)
                    for newpath in newpaths:
                        paths.append(newpath)
                #-
            else:
                newpaths = find_all_paths(graph, node, end, visited_twice, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths       

def day12(input):
    nodes = {}
    with open(input) as inputfile:
        for line in inputfile:
            a,b = line.rstrip().split('-')
            
            if a in nodes:
                nodes[a].append(b)
            else:
                nodes[a] = [b]
            
            if b in nodes:
                nodes[b].append(a)
            else:
                nodes[b] = [a]

    return len(find_all_paths(nodes,'start', 'end',False))
    
input = 'day12_input.txt'
print(day12(input))