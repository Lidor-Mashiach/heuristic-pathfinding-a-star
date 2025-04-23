from search_node import search_node
from grid_robot_state import grid_robot_state
import heapq

def create_open_set():
    open_heapq = []
    open_hash = {}
    return (open_heapq, open_hash)


def create_closed_set():
    closed_hash = {}
    return closed_hash


def add_to_open(vn, open_set):
    open_heapq, open_hash = open_set
    heapq.heappush(open_heapq, vn)
    open_hash[vn.get_State()] = vn


def open_not_empty(open_set):
    open_heapq, open_hash = open_set
    if len(open_hash)>0:
        return True
    return False

def get_best(open_set):
    open_heapq, open_hash = open_set
    while open_heapq :
        optional_best_node = heapq.heappop(open_heapq)
        if optional_best_node.get_State() in open_hash:
            best_node = optional_best_node
            open_hash.pop(best_node.get_State())
            return best_node



def add_to_closed(vn, closed_set):
    curr_state = vn.get_State()
    closed_set[curr_state] = vn


#returns False if curr_neighbor state not in open_set or has a lower g from the node in open_set
#remove the node with the higher g from open_set (if exists)
def duplicate_in_open(vn, open_set):
    open_heapq, open_hash = open_set
    curr_state = vn.get_State()
    if curr_state in open_hash:
        existing_node = open_hash[curr_state]
        if vn.get_g_Value() < existing_node.get_g_Value():
            open_hash.pop(curr_state)
            return False
        else:
            return True
    return False

#returns False if curr_neighbor state not in closed_set or has a lower g from the node in closed_set
#remove the node with the higher g from closed_set (if exists)
def duplicate_in_closed(vn, closed_set):
    curr_state = vn.get_State()
    if curr_state in closed_set:
        existing_node = closed_set[curr_state]
        if vn.get_g_Value() < existing_node.get_g_Value():
            closed_set.pop(curr_state)
            return False
        else:
            return True
    return False


# helps to debug sometimes..
def print_path(path):
    for i in range(len(path)-1):
        print(f"[{path[i].state.get_state_str()}]", end=", ")
    print(path[-1].state.state_str)


def search(start_state, heuristic):
    open_set = create_open_set()
    closed_set = create_closed_set()
    start_node = search_node(start_state, 0, heuristic(start_state))
    add_to_open(start_node, open_set)

    while open_not_empty(open_set):

        current = get_best(open_set)
        if grid_robot_state.is_goal_state(current.state):
            path = []
            while current:
                path.append(current)
                current = current.prev
            path.reverse()
            return path

        add_to_closed(current, closed_set)

        for neighbor, edge_cost in current.get_neighbors():
            curr_neighbor = search_node(neighbor, current.g + edge_cost, heuristic(neighbor), current)

            if not duplicate_in_open(curr_neighbor, open_set) and not duplicate_in_closed(curr_neighbor, closed_set):
                add_to_open(curr_neighbor, open_set)

    return None



