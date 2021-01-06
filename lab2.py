import numpy as np
 
import numpy.random
import sys
# ввод размеров матрицы n, m
# ввод элементов матрицы
# Вносим изменения в файл на ветке 2
# Вносим изменения в файл в скопированном репозитории
# # Автоматическое заполнение списка
def fill_list_auto():
    
    alist = np.random.randint(5, size=(2, 4))
    return alist
    
def fill_list():
        # Проверка вводимых данных на тип
    try:
        n, m = list(map(int, input().split()))
        alist = list(map(int, input().split()))
    except ValueError:
        print('Ошибка!')

    return alist, n, m

# поиск максимального значения среди средних значений строк матрицы

def find_max_average():
    print('Введите "1" для заполнения списка автоматически и "2" для ввода элементов с клавиатуры')
    num = int(input())
    if num == 1:
        arr = fill_list_auto()

    elif num == 2:
        alist, n, m = fill_list()
        arr = np.array(alist)
        arr.shape = (n, m)
    
    print(arr)
    print(max(np.mean(arr, axis=1)))


find_max_average()
