def lucky_in_decimal(num, lucky_number):
    while num > 0:
        if(num % 10 == lucky_number):
            return True
        num = int(num / 10)
    return False

def lucky_in_sum(num, lucky_number):
    subtract = num - lucky_number
    if(subtract < lucky_number):
        return False
    if(lucky_in_decimal(subtract, lucky_number)):
        return True
    else:
        return lucky_in_sum(subtract, lucky_number)

def main():
    test_cases = int(input())
    for _ in range(test_cases):
        input_d_and_q = input().split()
        input_a_n = input().split()
        for a_n in input_a_n:
            if(lucky_in_decimal(int(a_n), int(input_d_and_q[1]))):
                print('YES')
            elif(lucky_in_sum(int(a_n), int(input_d_and_q[1]))):
                print('YES')
            else:
                print('NO')

if __name__ == '__main__':
    main()