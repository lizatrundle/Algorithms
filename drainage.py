
# dynamic programming assignment --> water drainagae system

#backtracking isnt needed because we only need the length of the longest drain, we dont need to spots that gave to that longest drain 

# import readline

#this is the main function of the program 
def find_longest_drain(heights, paths, input_grid):
    num_columns = len(input_grid)
    num_rows = len(input_grid[0])

    for height in heights:
        grid_point = height[0]
        x = height[1]
        y = height[2]

        #now check every case, in surrounding cases
        #check up, down, left, right to fit constraints of problem for finding possible drains 

       #up 
       
        if x-1 >= 0 and input_grid[x-1][y] < grid_point:
            paths[(x-1, y)] = paths[(x,y)] + 1 if paths[(x,y) ] + 1 > paths[(x-1, y)] else paths[(x-1, y)]
        #down 

        if x+1 < num_columns and input_grid[x+1][y] < grid_point:
            paths[(x+1, y)] = paths[(x,y)] + 1 if paths[(x,y) ] + 1 > paths[(x+1, y)] else paths[(x+1, y)]

        
        #left 
        if y-1 >= 0 and input_grid[x][y-1] < grid_point:
            paths[(x, y-1)] = paths[(x,y)] + 1 if paths[(x,y) ] + 1 > paths[(x, y-1)] else paths[(x, y-1)]


         #right 
        if y+1 < num_rows and input_grid[x][y+1] < grid_point:
            paths[(x, y+1)] = paths[(x,y)] + 1 if paths[(x,y) ] + 1 > paths[(x,y+1)] else paths[(x, y+1)]
       
        
        #turn path dict into a list to be able to take the max 
    path_list = list(paths.values())
    return max(path_list)

def init_grid(input_grid):
    paths = {}
    heights = []

    num_columns = len(input_grid)
    num_rows = len(input_grid[0])
    for x in range(num_columns):
        for y in range(num_rows):
            #initalize the drain map to hold -1 initially, update if path is longest 
            paths[(x,y)] = 1
            heights.append([input_grid[x][y], x, y])
    
    #sort the heights by descending order of length, to get longest path first 
    heights.sort(key=lambda grid: grid[0], reverse=True)
    return_list = [heights, paths]
    return return_list

#main 
# test = open("drain.txt")
# num_test = test.readline()
num_test = input()
answer_list = []

#num_tests = input()
for x in range(int(num_test)):
    # line_1 = input().split()
    line_1 = input().strip().split()
    name = line_1[0]
    rows = int(line_1[1])
    cols = int(line_1[2])
    matrix = []
    for y in range(rows):
        row = [int(num) for num in input().strip().split()]
        matrix.append(row)
    
    # print(matrix, x)
    
    answer = init_grid(matrix)
    # print(answer[0], answer[1])
    final = find_longest_drain(answer[0], answer[1], matrix)

    print(name + ": " + str(final))

    answer_list.append(answer)
