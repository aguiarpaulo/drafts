def func(*args):
    total = 1
    for num in args:
        total *= num
    print(total)
    return total

mult = func(1,2,3,4,5)

def func_2(num):
    if num %2==0:
        return print('par')
    return print('impar')

loc = func_2(7)