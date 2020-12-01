from sys import stdin

def check_vowel(string):
    n_vowels = 0
    n_vowels += string.count('a')
    n_vowels += string.count('e')
    n_vowels += string.count('i')
    n_vowels += string.count('o')
    n_vowels += string.count('u')
    return n_vowels

def check_repeat_letter(string, start_pos, space_betwwen, size):
    if(start_pos >= size-space_betwwen-1):
        return False
    if(string[start_pos] == string[start_pos+space_betwwen+1]):
        return string[start_pos]
    else:
        return check_repeat_letter(string, start_pos+1, space_betwwen, size)

def check_for_substring(string):
    if string.find('ab') != -1:
        return False
    if string.find('cd') != -1:
        return False
    if string.find('pq') != -1:
        return False
    if string.find('xy') != -1:
        return False
    else:
        return True

def main():
    input_strings = stdin.read().splitlines()
    valid_strings = 0
    

    ##----Part 1----##
    for string in input_strings:
        if(check_vowel(string) < 3):
            continue
        if not (check_repeat_letter(string, 0, 0, len(string))):
            continue
        if not (check_for_substring(string)):
            continue
        valid_strings += 1

    print(valid_strings)
    ##----Part 2----##
    valid_strings = 0
    for string in input_strings:
        if not (check_repeat_letter(string, 0, 1, len(string))):
            continue
        char = check_repeat_letter(string, 0, 0, len(string))
        if not(char):
            continue
        else:
            counter = string.count(char)
            if(((counter % 2) != 0) or counter == 2):
                continue
        print(string)
        valid_strings += 1

    print(valid_strings)

if __name__ == "__main__":
    main()