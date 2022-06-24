import numpy as np


# Функции:
# Маркировка вершин по чётности (первая вершина 1, исходящие из неё 2, и т.д.)
def dfsWithMarking(node, num):
    numl = num
    array[node] = numl
    numl += 1
    for i in range(n):
        if matrix[i][node] == 1 and array[i] == 0:
            dfsWithMarking(i, numl)


# Нахождение паросочетаний алгоритмов Куна (ищем увеличивающую цепь)
def dfsForMatching(node):
    if used[node]:
        return False
    used[node] = True
    for i in range(n):
        if matrix[i][node] != 0 and (match[i] == -1 or dfsForMatching(match[i])):
            match[i] = node
            return True
    return False


# Тело программы:
# Получение матрицы:
n = int(input("Введите число вершин: "))
matrix = np.zeros((n, n), "int")

print("Введите матрицу:")
for i in range(n):
    matrix[i] = list(map(int, input().split()))

# Проверка на неориентированность и невзвешенность:
isUndirected = True
isUnweighted = True

for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            isUndirected = False
        if matrix[i][j] > 1 or matrix[i][j] < -1:
            isUnweighted = False

if not isUndirected:
    print("Граф не соответствует требованию: неориентированный")
    exit()
if not isUnweighted:
    print("Граф не соответствует требованию: невзвешенный")
    exit()

# Проверка на двудольность:
array = [0] * n
dfsWithMarking(0, 1)
isBipartite = True
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            if array[i] % 2 == array[j] % 2:
                isBipartite = False

if not isBipartite:
    print("Граф не соответствует требованию: двудольный")
    exit()

# Нахождение паросочетаний:
match = [-1] * n
for i in range(n):
    used = [False] * n
    dfsForMatching(i)
for i in range(n):
    if match[i] != -1:
        print(i + 1, " ", match[i] + 1)
