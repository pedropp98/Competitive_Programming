import sys

def check_vowels(word):
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for vowel in vowels:
        count += word.count(vowel)
    return True if (count >= 3) else (False)

def check_twice(word):
    for i in range(len(word)-1):
        if(word[i] == word[i+1]):
            return True
    return False

def check_contain(word):
    strings = ['ab', 'cd', 'pq', 'xy']
    for string in strings:
        if string in word:
            return False
    return True

def check_pair(word):
    for i in range(len(word)-1):
        pair = '{}{}'.format(word[i], word[i+1])
        if word.count(pair) > 1:
            return True
    return False

def check_repeat(word):
    for i in range(len(word)-2):
        if(word[i] == word[i+2]):
            return True
    return False

def main():
    count1 = 0
    count2 = 0
    for word in sys.stdin:
        word = word.replace('\n', '')
        if check_vowels(word) and check_twice(word) and check_contain(word):
            count1 += 1
        if check_pair(word) and check_repeat(word):
            count2 += 1
    print('Part one: {}'.format(count1))
    print('Part two: {}'.format(count2))

if __name__ == '__main__':
    main()