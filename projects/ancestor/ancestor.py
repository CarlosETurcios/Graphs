
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


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


def get_neighbors(self,):
    neighbors_list = []


def earliest_ancestor(ancestors, starting_node, earliest_node):

    stack = Stack()

    visited = set()

    stack.push([starting_node])

    while stack.size() > 0:

        path = stack.pop()

        vertex = path[-1]

        if vertex == earliest_node:
            return path

        if vertex not in visited:
            visited.add(vertex)

            neighbors = get_neighbors(vertex)

            for neighbor in neighbors:
                path_copy = path[:]
                path_copy.append(neighbor)
                stack.push(path_copy)
