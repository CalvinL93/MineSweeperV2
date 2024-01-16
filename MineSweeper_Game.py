import pygame
import random
import time
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GRAY = (170, 170, 170)

# Box Size
WIDTH = 20
HEIGHT = 20
MARGIN = 5

# Left click on mouse, right click on mouse
LEFT = 1
RIGHT = 3

def play_minesweeper(difficulty): 
    if difficulty == 1:
        windowSize = (255, 255)
        gridSizeX = 10
        gridSizeY = 10
        numberOfMines = 10
    elif difficulty == 2:
        windowSize = (505, 505)
        gridSizeX = 20
        gridSizeY = 20
        numberOfMines = 50
    elif difficulty == 3:
        windowSize = (1005, 505)
        gridSizeX = 20
        gridSizeY = 40
        numberOfMines = 100

    pygame.init()

    # Set the width and height of the screen
    screen = pygame.display.set_mode(windowSize)

    font = pygame.font.SysFont('Calibri', 25, True, False)

    pygame.display.set_caption("MineSweeper")

    # Create grid for bombs
    grid = []
    for row in range(gridSizeX):
        grid.append([])
        for column in range(gridSizeY):
            # Marks all locations as empty
            grid[row].append(0)

    # Create mines and add to grid
    mines = 0
    i = 0
    while i < numberOfMines:
        x = random.randrange(0, gridSizeX)
        y = random.randrange(0, gridSizeY)
        if grid[x][y] != 10:
            grid[x][y] = 10
            mines += 1
            i += 1
        else:
            i -= 1

    # Add numbers to surrounding bomb locations on grid
    for row in range(gridSizeX):
        for column in range(gridSizeY):
            if grid[row][column] >= 10:
                if row < gridSizeX - 1 and not grid[row + 1][column] == 10:
                    grid[row + 1][column] += 1
                if column < gridSizeY - 1 and not grid[row][column + 1] == 10:
                    grid[row][column + 1] += 1
                if row > 0 and not grid[row - 1][column] == 10:
                    grid[row - 1][column] += 1
                if column > 0 and not grid[row][column - 1] == 10:
                    grid[row][column - 1] += 1
                if row < gridSizeX - 1 and column < gridSizeY - 1 and not grid[row + 1][column + 1] == 10:
                    grid[row + 1][column + 1] += 1
                if row < gridSizeX - 1 and column > 0 and not grid[row + 1][column - 1] == 10:
                    grid[row + 1][column - 1] += 1
                if row > 0 and column < gridSizeY - 1 and not grid[row - 1][column + 1] == 10:
                    grid[row - 1][column + 1] += 1
                if row > 0 and column > 0 and not grid[row - 1][column - 1] == 10:
                    grid[row - 1][column - 1] += 1

    # Display grid in console
    for row in range(gridSizeX):
        for column in range(gridSizeY):
            print(grid[row][column], end=" ") 
        print()

    # Find a location with no bomb for game start
    for row in range(gridSizeX):
        for column in range(gridSizeY):
            if grid[row][column] == 0:
                xSafe = row
                ySafe = column

    # Function to reveal surrounding squares
    def check_adjacent_cells(x, y):
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                new_x = x + i
                new_y = y + j
                if 0 <= new_x < gridSizeX and 0 <= new_y < gridSizeY:
                    if grid[new_x][new_y] == 0:
                        grid[new_x][new_y] = 9
                        check_adjacent_cells(new_x, new_y)
                    if grid[new_x][new_y] > 0 and grid[new_x][new_y] < 9:
                        grid[new_x][new_y] *= -1      

    # Loop until the user clicks the close button or endgame condition met.
    done = False 
    # How many safe locations on map
    safeLocations = (gridSizeX * gridSizeY) - numberOfMines
    # If left or right click is happening
    left = False
    right = False
    # Keep track of revealed squares to later determine if all mines have been found
    revealed = 0
    # Timer
    startTime = 0
    # Mine Count
    remaining_mines = numberOfMines
    
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    
    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        x = xSafe
        y = ySafe


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            # Click Down
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                y = pos[0] // 25
                x = pos[1] // 25
                if event.button == LEFT:
                    left = True
                    # Start Timer
                    if start_time == 0:
                        start_time = time.time()
                if event.button == RIGHT:
                    right = True

            # Left Click Up
            elif event.type == pygame.MOUSEBUTTONUP and event.button == LEFT and not right:
                pos = pygame.mouse.get_pos()
                y = pos[0] // 25
                x = pos[1] // 25
                #print("Click: (%s,%s) Value: %s"%(x,y,grid[x][y]))
                left = False

                # If left click on bomb game over
                if grid[x][y] == 10:
                    print("Game Over")
                    pygame.time.wait(1000)
                    done = True
                
                # If next to bomb make number negative to later check and reveal
                elif grid[x][y] > 0 and grid[x][y] < 9:
                    grid[x][y] *= -1
                    xSafe = x
                    ySafe = y
                
                # If square is empty reveal surrounding empty squares
                elif grid[x][y] == 0:
                    grid[x][y] = 9
                    xSafe = x
                    ySafe = y
                    check_adjacent_cells(x, y)

            # Right Click
            elif event.type == pygame.MOUSEBUTTONUP and event.button == RIGHT and not left:
                pos = pygame.mouse.get_pos()
                y = pos[0] // 25
                x = pos[1] // 25
                #print("Bomb Marked")
                right = False

                # Mark only squares that are unrevaled as possible bomb locations
                if grid[x][y] == 10:
                    grid[x][y] = 20
                elif grid[x][y] < 9 and grid[x][y] > 0:
                    grid[x][y] += 10
                elif grid[x][y] == 20:
                    grid[x][y] = 10
                elif grid[x][y] < 20 and grid[x][y] > 10:
                    grid[x][y] -= 10

            # Both Left and Right Click
            elif event.type == pygame.MOUSEBUTTONUP and left and right:
                pos = pygame.mouse.get_pos()
                y = pos[0] // 25
                x = pos[1] // 25
                right = False
                left = False

                # If both click revealed tile reveal surrounding tiles even if one is a bomb
                if grid[x][y] < 0:
                    for i in (-1, 0, 1):
                        for j in (-1, 0, 1):
                            if x + i >= 0 and y + j >= 0 and x + i <= gridSizeX - 1 and y + j <= gridSizeY - 1:
                                if grid[x + i][y + j] == 0:
                                    check_adjacent_cells(x, y)
                                elif grid[x + i][y + j] > 0 and grid[x + i][y + j] < 9:
                                    grid[x + i][y + j] *= -1

                

                
        # If you want a background image, replace this clear with blit'ing the
        # background image.
        screen.fill(BLACK)

        # --- Game logic should go here

        text = ""
        
        # If all mines found end game
        if safeLocations == revealed:
            print("You Win")
            pygame.time.wait(3000)
            done = True
            
        #print(revealed)
        
    
        # --- Screen-clearing code goes here
    
        # Here, we clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
    
        
    
        # --- Drawing code should go here
        revealed = 0
        
        # Draw top bar scoreboard
        pygame.draw.rect(screen, GRAY, [0, 0, windowSize[0], 40])

        # Timer
        current_time = int(time.time() - start_time)
        time_text = font.render(f'Time: {current_time}', True, BLACK)
        screen.blit(time_text, (20, 10))

        # Mine Count 
        mines_text = font.render(f'Remaining Mines: {remaining_mines}', True, BLACK)
        screen.blit(mines_text, (windowSize[0] - mines_text.get_width() - 20, 10))

        for row in range(gridSizeX):
            for column in range(gridSizeY):
                color = GRAY

                if grid[row][column] >= 50:
                    color = BLACK

                # Change background to white for all empty squares that have been clicked on
                if grid[row][column] == 9 :
                    color = WHITE
                    revealed += 1

                # Flag possible bomb location
                if grid[row][column] > 10:
                    color = RED
                
                # Change background to white if square has been clicked on
                if grid[row][column] < 0:
                    color = WHITE
                    revealed += 1

                # Draw grid
                pygame.draw.rect(screen,
                                color,
                                [(MARGIN + WIDTH) * column + MARGIN,
                                (MARGIN + HEIGHT) * row + MARGIN,
                                WIDTH,
                                HEIGHT])
                
                # Ouputs number in box if it is negative indicating it is next to a bomb and has been clicked on
                if grid[row][column] < 0:
                    text = font.render(str(abs(grid[row][column])), True, BLACK)
                    text_rect = text.get_rect(center=((column * 25) + WIDTH // 2 + 5, (row * 25) + HEIGHT // 2 + 5))
                    screen.blit(text, text_rect)
                
        
        pygame.display.flip()
        clock.tick(60)
    
    # Close the window and quit.
    pygame.quit()