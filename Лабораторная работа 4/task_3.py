def delete(list_, index=None):
    ...  # TODO реализовать функцию удаления элемента из списка по индексу
    if index is not None:
        list_.pop(index)
    else:
        index = -1
        list_.pop(index)
    return list_


print(delete([0, 1, 2], index=0))  # [1, 2]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]