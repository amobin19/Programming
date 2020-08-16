# Ayman Mobin, Actual 09/15/2017
up_down = 0 # vertical grid counter
right_left = 0 # horizontal grid counter
grid = [] # list to hold each new grid position [similar to (x,y) coordinate system]
while(True):
    direction = input("Select w, s, d, or a to tell the driver where to go: ") # arrow input is taken
    if(direction == "w"):
        up_down += 1 # if north increase vertical by 1 on grid
        if((right_left, up_down) not in grid): 
            grid.append((right_left, up_down)) # add to grid list if new position
    elif(direction == "s"):
        up_down -= 1 # if south decrease vertical by 1 on grid
        if((right_left, up_down) not in grid):
            grid.append((right_left, up_down)) # add to grid list if new position
    elif(direction == "d"): 
        right_left += 1 # if east increase horizontal by 1 on grid
        if((right_left, up_down) not in grid):
            grid.append((right_left, up_down)) # add to grid list if new position
    elif(direction == "a"):
        right_left -= 1 # if west decrease horizontal by 1 on grid
        if((right_left, up_down) not in grid):
            grid.append((right_left, up_down)) # add to grid list if new position 
    else:
        break # break out of loop if not arrow input
print("The turtle has been to a total of", len(grid), "points.") # prints total stores visited 