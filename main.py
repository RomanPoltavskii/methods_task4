import math
from scipy.optimize import minimize_scalar

def f(x):
    return math.cos(math.log(x))

def ddf(x):
    return -(math.cos(math.log(x)) - math.sin(math.log(x)))/x**2
a, b = 1, 3  # границы интервала
n = 100      # число интервалов (шагов сетки)

# вычисляем значение интеграла методом правых прямоугольников
def sol(f, a, b, n):
    sum_ = 0
    h = (b - a) / n
    x = a + h / 2

    for i in range(n):
        sum_ += f(x) * h
        x += h

    return sum_

def accuracy(ddf, a, b, n):
    max_ddf = minimize_scalar(lambda x: -abs(ddf(x)), bounds=(a, b), method='bounded')
    h = (b - a) / n
    return (((b - a)*h**2)/24)*round(abs(max_ddf.fun), 5)

res = sol(f,a,b,n)
# выводим результаты
print("Приближенное значение интеграла: ", res)
print(str(accuracy(ddf, a, b, n)))