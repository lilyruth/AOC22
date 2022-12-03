import math

priority_value = 0
common = []
total_count = 0

f = open("Day3/day_3_input.txt", "r")
lines = f.readlines()
for line in lines: 
    contents = list(line)
    contents.remove('\n')
    total_count = total_count+1
    count = len(contents)
    split = math.floor(count/2)
    first = contents[:split]
    second = contents[split:]
    
    line_common = ""
    for char in second : 
        if first.count(char) : 
            line_common = char
    common.append(line_common)    
print(common)
for char in common : 
    if ord(char) > 96 : 
        priority_value += (ord(char) - 96)
    else : priority_value += (ord(char) - 38)
print(f"The total value is {priority_value}")
print(total_count)
