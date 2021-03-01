def main():
    data = input()
    print('Part one: {}'.format(data.count('(') - data.count(')')))
    count = 0
    for i in range(len(data)):
        if data[i] == '(':
            count += 1
        if data[i] == ')':
            count -= 1
        if count < 0:
            print('Part two: {}'. format(i+1))
            break

if __name__ == '__main__':
    main()