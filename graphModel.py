import pygame

class Graph:
    def __init__(self, screen_dimensions, box_dimensions, screen):
        self.edges = {}
        self.walls = set()
        self.start_coordinate = None
        self.end_coordinate = None
        self.grid_height = screen_dimensions[1] // (box_dimensions[1] + box_dimensions[2])
        self.grid_width = screen_dimensions[0] // (box_dimensions[0] + box_dimensions[2])
        self.box_width = box_dimensions[0]
        self.box_height = box_dimensions[1]
        self.margin = box_dimensions[2]
        self.grid = self.make_grid_matrix(self.grid_width, self.grid_height)
        self.screen = screen

    def draw_grid(self, screen):
        ''' Draws the grid onto the screen '''
        margin = self.margin
        width = self.box_width
        height = self.box_height
        color = (255, 255, 255)
        for row in range(self.grid_height):
            for column in range(self.grid_width):
                pygame.draw.rect(screen, color,[(margin + width) * column
                + margin,(margin + height) * row + margin, width,height])
        pygame.display.update()
        return

    def make_grid_matrix(self, grid_width, grid_height):
        grid = []
        for x in range(grid_height):
            temp = []
            for y in range(grid_width):
                temp.append((x,y))
            grid.append(temp)
        return grid

    def clear_box(self, row, column):
        '''
        Input : the array indexes
        Output: Resets that box color to the default color
        '''

        margin = self.margin
        width = self.box_width
        height = self.box_height
        screen = self.screen

        rect_dimen = (((margin + width) * column) + margin, (margin + height) * row + margin, width, height)
        # draw and update
        color = (255,255,255)
        pygame.draw.rect(screen, color,[(margin + width) * column + margin,(margin + height) * row + margin, width, height])
        pygame.display.update()
        return

    def change_box_color_mouse(self, color):
        '''
        Input: color the box will change to
        Output: Changes the box color and returns the array indexes of the box
        '''

        print("CHANGE BOC XOLOER FUNC")

        mouse_coordinates = pygame.mouse.get_pos()

        width = self.box_width
        height = self.box_height
        margin = self.margin
        screen = self.screen

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

    def change_box_color_coordinate(self, coordinates, color):
        '''
        Input: coordinates tuple (x,y), and color the box will change to
        Output: changes the color of the box
        '''
        row = coordinates[0]
        column = coordinates[1]

        screen = self.screen
        width = self.box_width
        height = self.box_height
        margin = self.margin

        pygame.draw.rect(screen, color,[(margin + width) * column + margin,(margin + height) * row + margin, width, height])
        pygame.display.update()
        return

    def color_path(self, path_list, start_coordinate):
        '''
        Input : a list of tuple coordinate
        Output : colors corrdinates in the path
        '''
        for box in path_list:
            if box != start_coordinate:
                self.change_box_color_coordinate(box, (215, 224, 36))

    def in_bounds(self, coordinate_tuple):
        row, column = coordinate_tuple
        return ((0 <= row <= (self.grid_height - 1)) and (0 <= column <= (self.grid_width - 1)))

    def not_wall(self, coordinate_tuple):
        return coordinate_tuple not in self.walls

    def neighbors(self, coordinate_tuple):
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

            return self.edges[coordinate_tuple]

    def distance_cost(self, graph_coordinate):
        '''
        Input : a graph coordinate
        Output : an integer representing the distance to the end/goal coordinate
        '''
        return abs(graph_coordinate[0] - self.end_coordinate[0]) + abs(graph_coordinate[1] - self.end_coordinate[1])

    def display_message(self, message, color):
        text = pygame.font.Font('freesansbold.ttf', 60)
        surface = text.render(message, True, color)
        rect = surface.get_rect()
        rect.center = (700/2, 500/2)
        self.screen.blit(surface, rect)
        pygame.display.update()

import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]
