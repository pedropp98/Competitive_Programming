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

def search(array, number):
    length = len(array)
    i = 0
    while i <= length:
        if(array[i] + array[length-1] == number):
            return array[i], array[length-1]
        elif(array[i] + array[length-1] < number):
            i += 1
        else:
            length -= 1
    return -1, -1

def main():
    input_values = list()
    for line in stdin:
        input_values.append(int(line.replace("\n", "")))
    mergesort(input_values, 0, len(input_values)-1)
    result_numbers = search(input_values, 2020)
    print(f"First: {result_numbers[0] * result_numbers[1]}")
    i = 0
    for i in input_values:
        result_numbers = search(input_values, 2020 - i)
        if(result_numbers[0] != -1):
            break
    print(f"Second: {i * result_numbers[0] * result_numbers[1]}")

if __name__ == "__main__":
    main()