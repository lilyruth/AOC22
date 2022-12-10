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

two_x = 500
two_y = 500

three_x = 500
three_y = 500

four_x = 500
four_y = 500

five_x = 500
five_y = 500

six_x = 500
six_y = 500

seven_x = 500
seven_y = 500

eight_x = 500
eight_y = 500

nine_x = 500
nine_y = 500


head_position = grid[head_x][head_y]
two_position = grid[two_x][two_y]
three_position = grid[three_x][three_y]
four_position = grid[four_x][four_y]
five_position = grid[five_x][five_y]
six_position = grid[six_x][six_y]
seven_position = grid[seven_x][seven_y]
eight_position = grid[eight_x][eight_y]
nine_position = grid[nine_x][nine_y]
tail_position = grid[tail_x][tail_y]

tail_visits = {
    tail_position
}

def determine_direction(lead_position_x, lead_position_y, current_position_x, current_position_y):
    if lead_position_y == current_position_y:
        if lead_position_x > current_position_x:
            return 'D'
        elif lead_position_x < current_position_x:
            return 'U'
    elif lead_position_x == current_position_x:
        if lead_position_y > current_position_y:
            return 'R'
        elif lead_position_y < current_position_y:
            return 'L'
    else:
        diff_x = abs(lead_position_x - current_position_x)
        diff_y = abs(lead_position_y - current_position_y)
        if diff_x > diff_y:
            if lead_position_x > current_position_x:
                return 'D'
            elif lead_position_x < current_position_x:
                return 'U'
        else:
            if lead_position_y > current_position_y:
                return 'R'
            elif lead_position_y < current_position_y:
                return 'L'

def move(direction, lead_position_x, lead_position_y, current_position_x, current_position_y):
    if direction == 'R':
        x_diff = abs(lead_position_x - current_position_x)
        y_diff = abs(lead_position_y - current_position_y)
        
        if y_diff > 1 and x_diff > 0:
            current_position_y += 1
            if lead_position_x > current_position_x: current_position_x += 1
            else: current_position_x -= 1
        elif y_diff > 1:
            current_position_y += 1

    elif direction == 'L':
        x_diff = abs(lead_position_x - current_position_x)
        y_diff = abs(lead_position_y - current_position_y)

        if y_diff > 1 and x_diff > 0:
            current_position_y -= 1
            if lead_position_x > current_position_x: current_position_x += 1
            else: current_position_x -= 1
        elif y_diff > 1:
            current_position_y -= 1

    elif direction == 'U':
        x_diff = abs(lead_position_x - current_position_x)
        y_diff = abs(lead_position_y - current_position_y)
        if x_diff > 1 and y_diff > 0:
            current_position_x -= 1
            if lead_position_y > current_position_y: current_position_y += 1
            else: current_position_y -= 1
        elif x_diff > 1:
            current_position_x -= 1

    elif direction == 'D':
        x_diff = abs(lead_position_x - current_position_x)
        y_diff = abs(lead_position_y - current_position_y)
        if x_diff > 1 and y_diff > 0:
            current_position_x += 1
            if lead_position_y > current_position_y: current_position_y += 1
            else: current_position_y -= 1
        elif x_diff > 1:
            current_position_x += 1
    return [current_position_x, current_position_y]


