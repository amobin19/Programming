def duplicate(numbers_list):
    numbers_list.sort()
    if len(numbers_list) == 0:
        return "No values in list"
    elif len(numbers_list) == 1:
        return numbers_list[0]
    for i in range(1, len(numbers_list)):
        if numbers_list[i] == numbers_list[i - 1]:
            return numbers_list[i]


print(duplicate([9, 0, 2, 1, 0]))
