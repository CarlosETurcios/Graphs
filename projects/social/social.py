import random
from collections import deque


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


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0  # current number of users
        self.users = {}  # your user with their attributes
        self.friendships = {}  # adjacenct list

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def fisher_yates_shuffle(self, l):
        for i in range(0, len(l)):
            random_index = random.randint(i, len(l) - 1)
            l[random_index], l[i] = l[i], l[random_index]

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for user in range(num_users):
            self.add_user(user)

        # Create friendships
        # if 1 is a frind of 2, and 2 is a friend of 1, count this as 2 friendships
        total_friendships = avg_friendships * num_users

        # create a list with all possible friendship combinations
        # friendship_compos = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
        friendship_combos = []

        for user_id in range(1, num_users + 1):
            # you can avoid this by only creating a friendship where user1 < user2
            for friend_id in range(user_id + 1, num_users + 1):
                friendship_combos.append((user_id, friend_id))
             # shuffle the list
        self.fisher_yates_shuffle(friendship_combos)
        # then grab the first N elements from the list
        friendship_to_make = friendship_combos[:(total_friendships // 2)]

        for friendship in friendship_to_make:
            self.add_friendship(friendship[0], friendship[1])

    def getFriends(self, user_id):
        return self.friendships[user_id]

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """

        # key: user_id value:path
        # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        # understand the problem
        # find every single user in users ones extended network
        # for each of the user extended network what is the shortest path
        # BFS shortes path
        # make a queue
        q = Queue()
        visited = {}
        # make sure its a array ([])
        q.enqueue([user_id])

        while q.size() > 0:
            #  get the next person in line
            current_path = q.dequeue()
            current_person = current_path[-1]
            # check if we visited them yet
            if current_person not in visited:

                # if not, mark as visited
                visited[current_person] = current_path
            # get thier firends (visted thier edges)
                friends = self.getFriends(current_person)
            # enquiue them
                for friend in friends:
                    friend_path = list(current_path)
                    friend_path.append(friend)
                    q.enqueue(friend_path)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
