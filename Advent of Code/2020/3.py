from sys import stdin

def check_slope(map, slope_x, slope_y):
    trees = 0
    for i, value in enumerate(map[::slope_y]):
        if(value[(i * slope_x) % len(value)] == "#"):
            trees+=1
    return trees

def main():
    input_values = list()
    for line in stdin:
        input_values.append(line.replace("\n", ""))

    trees_3_1 = 0

    # --- Part one --- #
    trees_3_1 = check_slope(input_values, 3, 1)
    
    print(f"Part one: {trees_3_1}")

    # --- Part two --- #
    trees_1_1 = check_slope(input_values, 1, 1)
    trees_5_1 = check_slope(input_values, 5, 1)
    trees_7_1 = check_slope(input_values, 7, 1)
    trees_1_2 = check_slope(input_values, 1, 2)

    result = trees_1_1 * trees_1_2 * trees_3_1 * trees_5_1 * trees_7_1

    print(f"Part two: {result}")

if __name__ == "__main__":
    main()