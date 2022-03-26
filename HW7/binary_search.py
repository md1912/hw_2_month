# num - список
# num1 - число которое нужно найти в списке по индексу
# Как я понял нужно список разделить на три это начало, середина, конец
# Искал в интернете так как были проблемы с пунктом выше
# А так логика очень простая и понятная - Урок усвоил.
def binary_search(num, num1):
    mid = 0
    low = 0
    high = len(num)-1
    step = 0

    while low <= high:
        print(f"Шаг {step}:\n {num[low:high + 1]}")
        step += 1
        mid = (low + high) // 2

        if num1 == num[mid]:
            return mid

        if num1 < num[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


num1 = 16
num = [1, 4, 6, 8, 9, 12, 16, 19, 23, 33, 41]
print(f"Поиск числа {num1}")
print(f"Индекс числа {num1}: {binary_search(num, num1)}")
