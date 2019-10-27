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
