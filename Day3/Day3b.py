import math

priority_value = 0
sacks = []
badges = []


f = open("Day3/day_3_input.txt", "r")
lines = f.readlines()
for line in lines: 
    sacks.append(line)

while (len(lines) > 0) : 
    set = []
    list1 = []
    list2 = []
    list3 = []
    common = ""
    for x in range(3) :
        line = lines.pop(0)
        set.append(line)
    for line in set : 
        line1 = set.pop(0)
        for char in line1 : list1.append(char)
        list1.pop(-1)
        line2 = set.pop(0)
        for char in line2 : list2.append(char)
        list2.pop(-1)
        line3 = set.pop(0)
        for char in line3 :  list3.append(char)
        list3.pop(-1)
        for char in list1 : 
            if list2.count(char) and list3.count(char) : 
                common = char
        badges.append(common)
print(badges) 
for char in badges : 
    if ord(char) > 96 : 
        priority_value += (ord(char) - 96)
    else : priority_value += (ord(char) - 38)
print(f"The total value is {priority_value}")
