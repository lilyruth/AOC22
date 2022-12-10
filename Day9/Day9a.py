grid = []

count = 0

while len(grid) < 1000:
    row = []
    while len(row) < 1000:
        row.append(count)
        count += 1
    grid.append(row)

head_x = 500
head_y = 500

tail_x = 500
tail_y = 500

head_position = grid[head_x][head_y]
tail_position = grid[tail_x][tail_y]

tail_visits = {
    tail_position
}

f = open("Day9/day_9_input.txt", "r")
lines = f.readlines()
for line in lines: 
    line = line.rstrip('\n')
    line_parse = line.split(' ')
    direction = line_parse[0]
    count = int(line_parse[1])
    print(direction, count)

    if direction == 'R':
        target_value = head_y + count
        while head_y < target_value:
            head_y += 1
            x_diff = abs(head_x - tail_x)
            y_diff = abs(head_y - tail_y)
            if y_diff > 1 and x_diff > 0:
                tail_y += 1
                if head_x > tail_x: tail_x += 1
                else: tail_x -=1
            elif y_diff > 1:
                tail_y += 1
            tail_position = grid[tail_x][tail_y]
            tail_visits.add(tail_position)
            print(f"The head is located at {grid[head_x][head_y]}. The tail is located at {grid[tail_x][tail_y]}")
    elif direction == 'L':
        target_value = head_y - count
        while head_y > target_value:
            head_y -= 1
            x_diff = abs(head_x - tail_x)
            y_diff = abs(head_y - tail_y)
            if y_diff > 1 and x_diff > 0:
                tail_y -= 1
                if head_x > tail_x: tail_x += 1
                else: tail_x -=1
            elif y_diff > 1:
                tail_y -= 1
            tail_position = grid[tail_x][tail_y]
            tail_visits.add(tail_position)
            print(f"The head is located at {grid[head_x][head_y]}. The tail is located at {grid[tail_x][tail_y]}")
    elif direction == 'U':
        target_value = head_x - count
        while head_x > target_value:
            head_x -= 1
            x_diff = abs(head_x - tail_x)
            y_diff = abs(head_y - tail_y)
            if x_diff > 1 and y_diff > 0:
                tail_x -= 1
                if head_y > tail_y: tail_y += 1
                else: tail_y -= 1
            elif x_diff > 1:
                tail_x -= 1
            tail_position = grid[tail_x][tail_y]
            tail_visits.add(tail_position)
            print(f"The head is located at {grid[head_x][head_y]}. The tail is located at {grid[tail_x][tail_y]}")
    elif direction == 'D':
        target_value = head_x + count
        while head_x < target_value:
            head_x += 1
            x_diff = abs(head_x - tail_x)
            y_diff = abs(head_y - tail_y)
            if x_diff > 1 and y_diff > 0:
                tail_x += 1
                if head_y > tail_y: tail_y += 1
                else: tail_y -= 1
            elif x_diff > 1:
                tail_x += 1
            tail_position = grid[tail_x][tail_y]
            tail_visits.add(tail_position)
            print(f"The head is located at {grid[head_x][head_y]}. The tail is located at {grid[tail_x][tail_y]}")
print(tail_visits)
print(f"The total number of places the tail visited is {len(tail_visits)}")

    





