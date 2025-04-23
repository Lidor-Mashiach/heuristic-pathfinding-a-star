class grid_robot_state:
    # you can add global params

    def __init__(self, robot_location, map=None, lamp_height=-1, lamp_location=(-1, -1), curr_height=0, obstacles=None, stairs = None):
        ## Initialize obstacles and stairs from the map

        self.map = map
        if obstacles is None:
            self.obstacles = self.create_obstacles(self.map)
        else:
            self.obstacles = obstacles

        if stairs is None:
            self.stairs = self.create_stairs(self.map)
        else:
            self.stairs = stairs
        self.location = robot_location
        self.lamp_height = lamp_height
        self.lamp_location = lamp_location
        self.curr_height = curr_height
        self.Row_len = len(map[0])
        self.Col_len = len(map)


    @staticmethod
    def create_obstacles(map):
        """
        Creates a set of obstacle locations (-1 cells) from the map.

        Args:
            map (list of lists): The grid map.

        Returns:
            set: A set of (row, col) tuples representing obstacle locations.
        """
        result = set()
        for i in range(len(map)):
            for j in range(len(map[0])):
                if map[i][j] == -1:
                    result.add((i, j))
        return result

    @staticmethod
    def create_stairs(map):
        """
        Creates a dictionary of stair locations and heights from the map.

        Args:
            map (list of lists): The grid map.

        Returns:
            dict: A dictionary mapping (row, col) tuples to stair heights.
        """
        result = {}  #
        for i in range (len(map)):
            for j in range (len(map[0])):
                if map[i][j]>0:
                    result[(i, j)] = map[i][j]
        return result

    @staticmethod
    def is_goal_state(_grid_robot_state):
        if _grid_robot_state.location == _grid_robot_state.lamp_location:
            if _grid_robot_state.stairs.get(_grid_robot_state.lamp_location , 0) == _grid_robot_state.lamp_height:
                return True
        return False


    def get_neighbors(self):
        neighbors_Array = []

        # Lower neighbor
        if self.location[0] + 1 < self.Col_len:
            new_location = (self.location[0] + 1, self.location[1])
            if new_location not in self.obstacles:  # Ensure the location is not an obstacle
                Lower_neighbor_state = grid_robot_state( new_location, self.map, self.lamp_height, self.lamp_location, self.curr_height, self.obstacles, self.stairs)
                neighbors_Array.append((Lower_neighbor_state, 1 + self.curr_height))

        # Upper neighbor
        if self.location[0] - 1 >= 0:
            new_location = (self.location[0] - 1, self.location[1])
            if new_location not in self.obstacles:  # Ensure the location is not an obstacle
                Upper_neighbor_state = grid_robot_state(new_location, self.map, self.lamp_height, self.lamp_location, self.curr_height, self.obstacles, self.stairs)
                neighbors_Array.append((Upper_neighbor_state, 1 + self.curr_height))

        # Right neighbor
        if self.location[1] + 1 < self.Row_len:
            new_location = (self.location[0], self.location[1] + 1)
            if new_location not in self.obstacles:  # Ensure the location is not an obstacle
                Right_neighbor_state = grid_robot_state(new_location, self.map,self.lamp_height,self.lamp_location, self.curr_height,self.obstacles, self.stairs)
                neighbors_Array.append((Right_neighbor_state, 1 + self.curr_height))

        # Left neighbor
        if self.location[1] - 1 >= 0:
            new_location = (self.location[0], self.location[1] - 1)
            if new_location not in self.obstacles:  # Ensure the location is not an obstacle
                Left_neighbor_state = grid_robot_state(new_location, self.map, self.lamp_height, self.lamp_location, self.curr_height, self.obstacles, self.stairs)
                neighbors_Array.append((Left_neighbor_state, 1 + self.curr_height))

        # If lifting stairs is available --> append the operation's state to the array
        if self.location in self.stairs:
            stair_height = self.stairs[self.location]
            if self.curr_height + stair_height <= self.lamp_height:  # Ensure height constraint
                new_stairs = self.stairs.copy()
                del new_stairs[self.location]  # Remove the stairs after lifting
                neighbor_state = grid_robot_state(self.location, self.map, self.lamp_height, self.lamp_location, self.curr_height + stair_height, self.obstacles, new_stairs)
                neighbors_Array.append((neighbor_state, 1))  # Current state after lifting

        # If dropping stairs is available --> append the operation's state to the array
        if self.curr_height > 0 and self.location not in self.stairs:
            new_stairs = self.stairs.copy()
            new_stairs[self.location] = self.curr_height
            neighbor_state = grid_robot_state(self.location, self.map, self.lamp_height, self.lamp_location,0, self.obstacles, new_stairs)
            neighbors_Array.append((neighbor_state, 1))  # Current state after dropping

        return neighbors_Array

    def __hash__(self):
            """
                Generates a unique hash for the state.
                Uses only relevant fields to ensure efficiency.
            """
            return hash((self.location, frozenset(self.stairs.items())))

    def __eq__(self, other):
            """
                Compares this state to another for equality.
            """

            return self.location == other.location and self.stairs == other.stairs

    def get_current_height(self):
        return self.curr_height

    def get_lamp_location_stairs(self):
        return self.stairs.get(self.lamp_location,0)

    def get_stairs(self):
        return self.stairs


    def get_state_str(self):
        return self.location



    #you can add helper functions