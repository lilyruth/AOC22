import math

monkeys = {
    '0': { 
        'items': [],
        'operation': '',
        'operation_number': 1,
        'divide_by': 1,
        'monkey_true': '',
        'monkey_false': '',
        'inspections': 0
        },
    '1': { 
        'items': [],
        'operation': '',
        'operation_number': 1,
        'divide_by': 1,
        'monkey_true': '',
        'monkey_false': '',
        'inspections': 0
        },
    '2': { 
        'items': [],
        'operation': '',
        'operation_number': 1,
        'divide_by': 1,
        'monkey_true': '',
        'monkey_false': '',
        'inspections': 0
        },
    '3': { 
        'items': [],
        'operation': '',
        'operation_number': 1,
        'divide_by': 1,
        'monkey_true': '',
        'monkey_false': '',
        'inspections': 0
        },
    '4': { 
        'items': [],
        'operation': '',
        'operation_number': 1,
        'divide_by': 1,
        'monkey_true': '',
        'monkey_false': '',
        'inspections': 0
        },
    '5': { 
        'items': [],
        'operation': '',
        'operation_number': 1,
        'divide_by': 1,
        'monkey_true': '',
        'monkey_false': '',
        'inspections': 0
        },
    '6': { 
        'items': [],
        'operation': '',
        'operation_number': 1,
        'divide_by': 1,
        'monkey_true': '',
        'monkey_false': '',
        'inspections': 0
        },
    '7': { 
        'items': [],
        'operation': '',
        'operation_number': 1,
        'divide_by': 1,
        'monkey_true': '',
        'monkey_false': '',
        'inspections': 0
        }
}

monkey_0 = 0
monkey_1 = 0
monkey_2 = 0
monkey_3 = 0

current_monkey = ''


def round():
    for monkey in monkeys: 
        while len(monkeys[monkey]['items']) > 0:
            new_item = monkeys[monkey]['items'].pop(-1)
            monkeys[monkey]['inspections'] += 1        
            if monkeys[monkey]['operation'] == '+':
                new_item = new_item + monkeys[monkey]['operation_number'] 
            elif monkeys[monkey]['operation_number'] == 'square':
                new_item = new_item * new_item
            else: new_item = new_item * monkeys[monkey]['operation_number']
            new_item = new_item % mod
            monkey_true = monkeys[monkey]['monkey_true']
            monkey_false = monkeys[monkey]['monkey_false']
            if new_item % monkeys[monkey]['divide_by'] == 0:
                monkeys[monkey_true]['items'].append(new_item)
            else: 
                monkeys[monkey_false]['items'].append(new_item)


f = open("Day11/day_11_input.txt", "r")
lines = f.readlines()
for line in lines: 

    line = line.rstrip('\n')
    line = line.lstrip()
    line = line.split(' ')

    if line[0] == 'Monkey':
        current_monkey = line[1][:-1]
    if line[0] == 'Starting':
        for item in line:
            if item[-1] == ',': 
                item = item[:-1]
                item = int(item)
                monkeys[current_monkey]['items'].append(item)
        last_int = line[-1]    
        last_int = int(last_int)
        monkeys[current_monkey]['items'].append(last_int)
    if line[0] == 'Operation:':
        monkeys[current_monkey]['operation'] = line[4]
        if line[5] != 'old': monkeys[current_monkey]['operation_number'] = int(line[5])
        else: monkeys[current_monkey]['operation_number'] = 'square'
    if line[0] == 'Test:':
        monkeys[current_monkey]['divide_by'] = int(line[3])
    if line[1] == 'true:':
        monkeys[current_monkey]['monkey_true'] = line[5]
    if line[1] == 'false:':
        monkeys[current_monkey]['monkey_false'] = line[5]

divisors = []
for monkey in monkeys:
    divisors.append(monkeys[monkey]['divide_by'])
print(divisors)
mod = math.prod(divisors)
count = 0

while count < 10000:
    print(f"Now on round {count}")
    round()
    count+= 1

inspections = []

for monkey in monkeys:
    inspections.append(monkeys[monkey]['inspections'])

print(inspections)
inspections.sort()
print(f"The level of monkey business is {inspections[-1] * inspections[-2]}")

# starting item worry level
# operation shows worry level changes during inspection
# worry level divided by three and rounded down
# test is where the monkey throws the item

# --> Each monkey goes through all of its items. Each monkey goes through all its items before going on to the next monkey. The entire process of all monkeys taking turns is a round.

## when a monkey throws an item it goes to the end of that monkey's list

