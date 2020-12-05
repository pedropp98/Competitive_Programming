from sys import stdin

def merge(array, begin, split, end):
    side_array = list()
    i = begin
    j = split+1
    k = 0
    while(i <= split and j <= end):
        if(array[i] < array[j]):
            side_array.append(array[i])
            i += 1
        else:
            side_array.append(array[j])
            j += 1

    while(i <= split):
        side_array.append(array[i])
        i += 1
    while(j <= end):
        side_array.append(array[j])
        j += 1

    i = begin
    while(i <= end):
        array[i] = side_array[k]
        k += 1
        i += 1

def mergesort(array, begin, end):
    if(end <= begin):
        return
    split = int(begin + ((end - begin) / 2))

    mergesort(array, begin, split)
    mergesort(array, split+1, end)

    merge(array, begin, split, end)
    return

def main():
    seat_id = list()

    # --- Part one --- #
    for line in stdin:
        rows = [0, 127]
        column = [0, 7]
        for i in range(7):
            if(line[i] == "F"):
                rows[1] = int((rows[0] + rows[1]) / 2)
            else:
                rows[0] = int(((rows[0] + rows[1]) / 2) + 1)

        for i in range(3):
            if(line[i+7] == "L"):
                column[1] = int((column[0] + column[1]) / 2)
            else:
                column[0] = int(((column[0] + column[1]) / 2) + 1)

        seat_id.append((rows[0] * 8) + column[0])

    mergesort(seat_id, 0, len(seat_id)-1)
    print(f"Part one: {seat_id}")

    # --- Part two --- #
    for i in range(len(seat_id)-1):
        if(seat_id[i] != seat_id[i+1]-1):
            print(f"Part two: {seat_id[i]+1}")
            break

if __name__ == "__main__":
    main()