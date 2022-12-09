tree_grid = []
rotated_tree_grid = []

max_scenic_view = 0

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

x = 1

while x < length:
    y = 1
    while y < length:
        curr_tree = tree_grid[x][y]
        tree_slice_left = tree_grid[x][:y]
        tree_slice_left.reverse()
        scenic_view_left = 0
        for tree in tree_slice_left:
            if curr_tree > tree:
                scenic_view_left += 1
            if curr_tree <= tree:
                scenic_view_left += 1
                break
        tree_slice_right = tree_grid[x][y+1:]
        scenic_view_right = 0
        for tree in tree_slice_right:
            if curr_tree > tree:
                scenic_view_right += 1
            if curr_tree <= tree:
                scenic_view_right += 1
                break
        tree_slice_up = rotated_tree_grid[y][:x]
        tree_slice_up.reverse()
        scenic_view_up = 0
        for tree in tree_slice_up:
            if curr_tree > tree:
                scenic_view_up += 1
            if curr_tree <= tree:
                scenic_view_up += 1
                break
        tree_slice_down = rotated_tree_grid[y][x+1:]
        scenic_view_down = 0
        for tree in tree_slice_down:
            if curr_tree > tree:
                scenic_view_down += 1
            if curr_tree <= tree:
                scenic_view_down += 1
                break
        scenic_score = scenic_view_left * scenic_view_right * scenic_view_up * scenic_view_down
        max_scenic_view = max(max_scenic_view, scenic_score)
        y+=1
    x+=1

print(max_scenic_view)