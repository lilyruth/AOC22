sections = 0

f = open("Day4/day_4_input.txt", "r")
lines = f.readlines()
for line in lines: 
    assignments = line.split(',')
    assignments[1] = assignments[1].replace('\n', '')
    first_section = assignments[0].split('-')
    first_section_start = int(first_section[0])
    first_section_finish = int(first_section[-1])
    second_section = assignments[1].split('-')
    second_section_start = int(second_section[0])
    second_section_finish = int(second_section[-1])
    counted = False
    if first_section_start >= second_section_start and first_section_finish <= second_section_finish : 
        sections+= 1
        counted = True
    if second_section_start >= first_section_start and second_section_finish <= first_section_finish and counted == False: 
        sections+= 1

print(f"The total value is {sections}")

