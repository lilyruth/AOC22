
count = 3

f = open("Day6/day_6_input.txt", "r")
line = f.readlines()
stream = list(line[0])
num_characters = len(stream)
print('stream', stream)
while count < num_characters : 

    one = stream[count-3]
    two = stream[count-2]
    three = stream[count-1]
    four = stream[count]
    if one != two and one != three and one != four and two != three and two != four and three != four and count >= 4: 
        print(f"{count+1} chars need to be processed to get through the start-of-packet marker.")
        print(one, two, three, four)
        break
    else : count+=1
  

