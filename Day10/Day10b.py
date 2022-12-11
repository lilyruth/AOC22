cycle = 1
current_draw = (cycle - 1) % 40
x = 1

current_sprite_1 = 0
current_sprite_2 = 1
current_sprite_3 = 2

count = 0
rows = 0
CRT = []

while len(CRT) < 6:
    row = []
    while len(row) < 40:
        row.append(' ')
    CRT.append(row)

f = open("Day10/day_10_input.txt", "r")
lines = f.readlines()
for line in lines: 
    line = line.rstrip('\n')
    line = line.split(' ')

    if current_sprite_1 == current_draw or current_sprite_2 == current_draw or current_sprite_3 == current_draw:
        row = int(cycle / 40)
        col = (cycle - 1) % 40
        CRT[row][col] = '#'

    if line[0] == 'noop': 
        cycle+=1
        current_draw = (cycle - 1) % 40 

    else: 

        if current_sprite_1 == current_draw or current_sprite_2 == current_draw or current_sprite_3 == current_draw:
            row = int(cycle / 40)
            col = (cycle - 1) % 40
            CRT[row][col] = '#'

        add_val = int(line[1])
        cycle += 1
        current_draw = (cycle - 1) % 40 

        if current_sprite_1 == current_draw or current_sprite_2 == current_draw or current_sprite_3 == current_draw:
            row = int(cycle / 40)
            col = (cycle - 1) % 40
            CRT[row][col] = '#'
        
        cycle += 1  
        current_draw = (cycle - 1) % 40 

        x += add_val
        current_sprite_1 = x - 1
        current_sprite_2 = x 
        current_sprite_3 = x + 1

print(CRT)
    
