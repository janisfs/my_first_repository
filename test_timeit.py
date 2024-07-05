import timeit

a = list(range(10000))  # Большой список
b = list(range(5000, 15000))  # Другой большой список с частичным перекрытием

def method1():
    return [x for x in a if x in b]

def method2():
    return list(set(a).intersection(set(b)))

print("Метод 1 (списковое включение):", timeit.timeit(method1, number=100))
print("Метод 2 (множества):", timeit.timeit(method2, number=100))