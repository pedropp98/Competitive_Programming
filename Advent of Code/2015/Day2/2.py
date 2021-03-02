def ribbon(l, w, h):
    return l * w * h

def smallest(n1, n2, n3):
    if n1 <= n2 and n1 <= n3:
        return n1
    elif n2 <= n1 and n2 <= n3:
        return n2
    else:
        return n3


def smallest_perimeter(l, w, h):
    perimeter1 = 2 * l + 2 * w
    perimeter2 = 2 * w + 2 * h
    perimeter3 = 2 * l + 2 * h
    return smallest(perimeter1, perimeter2, perimeter3)

def wrapping_paper(l, w, h):
    return ((2 * l * w) + (2 * w * h) + (2 * h * l))

def slack(l, w, h):
    area1 = l * w
    area2 = w * h
    area3 = l * h
    return smallest(area1, area2, area3)

def main():
    total1 = 0
    total2 = 0
    try:
        while True:
            length, width, height = input().split('x')
            total1 += wrapping_paper(int(length), int(width), int(height)) + slack(int(length), int(width), int(height))
            total2 += smallest_perimeter(int(length), int(width), int(height)) + ribbon(int(length), int(width), int(height))
    except EOFError:
        pass
    print('Part one: {}'.format(total1))
    print('Part two: {}'.format(total2))

if __name__ == '__main__':
    main()