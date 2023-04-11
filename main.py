import math

def f(x):
    return math.cos(math.log(x))

a, b = 1, 3  # границы интервала
n = 1000      # число интервалов (шагов сетки)
dx = (b - a) / n  # шаг сетки

# вычисляем значение интеграла методом правых прямоугольников
integral = 0
for i in range(n):
    xi = a + i*dx
    fi = f(xi + dx)
    integral += fi*dx

# вычисляем абсолютную и относительную погрешности
I_exact = 1.51811  # точное значение интеграла
I_approx = integral  # приближенное значение интеграла
Delta_I_abs = abs(I_exact - I_approx)
Delta_I_rel = Delta_I_abs / abs(I_exact)

# выводим результаты
print("Приближенное значение интеграла: ", I_approx)
print("Абсолютная погрешность: ", Delta_I_abs)
print("Относительная погрешность: ", Delta_I_rel)