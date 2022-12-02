working_sum = 0
high_sum = 0

f = open("day_1_input.txt", "r")
for num in f: 
    if num != "\n" : 
        num = int(num)
        working_sum += num
        print(working_sum)
        if high_sum < working_sum : high_sum = working_sum
    else : 
        working_sum = 0
print(f"The high_sum is {high_sum}")