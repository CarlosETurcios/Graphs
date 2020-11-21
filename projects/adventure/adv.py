from room import Room
from player import Player
from world import World
from collections import deque


import random
from ast import literal_eval


class Queue():
    def __init__(self):
        self.queue = deque()

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.popleft()
        else:
            return None

    def size(self):
        return len(self.queue)


# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
# make your own graph
# store the path direction inside the travel path
# do a bfs
# choose a path at random
#
traversal_path = []


def getPath(self, path):

    return


def shorTraversal(self, path, new='?'):

    q = Queue()
    visited = {}
    # make sure its a array ([])
    q.enqueue([path])

    while q.size() > 0:

        current_path = q.dequeue()
        current_newPath = current_path[-1]

        # check to see if new path found
        if current_newPath == new:
            # needs to go down new path
            return current_newPath

        if current_newPath not in visited:

            # if not, mark as visited
            visited[current_newPath] = current_path
        # get thier firends (visted thier edges)
            paths = self.getPath(current_newPath)
        # enquiue them
            for path in paths:
                new_path = list(current_path)
                new_path.append(new_path)
                q.enqueue(new_path)

    return visited


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
