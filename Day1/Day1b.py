working_sum = 0
first_sum = 0
second_sum = 0
third_sum = 0



f = open("Day1/day_1_input.txt", "r")
for num in f: 
    if num != "\n" : 
        num = int(num)
        working_sum += num
        
    else : 
        if working_sum < first_sum and working_sum < second_sum and working_sum > third_sum : third_sum = working_sum
        if working_sum < first_sum and working_sum > second_sum : 
            placeholder_sum = second_sum 
            second_sum = working_sum
            if placeholder_sum > third_sum : thid_sum = placeholder_sum
        if working_sum >= first_sum : 
            placeholder_first = first_sum
            first_sum = working_sum
            if placeholder_first >= second_sum : 
                placeholder_second = second_sum
                second_sum = placeholder_first
                if placeholder_second > third_sum : third_sum = placeholder_second
        working_sum = 0

print(f"The sum of the top three is {first_sum + second_sum + third_sum}")