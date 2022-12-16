
terrain = []


f = open("Day12/day_12_input.txt", "r")
lines = f.readlines()
for line in lines: 
    line=line.rstrip('\n')
    row = []
    for char in line:
        if char != 'S' and char != 'E': row.append(int(ord(char)))
        elif char == 'E': row.append(123)
        elif char == 'S': row.append(97)
    terrain.append(row)

print(terrain)

q = [[[20,0]]]
mapped = []
current_value = terrain[0][0]
print(current_value)

while current_value != 123:
    path = q.pop(0)
    coordinates = path[-1]
    x = coordinates[0]
    y = coordinates[1]
    current_value = terrain[x][y]
    mapped.append(coordinates)

    #left
    left = [x, y-1]
    if y-1 >= 0 and terrain[x][y-1] <= current_value + 1 and mapped.count(left) == 0:
        left_path = path[:]
        left_path.append(left)
        q.append(left_path)

    #right
    right = [x, y+1]
    if y+1 < len(terrain[0]) and terrain[x][y+1] <= current_value + 1 and mapped.count(right) == 0:
        right_path = path[:]
        right_path.append(right)
        q.append(right_path)

    #up 
    up = [x-1, y]
    if x-1 >= 0 and terrain[x-1][y] <= current_value + 1 and mapped.count(up) == 0:
        up_path = path[:]
        up_path.append(up)
        q.append(up_path)

    #down
    down = [x+1, y]
    if x+1 < len(terrain) and terrain[x+1][y] <= current_value + 1 and mapped.count(down) == 0:
        down_path = path[:]
        down_path.append(down)
        q.append(down_path)
        print('down appended')


print(len(path))


