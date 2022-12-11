cycle = 1
x = 1
cycles = []

f = open("Day10/day_10_input.txt", "r")
lines = f.readlines()
for line in lines: 
    line = line.rstrip('\n')
    line = line.split(' ')
    if line[0] == 'noop': 
        if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
            cycles.append(x * cycle)
            print(f"The cycle is {cycle} and x is {x}")
        cycle+=1 
    else: 
        add_val = int(line[1])
        if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
            cycles.append(x * cycle)
            print(f"The cycle is {cycle} and x is {x}")
        cycle += 1
        if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
            cycles.append(x * cycle)
            print(f"The cycle is {cycle} and x is {x}")  
        cycle += 1  
        x += add_val
    print(f"The cycle is {cycle} and x is {x}")
    

print(f"The list is {cycles} and total value is {sum(cycles)}")

