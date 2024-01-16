# Напишите программу, которой на вход подается последовательность чисел через пробел, а также запрашивается у пользователя любое число.
# В качестве задания повышенного уровня сложности можете выполнить проверку соответствия указанному в условии ввода данных.
# Далее программа работает по следующему алгоритму:
#   Преобразование введённой последовательности в список
#   Сортировка списка по возрастанию элементов в нем (для реализации сортировки определите функцию)
#   Устанавливается номер позиции элемента, который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу.
#
# При установке позиции элемента воспользуйтесь алгоритмом двоичного поиска. Реализуйте его также отдельной функцией.

# Подсказка:
# Помните, что у вас есть числа, которые могут не соответствовать заданному условию. В этом случае необходимо вывести соответствующее сообщение.


def sort(array):
    for i in range(1, len(array)):
        x = array[i]
        idx = i
        while idx > 0 and array[idx - 1] > x:
            array[idx] = array[idx - 1]
            idx -= 1
        array[idx] = x
    return array

def binary_search1(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находим середину
    if array[middle] < element and array[middle+1] >= element:  # проверяем наше условие в середине
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search1(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search1(array, element, middle + 1, right)


input_OK = False
while not input_OK:
    input_Flag = 0
    arr_count = 0  # кол-во элементов в массиве
    array_str = input("Введите последовательность чисел через пробел : ").split()
    for i in array_str:
        arr_count += 1
        isd = i.isdigit()
        if isd == False:
            input_Flag = 1
    if input_Flag == 0:
        input_OK = True
    else:
        print("Ошибка ввода!")

input_OK = False
while not input_OK:
    m_str = input("Введите любое число: ")
    isd = m_str.isdigit()
    if isd == False:
        print("Ошибка ввода!")
    else:
        input_OK = True

array = list(map(int, array_str))
m = int(m_str)

sort(array)
print(array)

if m <= array[0] or m > array[-1]:
    print("Введенное число не соответствует условию задачи!")
else:
    print("Номер позиции элемента в последовательности,который меньше введенного числа, а следующий за ним больше или равен этому числу: ", binary_search1(array, m, 0, arr_count-1)+1)