f = open("Day9/day_9_input.txt", "r")
lines = f.readlines()
for line in lines: 
    line = line.rstrip('\n')
    line_parse = line.split(' ')
    initial_direction = line_parse[0]
    count = int(line_parse[1])
    print(initial_direction, count)

    if initial_direction == 'R': 
        target_value = head_y + count
        while head_y < target_value:
            head_y += 1

            direction = determine_direction(head_x, head_y, two_x, two_y)
            new_two = move(direction, head_x, head_y, two_x, two_y)
            two_x = new_two[0]
            two_y = new_two[1]

            direction = determine_direction(two_x, two_y, three_x, three_y)
            new_three = move(direction, two_x, two_y, three_x, three_y)
            three_x = new_three[0]
            three_y = new_three[1]

            direction = determine_direction(three_x, three_y, four_x, four_y)
            new_four = move(direction, three_x, three_y, four_x, four_y)
            four_x = new_four[0]
            four_y = new_four[1]

            direction = determine_direction(four_x, four_y, five_x, five_y)
            new_five = move(direction, four_x, four_y, five_x, five_y)
            five_x = new_five[0]
            five_y = new_five[1]

            direction = determine_direction(five_x, five_y, six_x, six_y)
            new_six = move(direction, five_x, five_y, six_x, six_y)
            six_x = new_six[0]
            six_y = new_six[1]

            direction = determine_direction(six_x, six_y, seven_x, seven_y)
            new_seven = move(direction, six_x, six_y, seven_x, seven_y)
            seven_x = new_seven[0]
            seven_y = new_seven[1]

            direction = determine_direction(seven_x, seven_y, eight_x, eight_y)
            new_eight = move(direction, seven_x, seven_y, eight_x, eight_y)
            eight_x = new_eight[0]
            eight_y = new_eight[1]

            direction = determine_direction(eight_x, eight_y, nine_x, nine_y)
            new_nine = move(direction, eight_x, eight_y, nine_x, nine_y)
            nine_x = new_nine[0]
            nine_y = new_nine[1]

            direction = determine_direction(nine_x, nine_y, tail_x, tail_y)
            new_tail = move(direction, nine_x, nine_y, tail_x, tail_y)
            tail_x = new_tail[0]
            tail_y = new_tail[1]

            tail_position = grid[tail_x][tail_y]
            tail_visits.add(tail_position)
            print(f"The head is located at {grid[head_x][head_y]}. The tail is located at {grid[tail_x][tail_y]}")
    
    elif initial_direction == 'L':
        target_value = head_y - count
        while head_y > target_value:
            head_y -= 1

            direction = determine_direction(head_x, head_y, two_x, two_y)
            new_two = move(direction, head_x, head_y, two_x, two_y)
            two_x = new_two[0]
            two_y = new_two[1]

            direction = determine_direction(two_x, two_y, three_x, three_y)
            new_three = move(direction, two_x, two_y, three_x, three_y)
            three_x = new_three[0]
            three_y = new_three[1]       

            direction = determine_direction(three_x, three_y, four_x, four_y)
            new_four = move(direction, three_x, three_y, four_x, four_y)
            four_x = new_four[0]
            four_y = new_four[1]

            direction = determine_direction(four_x, four_y, five_x, five_y)
            new_five = move(direction, four_x, four_y, five_x, five_y)
            five_x = new_five[0]
            five_y = new_five[1]

            direction = determine_direction(five_x, five_y, six_x, six_y)
            new_six = move(direction, five_x, five_y, six_x, six_y)
            six_x = new_six[0]
            six_y = new_six[1]

            direction = determine_direction(six_x, six_y, seven_x, seven_y)
            new_seven = move(direction, six_x, six_y, seven_x, seven_y)
            seven_x = new_seven[0]
            seven_y = new_seven[1]

            direction = determine_direction(seven_x, seven_y, eight_x, eight_y)
            new_eight = move(direction, seven_x, seven_y, eight_x, eight_y)
            eight_x = new_eight[0]
            eight_y = new_eight[1]

            direction = determine_direction(eight_x, eight_y, nine_x, nine_y)
            new_nine = move(direction, eight_x, eight_y, nine_x, nine_y)
            nine_x = new_nine[0]
            nine_y = new_nine[1]

            direction = determine_direction(nine_x, nine_y, tail_x, tail_y)
            new_tail = move(direction, nine_x, nine_y, tail_x, tail_y)
            tail_x = new_tail[0]
            tail_y = new_tail[1]

            tail_position = grid[tail_x][tail_y]
            tail_visits.add(tail_position)
            print(f"The head is located at {grid[head_x][head_y]}. The tail is located at {grid[tail_x][tail_y]}")

    elif initial_direction == 'U': 
        target_value = head_x - count
        while head_x > target_value:
            head_x -= 1

            direction = determine_direction(head_x, head_y, two_x, two_y)
            new_two = move(direction, head_x, head_y, two_x, two_y)
            two_x = new_two[0]
            two_y = new_two[1]

            direction = determine_direction(two_x, two_y, three_x, three_y)
            new_three = move(direction, two_x, two_y, three_x, three_y)
            three_x = new_three[0]
            three_y = new_three[1]           

            direction = determine_direction(three_x, three_y, four_x, four_y)
            new_four = move(direction, three_x, three_y, four_x, four_y)
            four_x = new_four[0]
            four_y = new_four[1]

            direction = determine_direction(four_x, four_y, five_x, five_y)
            new_five = move(direction, four_x, four_y, five_x, five_y)
            five_x = new_five[0]
            five_y = new_five[1]

            direction = determine_direction(five_x, five_y, six_x, six_y)
            new_six = move(direction, five_x, five_y, six_x, six_y)
            six_x = new_six[0]
            six_y = new_six[1]

            direction = determine_direction(six_x, six_y, seven_x, seven_y)
            new_seven = move(direction, six_x, six_y, seven_x, seven_y)
            seven_x = new_seven[0]
            seven_y = new_seven[1]

            direction = determine_direction(seven_x, seven_y, eight_x, eight_y)
            new_eight = move(direction, seven_x, seven_y, eight_x, eight_y)
            eight_x = new_eight[0]
            eight_y = new_eight[1]

            direction = determine_direction(eight_x, eight_y, nine_x, nine_y)
            new_nine = move(direction, eight_x, eight_y, nine_x, nine_y)
            nine_x = new_nine[0]
            nine_y = new_nine[1]

            direction = determine_direction(nine_x, nine_y, tail_x, tail_y)
            new_tail = move(direction, nine_x, nine_y, tail_x, tail_y)
            tail_x = new_tail[0]
            tail_y = new_tail[1]

            tail_position = grid[tail_x][tail_y]
            tail_visits.add(tail_position)
            print(f"The head is located at {grid[head_x][head_y]}. The tail is located at {grid[tail_x][tail_y]}")

    elif initial_direction == 'D':
        target_value = head_x + count
        while head_x < target_value:
            head_x += 1

            direction = determine_direction(head_x, head_y, two_x, two_y)
            new_two = move(direction, head_x, head_y, two_x, two_y)
            two_x = new_two[0]
            two_y = new_two[1]

            direction = determine_direction(two_x, two_y, three_x, three_y)
            new_three = move(direction, two_x, two_y, three_x, three_y)
            three_x = new_three[0]
            three_y = new_three[1]

            direction = determine_direction(three_x, three_y, four_x, four_y)
            new_four = move(direction, three_x, three_y, four_x, four_y)
            four_x = new_four[0]
            four_y = new_four[1]

            direction = determine_direction(four_x, four_y, five_x, five_y)
            new_five = move(direction, four_x, four_y, five_x, five_y)
            five_x = new_five[0]
            five_y = new_five[1]

            direction = determine_direction(five_x, five_y, six_x, six_y)
            new_six = move(direction, five_x, five_y, six_x, six_y)
            six_x = new_six[0]
            six_y = new_six[1]

            direction = determine_direction(six_x, six_y, seven_x, seven_y)
            new_seven = move(direction, six_x, six_y, seven_x, seven_y)
            seven_x = new_seven[0]
            seven_y = new_seven[1]

            direction = determine_direction(seven_x, seven_y, eight_x, eight_y)
            new_eight = move(direction, seven_x, seven_y, eight_x, eight_y)
            eight_x = new_eight[0]
            eight_y = new_eight[1]

            direction = determine_direction(eight_x, eight_y, nine_x, nine_y)
            new_nine = move(direction, eight_x, eight_y, nine_x, nine_y)
            nine_x = new_nine[0]
            nine_y = new_nine[1]

            direction = determine_direction(nine_x, nine_y, tail_x, tail_y)
            new_tail = move(direction, nine_x, nine_y, tail_x, tail_y)
            tail_x = new_tail[0]
            tail_y = new_tail[1]

            tail_position = grid[tail_x][tail_y]
            tail_visits.add(tail_position)
            print(f"The head is located at {grid[head_x][head_y]}. The tail is located at {grid[tail_x][tail_y]}")
    
print(tail_visits)
print(f"The total number of places the tail visited is {len(tail_visits)}")

    





