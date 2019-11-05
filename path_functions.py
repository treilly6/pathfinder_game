import pygame
import time
import collections
from graphModel import Graph, PriorityQueue


def breadth_first_search(graphObj):
    '''
    Input: Graph object
    Output: path of the bfs result
    '''
    start_coordinate = graphObj.start_coordinate
    end_coordinate = graphObj.end_coordinate
    queue = collections.deque()
    queue.append(start_coordinate)
    came_from = {}
    came_from[start_coordinate] = None

    found = False
    while queue:
        current = queue.popleft()

        if current == end_coordinate:
            print("BROKEN")
            found = True
            break

        # time.sleep(.15)

        if current != start_coordinate:
            graphObj.change_box_color_coordinate(current, (179, 179, 179))
            pygame.display.update()

        for neighbor in graphObj.neighbors(current):
            if neighbor not in came_from:
                queue.append(neighbor)
                came_from[neighbor] = current

    result_handler(found,came_from, graphObj)

def a_star_search(graphObj):
    '''
    Input : graph object
    Output : A* path algorithm search
    '''
    start_coordinate = graphObj.start_coordinate
    end_coordinate = graphObj.end_coordinate

    queue = PriorityQueue()
    queue.put(start_coordinate, 0)
    came_from = {}
    cost = {}
    came_from[start_coordinate] = None
    cost[start_coordinate] = 0

    found = False
    while not queue.empty():
        current = queue.get()

        print("HERE THE CURRENT  ", current)

        # time.sleep(.15)

        if current == end_coordinate:
            print("EXIT CLAUSE")
            found = True
            break

        if current != start_coordinate:
            graphObj.change_box_color_coordinate(current, (179, 179, 179))
            pygame.display.update()

        for neighbor in graphObj.neighbors(current):
            new_cost = graphObj.distance_cost(neighbor)
            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                priority = new_cost
                queue.put(neighbor, priority)
                came_from[neighbor] = current

    result_handler(found,came_from, graphObj)


def depth_first_search(graphObj):
    '''
    Input : graph object
    Output : depth first search path
    '''

    start_coordinate = graphObj.start_coordinate
    end_coordinate = graphObj.end_coordinate
    found = False
    came_from = {}
    came_from[start_coordinate] = None

    queue = [start_coordinate]

    while queue:
        current = queue.pop()

        if current == end_coordinate:
            print("FOUND THE TARGET")
            found = True
            break

        if current != start_coordinate:
            graphObj.change_box_color_coordinate(current, (179, 179, 179))
            pygame.display.update()

        for neighbor in graphObj.neighbors(current):
            if neighbor not in came_from:
                queue.append(neighbor)
                came_from[neighbor] = current

    result_handler(found,came_from, graphObj)


def result_handler(found, came_from, graphObj):
    '''
    Input : found boolean, came_from dictionary, and graph object
    Output : handles the output message and path coloring for algorithm result
    '''

    end_coordinate = graphObj.end_coordinate

    if not found:
        print("NO POSSIBLE PATH")
        graphObj.display_message("No Path!", (255, 77, 77))
        return

    print("THERES A PATH")
    path = []
    while came_from[end_coordinate]:
        print(end_coordinate)
        path.append(came_from[end_coordinate])
        end_coordinate = came_from[end_coordinate]

    graphObj.color_path(path, graphObj.start_coordinate)
    graphObj.display_message("Path Found", (0, 153, 51))
    pygame.display.update()



# ADD DFS A*
