"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):

        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError(
                "All your vertices are mine, or rather, do not exist.")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # make a queue
        queue = Queue()
        # make a set to track which nodes we have visited
        visited = set()
        # enqueue the starting node
        queue.enqueue(starting_vertex)
        # dequeue, while the queue isnt empty
        while queue.size() > 0:
            # dequeue, this is our current node
            current_node = queue.dequeue()
            # check if we visited
            if current_node not in visited:
                print(current_node)
            # if not we go to the node
            # mark as visited == add to visited set
                visited.add(current_node)

            # get the neighbors
                neighbors = self.get_neighbors(current_node)
            # iterate over the neighbors,. enqueue them
                for neighbor in neighbors:
                    queue.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        # make a set to track which nodes we have visited
        visited = set()
        # push the starting node
        stack.push(starting_vertex)
        # pop, while the stack isnt empty
        while stack.size() > 0:
            # pop, this is our current node
            current_node = stack.pop()
            # check if we visited
            if current_node not in visited:
                print(current_node)
            # if not we go to the node
            # mark as visited == add to visited set
                visited.add(current_node)

            # get the neighbors
                neighbors = self.get_neighbors(current_node)
            # iterate over the neighbors,. enqueue them
                for neighbor in neighbors:
                    stack.push(neighbor)

    def dft_recursive(self, vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        "" "needs to call itself"""
        if vertex not in visited:
            print(vertex)

            visited.add(vertex)

            neighbors = self.get_neighbors(vertex)
            if len(neighbors) == 0:
                return
            else:
                for neighbor in neighbors:
                    self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # make a queue()
        queue = Queue()
        # make a set to track which nodes we have visited
        visited = set()

        queue.enqueue([starting_vertex])

        # loop while the queue isn't empty
        while queue.size() > 0:
            current_path = queue.dequeue()
            current_node = current_path[-1]
            # check if we found our target node
            if current_node == destination_vertex:
                # then were done
                return current_path
            # check if we've yet visited:
            if current_node not in visited:
                # if not, we go to the node
                # mark as visited == add tho visited set
                visited.add(current_node)
                # get the neighbors
                neighbors = self.get_neighbors(current_node)
                # iterate over the neigbors, enqueue the path the them
                for neighbor in neighbors:
                    path_copy = current_path + [neighbor]
                    queue.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """

        # make a stack
        stack = Stack()
        # make visited
        visited = set()
        # push the starting node
        stack.push([starting_vertex])
        # loop while stack isnt empty:
        while stack.size() > 0:
            # pop the top of the stack
            # current should be path
            path = stack.pop()

            # must return the top node
            vertex = path[-1]

            # check to see if youfound the destinaion

            if vertex == destination_vertex:
                return path
                # check to see if not in visited list
            if vertex not in visited:
                visited.add(vertex)

                neighbors = self.get_neighbors(vertex)
                for neighbor in neighbors:
                    path_copy = path[:]
                    path_copy.append(neighbor)
                    stack.push(path_copy)

    def dfs_recursive(self, starting_vertex, destination_vertex, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
         """
        # dfs is good for getting the longest path
        # if the node your looking for is all the way at the end or a leafe of a tree
        # can be implemeted recursivly or randomly
        # check to see if path not None
        if not path:
            # starting of the path is starting vertex == same as adding the starting node to the stack or queue
            path = [starting_vertex]
        # set a variable to -1, last one in the path .
        vertex = path[-1]

        # we are checking to see if the path is the destination
        if vertex == destination_vertex:
            # you find it return path
            return path

        neighbors = self.get_neighbors(vertex)

        for neighbor in neighbors:
            # checking to make sure your not makeing duplicate searches
            if neighbor not in path:
                # create a copy of the path
                path_copy = path[:]
                # append the neigbors
                path_copy.append(neighbor)
                # recursive call take three argurments
                # recursive call only works if used with a variable
                recursive = self.dfs_recursive(
                    starting_vertex, destination_vertex, path_copy)
                # returns the recursive call
                if recursive:
                    return recursive


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
