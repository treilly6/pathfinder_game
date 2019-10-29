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

    print("END OF BFS")
    path = []
    if not found:
        print("NO PATH POSSIBLE")
        return

    while came_from[end_coordinate]:
        path.append(came_from[end_coordinate])
        end_coordinate = came_from[end_coordinate]

    graphObj.color_path(path, start_coordinate)
    pygame.display.update()
    return

def dijkstra_search(graphObj):
    '''
    Input : start and end coordinate
    Output : path of dijkstra's algorithm search
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

    print("END OF dijkstra")
    # print(came_from)
    if not found:
        print("NO POSSIBLE PATH")
        return

    path = []
    while came_from[end_coordinate]:
        path.append(came_from[end_coordinate])
        end_coordinate = came_from[end_coordinate]

    graphObj.color_path(path, start_coordinate)
    pygame.display.update()
    return
