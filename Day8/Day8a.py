tree_grid = []
rotated_tree_grid = []

visible_tree_count = 0

f = open("Day8/day_8_input.txt", "r")
lines = f.readlines()
for line in lines: 
    line = line.rstrip('\n')
    tree_row = []
    for tree in line:
        tree_row.append(int(tree))
    tree_grid.append(tree_row)
length = len(tree_grid)
width = len(tree_grid[0])

x = 0
y = 0

while x < length:
    tree_row = []
    y = 0
    while y < width:
        tree_row.append(tree_grid[y][x])
        y+=1
    rotated_tree_grid.append(tree_row)
    x += 1

x = 0

while x < length:
    y = 0
    while y < length:
        if x == 0 or y == 0 or x == length - 1 or y == width - 1:
            visible_tree_count += 1
        else: 
            curr_tree = tree_grid[x][y]
            tree_slice_left = tree_grid[x][:y]
            tree_slice_right = tree_grid[x][y+1:]
            tree_slice_up = rotated_tree_grid[y][:x]
            tree_slice_down = rotated_tree_grid[y][x+1:]
            if curr_tree > max(tree_slice_left) or curr_tree > max(tree_slice_right) or curr_tree > max(tree_slice_up) or curr_tree > max(tree_slice_down):
                visible_tree_count += 1
        y+=1
    x+=1

print(visible_tree_count)