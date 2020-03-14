from functools import reduce
def red_f(x,y):
    return x * y
print(reduce(red_f, [x for x in range(100,1001,2)]))
