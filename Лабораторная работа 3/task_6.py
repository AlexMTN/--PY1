list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение
max_index = 0
for index, num in enumerate(list_numbers):
    max_num = list_numbers[max_index]
    current_num = list_numbers[index]
    if current_num >= max_num:
        max_index = index
        max_num = current_num
list_numbers[-1], list_numbers[max_index] = list_numbers[max_index], list_numbers[-1]

print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
