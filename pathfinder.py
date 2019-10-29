import pygame
from tkinter import *
import time
import collections
from path_functions import *
from graphModel import Graph, PriorityQueue


############################ FUNCTIONS FOR FILE ####################################




########################### END OF FUNCTIONF FOR THE PROGRAM #######################################
algorithm = None
algo_dict = {
    1 : breadth_first_search,
    2 : dijkstra_search,
}

class OpenWindow:
    def __init__(self):
        self.window = Tk()
        self.var = IntVar(self.window)

        self.window.title("PAthfinder game plesae set some shit")
        Label(self.window, text = "Choose which Search Algorithm to Use").pack(anchor = W)
        Radiobutton(self.window, text="Breadth First Search", variable = self.var, value=1).pack(anchor=W)
        Radiobutton(self.window, text="Dijkstra", variable = self.var, value=2).pack(anchor=W)
        Button(self.window, text="Submit", width = 20, command = self.choose_algo_click).pack(anchor=W)
        self.window.mainloop()

    def choose_algo_click(self):
        global algorithm
        var = self.var
        selection = var.get()
        algorithm = algo_dict[selection]
        self.window.destroy()

class CloseWindow():
    def __init__(self):
        self.window = Tk()
        self.var = IntVar(self.window)
        self.repeat = False

        self.window.title("PAthfinder game plesae set some shit")
        Label(self.window, text = "Play Again?").pack(anchor = W)
        Radiobutton(self.window, text="Yes", variable = self.var, value=1).pack(anchor=W)
        Radiobutton(self.window, text="No", variable = self.var, value=2).pack(anchor=W)
        Button(self.window, text="Submit", width = 20, command = self.repeat_click).pack(anchor=W)
        self.window.mainloop()

    def repeat_click(self):
        var = self.var
        selection = var.get()
        if selection == 1:
            self.repeat = True
        self.window.destroy()

def start_game():
    ow = OpenWindow()

    pygame.init()


    # create the dimensions of the pygame window
    screen_width = 700
    screen_height = 500
    screen = pygame.display.set_mode([screen_width,screen_height])

    pygame.display.set_caption("Pathfinder Game")

    black = (0, 0, 0)
    white = (255, 255, 255)
    green = (0, 255, 0)
    red = (255, 0, 0)
    yellow = (215, 224, 36)
    grey = (179, 179, 179)

    # Set the dimsensions of individual boxes in the grid
    #  (width, height, margin)
    screen_dimensions = (screen_width, screen_height)
    box_dimensions = (10, 10, 2)

    graph_obj = Graph(screen_dimensions, box_dimensions, screen)
    grid = graph_obj.grid

    screen.fill(black)

    running = True

    print("NICE")

    # draw the grid on the screen
    graph_obj.draw_grid(screen)

    while running:
        pygame.time.delay(10)
        mouse_keys = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


            mouse_keys = pygame.mouse.get_pressed()
            keys = pygame.key.get_pressed()

            if keys[pygame.K_s]:
                row, col = graph_obj.change_box_color_mouse(black)
                if graph_obj.start_coordinate:
                    graph_obj.clear_box(graph_obj.start_coordinate[0], graph_obj.start_coordinate[1])
                    if (graph_obj.start_coordinate[0], graph_obj.start_coordinate[1]) == (row,col):
                        print("SAME BOX")
                        graph_obj.start_coordinate = None
                    else:
                        graph_obj.start_coordinate = (row, col)
                else:
                    graph_obj.start_coordinate = (row, col)
                print("END")
                if graph_obj.start_coordinate == graph_obj.end_coordinate:
                    graph_obj.end_coordinate = None



            elif keys[pygame.K_e]:
                row, col = graph_obj.change_box_color_mouse(red)
                if graph_obj.end_coordinate:
                    graph_obj.clear_box(graph_obj.end_coordinate[0], graph_obj.end_coordinate[1])
                    if (graph_obj.end_coordinate[0], graph_obj.end_coordinate[1]) == (row,col):
                        print("SAME BOX")
                        graph_obj.end_coordinate = None
                    else:
                        graph_obj.end_coordinate = (row, col)
                else:
                    graph_obj.end_coordinate = (row, col)
                print("END")
                if graph_obj.end_coordinate == graph_obj.start_coordinate:
                    graph_obj.start_coordinate = None

            if (event.type == pygame.MOUSEMOTION and (mouse_keys[0] or mouse_keys[2])) or event.type == pygame.MOUSEBUTTONDOWN:
                print("DOWN CLICK")
                # Set the left click color change
                if mouse_keys[0]:
                    color = green

                # Set the right click color change
                elif mouse_keys[2]:
                    color = white

                row, column = graph_obj.change_box_color_mouse(color)

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

            if keys[pygame.K_SPACE]:
                print("START THE ALGORITHM")
                print(graph_obj.start_coordinate)
                print(graph_obj.end_coordinate)
                algorithm(graph_obj)
                running = False
                print("END LOOP IN THE SPACE KEY SHIT")

    cw = CloseWindow()
    if cw.repeat == True:
        return True
    elif cw.repeat == False:
        return False



def main():
    repeat = True
    while repeat == True:
        repeat = start_game()

main()
