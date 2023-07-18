"""
    ---Task 1---
 Решить 6 задачу.
 Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
    * Таблицу создайте в виде однострочного генератора, где каждый элемент генератора — отдельный пример
      таблицы умножения.
    * Для вывода результата используйте «принт» без перехода на новую строку.
"""
table = [f"{j} x {i} = {i*j}" for i in range(2, 10) for j in range(2, 10)]

nested_list = [table[i:i+4] for i in range(0, len(table), 4)]

odd_el = []

for i in range(len(nested_list)):
    if i % 2 == 0:
        print(nested_list[i])
    else:
        odd_el.append(nested_list[i])
print()

for item in odd_el:
    print(item)

"""
table = [f"{j} x {i} = {i*j}" for i in range(2, 10) for j in range(2, 10)]

nested_list = [table[i:i+4] for i in range(0, len(table), 4)]

odd_el = [nested_list[i] for i in range(len(nested_list)) if i % 2 != 0]
even_el = [nested_list[i] for i in range(len(nested_list)) if i % 2 == 0]

for sublist in even_el:
    print(sublist)

print()

for sublist in odd_el:
    print(sublist)

"""