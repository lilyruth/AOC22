line_number = 1

crates = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []
]

directions = []

f = open("Day5/day_5_input.txt", "r")
lines = f.readlines()

for line in lines: 
    if line[0] == "m" :
        line = line.replace("\n", "")
        directions.append(line)
    else : 
        count = 0
        for char in line: 
            if count == 1 and char != " ": crates[0].append(char)
            if count == 5 and char != " " : crates[1].append(char)
            if count == 9 and char != " " : crates[2].append(char)
            if count == 13 and char != " " : crates[3].append(char)
            if count == 17 and char != " " : crates[4].append(char)
            if count == 21 and char != " " : crates[5].append(char)
            if count == 25 and char != " " : crates[6].append(char)
            if count == 29 and char != " " : crates[7].append(char)
            if count == 33 and char != " " : crates[8].append(char)
            count+=1

for crate in crates : crate.pop(-1)

for direction in directions : 
    direction = direction.replace("move", "")
    direction = direction.replace("from", "")
    direction = direction.replace("to", "")
    direction = direction.replace(" ", "")
    if len(direction) == 3 : 
        crates_to_move = int(direction[0])
        original_crate = int(direction[1]) -1
        new_crate = int(direction[2]) -1
    else : 
        crates_to_move = int(direction[0:2])
        original_crate = int(direction[2]) -1
        new_crate = int(direction[3]) -1
    print(crates_to_move) 
    crate_set = crates[original_crate][0:crates_to_move]
    remaining_set = crates[original_crate][crates_to_move:]
    crates[original_crate] = remaining_set
    new_set = crate_set + crates[new_crate] 
    crates[new_crate] = new_set
    print(crates[original_crate], crates[new_crate])
  

message = ""

for crate in crates : 
    message += crate[0]

print(message)

  



