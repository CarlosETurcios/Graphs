
# understanding the problem
# how can I use a graph to solve this?
# get the earliest know Ancestor
# how is childer connected to the parent
# Graph termanlogy
# - what are my nodes? = the interger
# - what are my edges? = when is there an edge when is a node connected to another node ? when not ?
# Build your graph , or wright you get Neighbors
# Choose how will you traverse the graph ?
# how do we know what is connected to what ?
# DFS


def earliest_ancestor(ancestors, node, path=None, ):
    # Write a function that, given the dataset and the ID of an individual in the dataset,
    #  returns their earliest known ancestor – the one at the farthest distance from the input individual.
    # If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID.
    #  If the input individual has no parents, the function should return -1.

    visited = []

    for i in getNeighbors(ancestors, node):
        visited.append(i)
    while len(visited) > 0:
        node = visited.pop(0)
        for i in getNeighbors(ancestors, node):
            visited.append(i)
        if len(visited) == 0:
            return node

    return -1


def getNeighbors(tree, child_node):
    parents = [node[0] for node in tree if node[1] == child_node]
    parents.sort(reverse=True)
    return parents
