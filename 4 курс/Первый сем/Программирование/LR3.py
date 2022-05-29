import math
import timeit
import concurrent.futures as ftres
from functools import partial

def fun(x):
        f = 2 * math.sin(x) + math.cos(x*x) - 7
        return f

def integrate(f, a, b, n_iter=1000):
        dx = (b - a)/n_iter
        sum = 0.5 * (f(a) + f(b))
        for i in range(1, n_iter):
                sum += f(a + i * dx)
        
        return sum*dx

def integrate_async(f, a, b, *, n_jobs=2, n_iter=1000):
        executor = ftres.ThreadPoolExecutor(n_jobs)
        spawn = partial(executor.submit, integrate, f, n_iter=n_iter // n_jobs)
        step = (b - a) / n_jobs
        fs = [spawn(a + i * step, a + (i + 1) * step) for i in range(n_jobs)]
        return sum(f.result() for f in ftres.as_completed(fs))
    

print("Изначальная функция",timeit.timeit("integrate(fun, 1, 5)",globals=globals(),number=100))
print(integrate(fun, 1, 5))
print("Функция с 2 потоками",timeit.timeit("integrate_async(fun, 1, 5)",globals=globals(),number=100))
print(integrate_async(fun, 1, 5))
print("Функция с 4 потоками",timeit.timeit("integrate_async(fun, 1, 5,n_jobs=4)",globals=globals(),number=100))
print(integrate_async(fun, 1, 5,n_jobs=4))
print("Функция с 6 потоками",timeit.timeit("integrate_async(fun, 1, 5,n_jobs=6)",globals=globals(),number=100))
print(integrate_async(fun, 1, 5,n_jobs=6))
