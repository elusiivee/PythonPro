# 1
def generator(start, amount, rule):
    i = 0
    while i < amount:
        yield start
        start = rule(start)
        i += 1


def rule(n):
    return n * 2
    # return n**2               #чому квадрат не працює


funk = generator(1, 10, rule)

for element in funk:
    print(element)

# 2

# def fibonachi_gen(lim: int):
#     first, second = 1, 1
#     while first <= lim:
#         yield first
#         first, second = second, first+second
#
#
# print('\nFibonachi:')
# for item in fibonachi_gen(144):
#     print(item)


# 3
new_list = []


def list_gen(list,funk):
    return sum(funk(list))



print('\nList:')


def extra_funk(l):
    for i in l:
        new_list.append(i * 10)
    return new_list

print(list_gen([1,2,3,4,5,6],extra_funk))
