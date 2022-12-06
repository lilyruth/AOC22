dict = {}
count = 0

f = open("Day6/day_6_input.txt", "r")
line = f.readlines()
stream = list(line[0])
num_characters = len(stream)
print('stream', stream)
while count < num_characters : 
    char = stream[count]
    if char in dict : dict[char].append(count)
    else : dict[char] = [count]

    if count > 13 : 
        cut = count - 14
        for indecis in dict.values() : 
            if indecis.count(cut) : 
                indecis.remove(cut)
    check_for_deletion = ''
    for key in dict : 
        if len(dict[key]) == 0 : check_for_deletion = key
    if check_for_deletion != '' : 
        dict.pop(check_for_deletion, None)
    if len(dict) == 14 : 
       print(f"{count+1} chars need to be processed to get through the start-of-message marker.")
       break
    count+=1
 


  
