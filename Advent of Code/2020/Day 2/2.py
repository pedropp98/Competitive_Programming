from sys import stdin

def main():
    valid_passP1 = 0
    valid_passP2 = 0
    
    for line in stdin:
        line = line.split("-")
        minimum = int(line[0])
        line = line[1].split(" ")
        maximum = int(line[0])
        character = line[1].split(":")[0]
        password = line[2].split("\n")[0]

        # --- Part one --- #
        q = password.count(character)
        if(q >= minimum and q <= maximum):
            valid_passP1 += 1
        # -- Part two --- #
        if((password[minimum-1] == character) and (not password[maximum-1] == character)):
            valid_passP2 += 1
        elif((not password[minimum-1] == character) and (password[maximum-1] == character)):
            valid_passP2 += 1


    print(f"Part one: {valid_passP1}")
    print(f"Part two: {valid_passP2}")


if __name__ == "__main__":
    main()