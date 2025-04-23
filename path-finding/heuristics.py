from grid_robot_state import grid_robot_state



def base_heuristic(_grid_robot_state):
    """
       Calculates the Manhattan distance heuristic between the robot's current location
       and the lamp's target location.

       Args:
           _grid_robot_state (grid_robot_state): The current state of the robot.

       Returns:
           int: The Manhattan distance between the robot's location and the lamp's location.
       """
    robot_location = _grid_robot_state.location
    lamp_location = _grid_robot_state.lamp_location

    # Compute Manhattan distance
    manhattan_distance = abs(lamp_location[0] - robot_location[0]) + abs(lamp_location[1] - robot_location[1])

    return manhattan_distance



def advanced_heuristic(_grid_robot_state):
    robot_location = _grid_robot_state.location
    lamp_location = _grid_robot_state.lamp_location
    lamp_height = _grid_robot_state.lamp_height
    current_height = _grid_robot_state.get_current_height()
    stairs = _grid_robot_state.get_stairs()

    direct_distance = abs(lamp_location[0] - robot_location[0]) + abs(lamp_location[1] - robot_location[1])

    if current_height == lamp_height and not stairs:
        return direct_distance

    min_cost = float('inf')

    for stair_location, stair_value in stairs.items():
        if stair_value + current_height > lamp_height:
            continue

        to_stair = abs(stair_location[0] - robot_location[0]) + abs(stair_location[1] - robot_location[1])
        from_stair = abs(stair_location[0] - lamp_location[0]) + abs(stair_location[1] - lamp_location[1])
        height_adjustment = lamp_height - stair_value

        stair_cost = (
                to_stair + 1 +
                from_stair * (1 + stair_value) +
                1 + height_adjustment + (height_adjustment > 0)
        )


        if stair_cost < min_cost:
            min_cost = stair_cost


    if min_cost == float('inf'):
        height_penalty = lamp_height - current_height + (lamp_height > current_height)
        return direct_distance + height_penalty

    return min_cost