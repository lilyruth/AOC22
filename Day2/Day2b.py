points_total = 0

f = open("Day2/day_2_input.txt", "r")
for line in f: 
    round = []
    for char in line:
        if char != " " and char != "\n" : round.append(char)
    if (round[1] == "X") : 
        if (round[0] == "A") : points_total += 3
        if (round[0] == "B") : points_total += 1 
        if (round[0] == "C") : points_total += 2
    if (round[1] == "Y") : 
        if (round[0] == "A") : points_total += 4
        if (round[0] == "B") : points_total += 5 
        if (round[0] == "C") : points_total += 6
    if (round[1] == "Z") : 
        if (round[0] == "A") : points_total += 8
        if (round[0] == "B") : points_total += 9 
        if (round[0] == "C") : points_total += 7
   

    print(points_total)
        
print(f"The total points are {points_total}")