'''НT7.1. 1. Запишіть в один рядок генератор списку (числа в діапазоні
від 0 до 100 не включно), кожен елемент якого буде ділитись без остачі
на 5 але не буде ділитись на 3.
   Результат: [5, 10, 20, 25, 35, 40, 50, 55, 65, 70, 80, 85, 95].'''

result = [x for x in range(100) if x % 5 == 0 and x % 3 != 0]
matrix = result = [x for x in range(1, 7)]
print(result)
print(matrix)
print(result[1235])