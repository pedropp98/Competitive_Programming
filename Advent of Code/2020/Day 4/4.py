from sys import stdin

def valid_by_size(variable, size):
    if(len(variable) == size):
        return True

def main():
    data_passport = list()
    passport = ""
    for line in stdin:
        passport += line.replace("\n", " ")
        if(line[0] == "\n"):
            data_passport.append(passport)
            passport = ""

    data_passport.append(passport)

    pass_credentials = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid")

    valid_passports = 0
    count_credentials = 0
    
    for this_passport in data_passport:
        count_credentials = 0
        for credential in pass_credentials:
            if(this_passport.count(credential) == 0):
                if(credential == "cid"):
                    count_credentials += 1
            else:
                count_credentials += 1
        if(count_credentials == len(pass_credentials)):
            valid_passports += 1

    print(f"Part one: {valid_passports}")

    valid_passports = 0

    valid_eye_color = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")

    for this_passport in data_passport:
        count_credentials = 0
        split_value = this_passport.split(" ")

        for i in range(len(split_value)):
            new_split = split_value[i].split(":")
            if(new_split[0] == pass_credentials[0]):    
                year = int(new_split[1])
                if(year >= 1920 and year <= 2002):
                    count_credentials += 1

            if(new_split[0] == pass_credentials[1]):
                year = int(new_split[1])
                if(year >= 2010 and year <= 2020):
                    count_credentials += 1

            if(new_split[0] == pass_credentials[2]):
                year = int(new_split[1])
                if(year >= 2020 and year <= 2030):
                    count_credentials += 1

            if(new_split[0] == pass_credentials[3]):
                measure = new_split[1][len(new_split[1])-2:]
                convert_to_int = new_split[1][:len(new_split[1])-2]
                if(convert_to_int != ""):
                    size = int(convert_to_int)
                    if(measure == "cm"):
                        if(size >= 150 and size <= 193):
                            count_credentials += 1
                    else:
                        if(size >= 59 and size <= 76):
                            count_credentials += 1

            if(new_split[0] == pass_credentials[4]):
                if(len(new_split[1]) == 7):
                    count_credentials += 1

            if(new_split[0] == pass_credentials[5]):
                if(new_split[1] in valid_eye_color):
                    count_credentials += 1
        
            if(new_split[0] == pass_credentials[6]):
                if(valid_by_size(new_split[1], 9)):
                    count_credentials += 1

        if(count_credentials == 7):
            valid_passports += 1

    print(f"Part two: {valid_passports}")
if __name__ == "__main__":
    main()