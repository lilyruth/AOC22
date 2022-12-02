
points_total = 0

f = open("Day2/day_2_input.txt", "r")
for line in f: 
    round = []
    for char in line:
        if char != " " and char != "\n" : round.append(char)
    if (round[0] == "A" and round[1] == "X") : points_total += 4
    if (round[0] == "B" and round[1] == "Y") : points_total += 5
    if (round[0] == "C" and round[1] == "Z") : points_total += 6
    if (round[0] == "A" and round[1] == "Y") : points_total += 8
    if (round[0] == "B" and round[1] == "Z") : points_total += 9
    if (round[0] == "C" and round[1] == "X") : points_total += 7
    if (round[0] == "A" and round[1] == "Z") : points_total += 3
    if (round[0] == "B" and round[1] == "X") : points_total += 1
    if (round[0] == "C" and round[1] == "Y") : points_total += 2

    print(points_total)
        
print(f"The total points are {points_total}")