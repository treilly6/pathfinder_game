import pygame
import collections

def breadth_first_search(start_coordinate, end_coordinate):
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

        print("VISITING : ", current)

        for neighbor in graph_obj.neighbors(current):
            print("HERE TEH NEEGHTIBSKSDFJ", neighbor)
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
    color_path(path, start_coordinate)
    return(came_from)

def color_path(path_list, start_coordinate):
    '''
    Input : a list of tuple coordinate
    Output : colors corrdinates in the path
    '''
    for box in path_list:
        if box != start_coordinate:
            change_box_color_coordinate(box, yellow)




class Graph:
    def __init__(self, grid_width, grid_height):
        self.edges = {}
        self.walls = set()
        self.start_coordinate = None
        self.end_coordinate = None
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.grid = self.make_grid_matrix(grid_width, grid_height)

    def make_grid_matrix(self, grid_width, grid_height):
        grid = []
        for x in range(grid_height):
            temp = []
            for y in range(grid_width):
                temp.append((x,y))
            grid.append(temp)
        return grid

    def in_bounds(self, coordinate_tuple):
        row, column = coordinate_tuple
        return ((0 <= row <= (self.grid_height - 1)) and (0 <= column <= (self.grid_width - 1)))

    def not_wall(self, coordinate_tuple):
        return coordinate_tuple not in self.walls

    def neighbors(self, coordinate_tuple):
        print(self.edges)
        if coordinate_tuple in self.edges:
            return self.edges[coordinate_tuple]
        else:
            row,col = coordinate_tuple
            # set initial neighbors to the 4 graph nodes to the left, right, above, and below
            neighbors = [(row + 1, col),(row - 1, col),(row, col + 1),(row, col - 1)]
            # filter out possible positions if they are walls or not in bounds of grid
            # print("neightbors before filter " , neighbors)
            neighbors = list(filter(self.in_bounds, neighbors))
            neighbors = list(filter(self.not_wall, neighbors))
            # print("aFTER FILTER ", neighbors)
            self.edges[coordinate_tuple] = neighbors

            print("CHIRDT")
            for positon in self.edges[coordinate_tuple]:
                print(positon)
            print("YYEEET")
            return self.edges[coordinate_tuple]


pygame.init()


# create the dimensions of the pygame window
screen_width = 1000
screen_height = 500
screen = pygame.display.set_mode([screen_width,screen_height])

pygame.display.set_caption("Pathfinder Game")

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
yellow = (215, 224, 36)

# Set the dimsensions of individual boxes in the grid
width = 20
height = 20
margin = 5

# Set the dimensions of the collection of boxes
grid_width = screen_width // (width + margin)
grid_height = screen_height // (height + margin)

print(grid_width)
print(grid_height)
# Create graph object

graph_obj = Graph(grid_width, grid_height)
grid = graph_obj.grid

screen.fill(black)

running = True

print("NICE")

# Initial Setup of the Grid
for row in range(grid_height):
    for column in range(grid_width):
        color = white
        pygame.draw.rect(screen, color,[(margin + width) * column
        + margin,(margin + height) * row + margin, width,height])

pygame.display.update()


start_coordinate = None
end_coordinate = None

def change_box_color_coordinate(coordinates, color):
    '''
    Input: coordinates tuple (x,y), and color the box will change to
    Output: changes the color of the box
    '''
    row = coordinates[0]
    column = coordinates[1]

    pygame.draw.rect(screen, color,[(margin + width) * column + margin,(margin + height) * row + margin, width, height])
    pygame.display.update()

def change_box_color_mouse(color):
    '''
    Input: color the box will change to
    Output: Changes the box color and returns the array indexes of the box
    '''

    print("CHANGE BOC XOLOER FUNC")

    mouse_coordinates = pygame.mouse.get_pos()

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

def clear_box(row, column):
    '''
    Input : the array indexes
    Output: Resets that box color to the default color
    '''

    rect_dimen = (((margin + width) * column) + margin, (margin + height) * row + margin, width, height)
    # draw and update
    color = white
    pygame.draw.rect(screen, color,[(margin + width) * column + margin,(margin + height) * row + margin, width, height])
    pygame.display.update()


while running:
    pygame.time.delay(10)

    mouse_keys = pygame.mouse.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        mouse_keys = pygame.mouse.get_pressed()
        keys = pygame.key.get_pressed()

        if keys[pygame.K_s]:
            row, col = change_box_color_mouse(black)
            if start_coordinate:
                clear_box(start_coordinate[0], start_coordinate[1])
                if (start_coordinate[0], start_coordinate[1]) == (row,col):
                    print("SAME BOX")
                    start_coordinate = None
                else:
                    start_coordinate = (row, col)
            else:
                start_coordinate = (row, col)
            print("END")
            if start_coordinate == end_coordinate:
                end_coordinate = None



        elif keys[pygame.K_e]:
            row, col = change_box_color_mouse(red)
            if end_coordinate:
                clear_box(end_coordinate[0], end_coordinate[1])
                if (end_coordinate[0], end_coordinate[1]) == (row,col):
                    print("SAME BOX")
                    end_coordinate = None
                else:
                    end_coordinate = (row, col)
            else:
                end_coordinate = (row, col)
            print("END")
            if end_coordinate == start_coordinate:
                start_coordinate = None

        if (event.type == pygame.MOUSEMOTION and (mouse_keys[0] or mouse_keys[2])) or event.type == pygame.MOUSEBUTTONDOWN:
            print("DOWN CLICK")
            # Set the left click color change
            if mouse_keys[0]:
                color = green

            # Set the right click color change
            elif mouse_keys[2]:
                color = white

            row, column = change_box_color_mouse(color)

            # Add to the walls set in the graph object
            if color == green:
                if (row,column) not in graph_obj.walls:
                    graph_obj.walls.add((row, column))

            # remove from the walls set in the graph object
            if color == white:
                if (row,column) in graph_obj.walls:
                    graph_obj.walls.remove((row, column))

            print("ROW : ", row, " COL : ", column)
            print("END")
        if event.type == pygame.MOUSEBUTTONUP:
            print("UP CLICK")

        if keys[pygame.K_SPACE]:
            print("START THE ALGORITHM")
            print(start_coordinate)
            print(end_coordinate)
            print(graph_obj.walls)
            running = False
            breadth_first_search(start_coordinate, end_coordinate)
            break


print("EXITED STUFF")
print(graph_obj.walls)
print("END")

pygame.time.delay(5000)

# also need to fit the screen better for the squares


# need to check the coordinates of mouse and coordinates being saved in the tuples,
# getting many negative numbers for the tuples y positionf
