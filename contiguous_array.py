def contiguous_array(array):
    counter = 0
    result = 0
    if len(array) == 1:
        return array
    while counter < len(array):
        temp = []
        for num in array[counter:]:
            temp.append(num)
        temp_sum = sum(temp)
        if temp_sum > result:
            result = temp_sum
        counter += 1
    return result

print(contiguous_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
