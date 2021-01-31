def main():
    test_cases = int(input())
    for _ in range(test_cases):
        _ = int(input())
        a_n = [int(num) for num in input().split()]
        counter = [[x, a_n.count(x)] for x in set(a_n)]
        bigger = counter[0][0]
        for item in counter:
            if(item[1] > bigger):
                bigger = item[1]
            print(item)
        # print(bigger)

if __name__ == '__main__':
    main()