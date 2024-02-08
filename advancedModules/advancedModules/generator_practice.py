def create_cubes_list(n):
    cubes = []
    for x in range(n):
        result = x**3
        cubes.append(result)
    return cubes

print(create_cubes_list(5))


def create_cubes_gen(n):
    for x in range(n):
        yield x**3

for x in create_cubes_gen(5):
    print(x)


def gen_fib(n):
    a = 1
    b = 1
    for x in range(n):
        yield a
        a,b = b,a+b

print(list(gen_fib(5)))

for x in gen_fib(5):
    print(x)

fib = gen_fib(5)
print(next(fib))
print(next(fib))
print(next(fib))


s = 'Mike'
s = iter(s)
print(next(s))
print(next(s))
print(next(s))
