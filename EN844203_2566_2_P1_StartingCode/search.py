#####
#
# Name: Vititpoom Khamsong
# Student ID: 633040587-7
#
#####

from explore import explore  ##### DO NOT CHANGE THIS LINE #####


def initialize_dfs(m, n, sr, sc, gr, gc):
    
    global maze_row, maze_col, start_row, start_col, goal_row, goal_col
    maze_row, maze_col, start_row, start_col, goal_row, goal_col = m, n, sr, sc, gr, gc
    


def dfs():
    def explore_action(pop_list):
        right = (pop_list[0], pop_list[1] + 1)
        up = (pop_list[0] - 1, pop_list[1])
        left = (pop_list[0], pop_list[1] - 1)
        down = (pop_list[0] + 1, pop_list[1])
        return [right, up, left, down]
    
    def explore_and_go(direction, visited_list, row, column, stack_queue = []):
        if direction not in visited_list and (1 <= direction[1] < (column - 1) and 1 <= direction[0] < (row - 1)):
                result = explore(direction[0], direction[1])
                visited_list.append(direction)
                if result == "G":
                    return result
                elif result != "X":
                    stack_queue.append(direction)

    start_pos = (start_row, start_col)
    list = [start_pos]
    visited_list = [start_pos]

    while True:
        stack_queue = []
        pop_list = list.pop()
        actions = explore_action(pop_list)
        for index in range(len(actions)):
            result = explore_and_go(actions[index], visited_list, maze_row, maze_col, stack_queue)
            if result == "G":
                return
        stack_queue.reverse()
        list.extend(stack_queue)

    


def initialize_bfs(m, n, sr, sc, gr, gc):
    global maze_row, maze_col, start_row, start_col, goal_row, goal_col
    maze_row, maze_col, start_row, start_col, goal_row, goal_col = m, n, sr, sc, gr, gc
    


def bfs():
    def explore_actions(pop_list):
        right = (pop_list[0], pop_list[1] + 1)
        up = (pop_list[0] - 1, pop_list[1])
        left = (pop_list[0], pop_list[1] - 1)
        down = (pop_list[0] + 1, pop_list[1])
        return [right, up, left, down]
    
    def explore_and_go(direction, visited_list, row, column, queue = []):
        if direction not in visited_list and (1 <= direction[1] < (column - 1) and 1 <= direction[0] < (row - 1)):
            result = explore(direction[0], direction[1])
            visited_list.append(direction)
            if result == "G":
                return result
            elif result != "X":
                queue.append(direction)
                    
    start_pos = (start_row, start_col)
    list = [start_pos]
    visited_list = [start_pos]


    while True:
        pop_list = list.pop(0)
        actions = explore_actions(pop_list)
        for index in range(len(actions)):
            result = explore_and_go(actions[index], visited_list, maze_row, maze_col, list)
            if result == "G":
                return
            
            






def initialize_Astar(m, n, sr, sc, gr, gc, k):
    global maze_row, maze_col, start_row, start_col, goal_row, goal_col, magic_blade
    maze_row, maze_col, start_row, start_col, goal_row, goal_col, magic_blade = m, n, sr, sc, gr, gc, k
    pass  # TODO


def Astar():
    def explore_actions():
        return [(0, 1), (-1, 0), (0, -1), (1, 0)]
    
    
    def EuclideanDistance(start, goal):
        return ((goal[0] - start[0])**2 + (goal[1] - start[1])**2 ) ** 0.5
    
    magical_blade = magic_blade
    priority_queue = []
    visited = []

    start_grid = ((start_row, start_col), magical_blade, 0, 0)
    goal = (goal_row, goal_col)

    priority_queue.append(start_grid)

    while True:
        current = min(priority_queue, key=lambda node: node[2])
        magical_blade = current[1]
        
        priority_queue.remove(current)

        if current[0] == (goal_row, goal_col):
            return current[3]
        
        if (current[0], magical_blade) not in visited:
            visited.append((current[0], magical_blade))
            
            directions = explore_actions()
            for index in range(len(directions)):
                checking = tuple(map(sum, zip(directions[index], current[0])))
                if 1 <= checking[0] < (maze_row - 1) and 1 <= checking[1] < (maze_col - 1):
                    value = explore(checking[0], checking[1])
                    if value == "X" and magical_blade > 0:
                        value = "0"
                        magical_blade -= 1
                    if value == "S" or value == "G":
                        value = "0"
                    if value.isdigit():
                        value = int(value)
                    if value != "X":
                        gn = value + current[3]
                        hn = EuclideanDistance(checking, goal)
                        fn = gn + hn
                        priority_queue.append((checking, magical_blade, fn, gn))



