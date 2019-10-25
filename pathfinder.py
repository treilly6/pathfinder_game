import pygame

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

# Set the dimsensions of individual boxes in the grid
width = 20
height = 20
margin = 5

# Set the dimensions of the collection of boxes
grid_width = screen_width // (width + margin)
grid_height = screen_height // (height + margin)

print(grid_width)
print(grid_height)
# Create the underlying grid array matrix
grid = [[0 for x in range(grid_width)] for y in range(grid_height)]



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

def change_box_color(color):
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
    print(margin)
    print(height)
    print(width)
    print(row)
    print(column)
    print("end of celar fiund")
    rect_dimen = (((margin + width) * column) + margin, (margin + height) * row + margin, width, height)
    print(rect_dimen)
    print("HERE RECT DIMENT")

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
            row, col = change_box_color(black)
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
            row, col = change_box_color(red)
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

            change_box_color(color)

            print("ROW : ", row, " COL : ", column)
            print("END")
        if event.type == pygame.MOUSEBUTTONUP:
            print("UP CLICK")

        if keys[pygame.K_SPACE]:
            print("START THE ALGORITHM")


# need to make the actual index in an array equal to the nodes which
# contain info needed for the djkstras algorithm

# also need to fit the screen better for the squares
