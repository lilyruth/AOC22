import re

output = []
curr_dir = ""
breadcrumbs = []
file_tree = { "home": [] }
count = 1

f = open("Day7/day_7_input.txt", "r")
lines = f.readlines()
for line in lines: 
    output.append(line.rstrip('\n'))
for line in output:
    if line== "$ cd /":
        curr_dir = "home"
        breadcrumbs = ["home"]
    elif line == "$ cd ..":
        breadcrumbs.pop(-1)
        curr_dir = breadcrumbs[-1]
    else: 
        split_line = line.split(' ')
        if split_line[1] == "cd":
            prefix = ''
            for item in breadcrumbs:
                prefix += item
                prefix += "_"
            prefix += split_line[2]
            print(prefix)
            curr_dir = prefix
            breadcrumbs.append(curr_dir)
            file_tree[curr_dir] = []
        elif split_line[0] == "dir":
            prefix = ''
            for item in breadcrumbs:
                prefix += item
                prefix += "_"
            prefix += split_line[1]
            file_tree[curr_dir].append(prefix)
        elif split_line[1] != "ls":
            print(split_line)
            file_tree[curr_dir].append(int(split_line[0]))

print(file_tree)
for item in file_tree:
    print(f"{item} includes {file_tree[item]}")


dir_sizes = {}

for item in file_tree:
    contents = file_tree[item][:]
    sizes = []
    while len(contents) > 0:
        contents_item = contents.pop(-1)
        if isinstance(contents_item, str):
            nested_contents = file_tree[contents_item][:]
            for nested_item in nested_contents:
                contents.append(nested_item)
        else: sizes.append(contents_item)
    dir_sizes[item] = sizes[:]

dir_totals = {}

min_total = 0
for item in dir_sizes:
    dir_sum = sum(dir_sizes[item])
    dir_totals[item] = dir_sum
    if dir_sum <= 100000:
        min_total += dir_sum


space_available = 70000000 - dir_totals["home"]
print('space available', space_available)
space_needed = 30000000 - space_available
print('space needed', space_needed)

dir_available_for_deletion = []

for item in dir_totals:
    if dir_totals[item] >= space_needed:
        print(dir_totals[item])
        dir_available_for_deletion.append(dir_totals[item])
dir_available_for_deletion.sort()
print(dir_available_for_deletion[0])