def gen_func_geom():
    number = 1
    comm_denominator = 2
    while True:
        yield number
        number = number * comm_denominator


i = 0
print('Geometric progression:')
for item in gen_func_geom():
    print(item)
    i += 1
    if i == 20:
        break


# 2
def my_range_gen(lim: int):
    start = 0
    while start != lim:
        yield start
        start += 1


print('\nCustom range:')
for item in my_range_gen(10):
    print(item)

# 3

# def simple_nubmers(lim:int):
#
#
#
# print('\nPrime numbers in the given range:')
# for item in simple_nubmers(10):
#     print(item)


# 4
cube_list = []


def cube_gen(lim: int):
    start = 2
    while start < lim:
        cube = start ** 3
        cube_list.append(cube)
        start += 1
    yield cube_list


print('\nGeometric progression:')
for item in cube_gen(12):
    print(item)


# 5
def fibonachi_gen(lim: int):
    first, second = 1, 1
    while first <= lim:
        yield first
        first, second = second, first+second


print('\nFibonachi:')
for item in fibonachi_gen(144):
    print(item)



# 6            можливо тут треба використовувати якусь бібліотеку...
