def main():
    test_cases = int(input())
    for _ in range(test_cases):
        n = int(input())
        a_i = [int(num) for num in input().split()]
        b_i = list()
        d_i = list()

        a_i = [num for num in reversed(sorted(a_i))]
        
        right = True
        for i in range(n):
            if(a_i[i*2] != a_i[(i*2) + 1]):
                right = False
                break
            b_i.append(a_i[i*2])

        i = 1
        while(i < n and right):
            if(b_i[i-1] == b_i[i] or ((b_i[i-1] - b_i[i]) % (2 * (n-i))) != 0):
                right = False
                break
            d_i.append((b_i[i-1]-b_i[i]) / 2 / (n-i))
            i+=1

        i = 1
        while(i < n and right):
            b_i[n-1] -= (2 * i * d_i[i-1])
            i+=1

        if(not right):
            print('NO')
        else:
            if(b_i[n-1] <= 0 or b_i[n-1] % (2*n) != 0):
                print('NO')
            else:
                print('YES')

if __name__ == '__main__':
    main()