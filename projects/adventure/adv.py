from room import Room
from player import Player
from world import World
from collections import deque


import random
from ast import literal_eval


# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
#map_file = "maps/test_line.txt"
#map_file = "maps/test_cross.txt"
#map_file = "maps/test_loop.txt"
#map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

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
# /////
# while graph is less than the world room
# pick a random path
# mark it as vistied and store the path
# do that until all the rooms are visited atleast once
traversal_path = []
# make a queue





def shortPath(player, world):

    visited = set()
    graph = {}
    opposite = {'s':'n','n':'s','e':'w','w':'e'}
    dead_end = set()

    while len(visited) < len(world.rooms):

        if player.current_room not in visited:
            visited.add(player.current_room)
           

        # travel to random room
        exits = player.current_room.get_exits()

        # creating an object with the directions as keys and room id as values
        if graph.get(player.current_room.id) is None:
            graph[player.current_room.id] = {}

        for exit in exits:
            if graph[player.current_room.id].get(exit) is None:
               
                graph[player.current_room.id][exit] = '?'

                
      

        # TODO fill each rooms directions object with the id of the room thats been traveled
        # {
        # 0: {'n': ''?, 's': 5, 'w': '?', 'e': '?'},
        # :5 {'n': 0, 's': '?', 'e': '?'} }

        # if graph[player.current_room.id][exit] in visited:
        #     graph[player.current_room.id][exit] = player.current_room.id
        unexplored_list = []
        are_there_rooms_left = False
      
        for exit in exits:
            if graph[player.current_room.id][exit] == '?':
                unexplored_list.append(exit)
                are_there_rooms_left = True
        

        if len(unexplored_list) == 0:
            random_index = random.randint(0, len(exits) - 1)
            random_move = exits[random_index]

        else:
            random_index = random.randint(0, len(unexplored_list) - 1)
            random_move = unexplored_list[random_index]


        if len(exits) == 1:
            dead_end.add(player.current_room.id)
            # print("hell",graph[player.current_room.id][random_move])
            
        if len(exits) == 2:
            for exit in exits:
                if graph[player.current_room.id][exit] in dead_end:
                    dead_end.add(player.current_room.id)
        # if graph[player.current_room.id][opposite[random_move]]: 
            # print(dead_end)
        if len(exits) == 3:
            counter = 0
            for exit in exits:
                if graph[player.current_room.id][exit] in dead_end:
                    counter += 1
            if counter >= 2:
               dead_end.add(player.current_room.id)
                    
        

            
        
        if graph[player.current_room.id][random_move] not in dead_end:

            prev_room = player.current_room.id
            player.travel(random_move)
            graph[prev_room][random_move] = player.current_room.id
            if graph.get(player.current_room.id) is None:
                graph[player.current_room.id] = {}
            graph[player.current_room.id][opposite[random_move]] = prev_room


            traversal_path.append(random_move)

     
        

    #             next_room = random_move

    # def shortPath(self, player, world, target='?'):
    #     q = Queue()
    #     visited = set()
    #     q.enqueue([player.current_room])

    #     while len(visited) < len(world.rooms):
    #         current_path = q.dequeue()
    #         current_node = current_path[-1]

    #         current_room_in = player.current_room

    #         if target not in current_node and current_node not in visited:
    #             # path = []
    #             # path.append(current_node)
    #             visited.add(current_room_in)

    #             # if target not in current node add tho visited and move on to the next room

    #             random_move = random.randint(0, len(current_node) - 1)
    #             next_room = random_move

#'e', 'n', 'e', 'e', 'e', 'e', 's', 'n', 'w', 'w', 'w', 'n',
    #             player.travel(current_node[next_room])
    #             traversal_path.append(current_node[next_room])
    # check to see if vertex has exits
    # needs to go down new path
    # TRAVERSAL TESt
shortPath(player, world)
while len(traversal_path) > 2000:
    shortPath(player, world)

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
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
