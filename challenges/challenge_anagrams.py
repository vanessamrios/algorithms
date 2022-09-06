def convert_string(string):
    chars = list()
    for char in string.upper():
        chars.append(ord(char))
    return chars

# https://en.wikipedia.org/wiki/List_of_Unicode_characters


def quick_sort(numbers, start, end):
    if start < end:
        p = partition(numbers, start, end)
        quick_sort(numbers, start, p - 1)
        quick_sort(numbers, p + 1, end)


def partition(numbers, start, end):
    pivot = numbers[end]
    delimit = start - 1

    for index in range(start, end):
        if numbers[index] <= pivot:
            delimit = delimit + 1
            numbers[index], numbers[delimit] = numbers[delimit], numbers[index]

    numbers[delimit + 1], numbers[end] = numbers[end], numbers[delimit + 1]

    return delimit + 1


def is_anagram(first_string, second_string):
    if (first_string == "" or second_string == ""):
        return False
    first_string_converted = convert_string(first_string)
    second_string_converted = convert_string(second_string)
    quick_sort(first_string_converted, 0, len(first_string_converted)-1)
    quick_sort(second_string_converted, 0, len(second_string_converted)-1)

    if (first_string_converted == second_string_converted):
        return True
    else:
        return False
