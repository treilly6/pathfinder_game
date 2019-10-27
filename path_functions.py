import pygame
import time
import collections
from graphModel import Graph, PriorityQueue


def breadth_first_search(graphObj, start_coordinate, end_coordinate):
    '''
    Input: Start Coordinate and end coordinate
    Output: path of the bfs result
    '''
    queue = collections.deque()
    queue.append(start_coordinate)
    came_from = {}
    came_from[start_coordinate] = None

    while queue:
        current = queue.popleft()

        if current == end_coordinate:
            print("BROKEN")
            break

        time.sleep(.15)

        if current != start_coordinate:
            change_box_color_coordinate(graphObj, current, (179, 179, 179))
            pygame.display.update()

        for neighbor in graphObj.neighbors(current):
            if neighbor not in came_from:
                queue.append(neighbor)
                came_from[neighbor] = current

    print("END OF BFS")
    # print(came_from)
    path = []
    while came_from[end_coordinate]:
        path.append(came_from[end_coordinate])
        end_coordinate = came_from[end_coordinate]

    print("paht shit")
    print(path)
    print("REAL END")
    color_path(graphObj, path, start_coordinate)
    pygame.display.update()
    return

def dijkstra_search(graphObj, start_coordinate, end_coordinate):
    '''
    Input : start and end coordinate
    Output : path of dijkstra's algorithm search
    '''
    queue = PriorityQueue()
    queue.put(start_coordinate, 0)
    came_from = {}
    cost = {}
    came_from[start_coordinate] = None
    cost[start_coordinate] = 0

    while not queue.empty():
        current = queue.get()

        print("HERE THE CURRENT  ", current)

        time.sleep(.15)

        if current == end_coordinate:
            print("EXIT CLAUSE")
            break

        if current != start_coordinate:
            change_box_color_coordinate(graphObj, current, (179, 179, 179))
            print("chaneg")
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
    path = []
    print(len(came_from))
    print(came_from)
    print("important")
    while came_from[end_coordinate]:
        path.append(came_from[end_coordinate])
        end_coordinate = came_from[end_coordinate]

    print("paht shit")
    print(path)
    print("REAL END")
    color_path(graphObj, path, start_coordinate)
    pygame.display.update()
    return

def color_path(graphObj, path_list, start_coordinate):
    '''
    Input : a list of tuple coordinate
    Output : colors corrdinates in the path
    '''
    for box in path_list:
        if box != start_coordinate:
            change_box_color_coordinate(graphObj, box, (215, 224, 36))

def change_box_color_coordinate(graphObj, coordinates, color):
    '''
    Input: coordinates tuple (x,y), and color the box will change to
    Output: changes the color of the box
    '''
    row = coordinates[0]
    column = coordinates[1]

    screen = graphObj.screen
    width = graphObj.box_width
    height = graphObj.box_height
    margin = graphObj.margin

    pygame.draw.rect(screen, color,[(margin + width) * column + margin,(margin + height) * row + margin, width, height])
    pygame.display.update()
    return

def change_box_color_mouse(graphObj, color):
    '''
    Input: color the box will change to
    Output: Changes the box color and returns the array indexes of the box
    '''

    print("CHANGE BOC XOLOER FUNC")

    mouse_coordinates = pygame.mouse.get_pos()

    width = graphObj.box_width
    height = graphObj.box_height
    margin = graphObj.margin
    screen = graphObj.screen

    # Get the row and col indexs for the matrix
    # This format makes the left and top margins part of that box
    # (i.e if you click on the top left boxes top margin that would
    # be row 0 and that same boxes bottom margin would be considered row 1 and part of the box below it)
    column = mouse_coordinates[0] // (width + margin)
    row = mouse_coordinates[1] // (height + margin)

    # Set the dimensions and location of new drawn rectagle
    rect_dimen = (((margin + width) * column) + margin, (margin + height) * row + margin, width, height)

    # draw and update
    pygame.draw.rect(screen, color,[(margin + width) * column + margin,(margin + height) * row + margin, width, height])
    pygame.display.update()
    return (row, column)

def clear_box(graphObj, row, column):
    '''
    Input : the array indexes
    Output: Resets that box color to the default color
    '''

    margin = graphObj.margin
    width = graphObj.box_width
    height = graphObj.box_height
    screen = graphObj.screen

    rect_dimen = (((margin + width) * column) + margin, (margin + height) * row + margin, width, height)
    # draw and update
    color = (255,255,255)
    pygame.draw.rect(screen, color,[(margin + width) * column + margin,(margin + height) * row + margin, width, height])
    pygame.display.update()
    return
