import math

def f(x):
    return math.cos(math.log(x))

a, b = 1, 3  # границы интервала
n = 1000      # число интервалов (шагов сетки)

# вычисляем значение интеграла методом правых прямоугольников
def left_rectangular_integration(f, a, b, n):
    h = (b - a) / n
    I = 0

    for i in range(n):
        x = a + i * h
        I += f(x)

    return h * I

res = left_rectangular_integration(f,a,b,n)
# выводим результаты
print("Приближенное значение интеграла: ", res)
