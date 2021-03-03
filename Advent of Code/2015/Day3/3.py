def dict_position(start_x, start_y):
    position = {
        'x': start_x,
        'y': start_y
    }
    return position

def create_visited_positions(dictionary):
    visited_positions = list()
    visited_positions.append([dictionary['x'], dictionary['y']])
    return visited_positions

def change_position(value, dictionary):
    if value == '^':
        dictionary['y'] += 1
    elif value == 'v':
        dictionary['y'] -= 1
    elif value == '>':
        dictionary['x'] += 1
    else:
        dictionary['x'] -= 1

def check_list(value, list_items, presents):
    if value not in list_items:
        list_items.append(value)
        presents[0] += 1

def part_one(input_data):
    santa = dict_position(0, 0)
    visited = create_visited_positions(santa)
    presents = [1]

    for value in input_data:
        change_position(value, santa)
        check_list([santa['x'], santa['y']], visited, presents)
    print('Part one: {}'.format(presents))

def part_two(input_data):
    santa = dict_position(0, 0)
    elf = dict_position(0, 0)
    visited = create_visited_positions(santa)
    presents = [1]
    for i in range(len(input_data)):
        if (i % 2 == 0):
            change_position(input_data[i], santa)
            check_list([santa['x'], santa['y']], visited, presents)
        else:
            change_position(input_data[i], elf)
            check_list([elf['x'], elf['y']], visited, presents)
        
    print('Part two: {}'.format(presents))

def main():
    input_data = input()
    part_one(input_data)
    part_two(input_data)

if __name__ == '__main__':
    main()