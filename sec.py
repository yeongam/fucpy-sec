
def calculate(x, y):
    total = x + y
    print("In Function")
    print("a:", a, "b:", b, "a+b:", a+b, "total:", total)
    return total

a = 5
b = 7
total = 0
print("In Program")
print("a:", a, "b:", b, "a+b:", a+b, "total:", total)

sum = calculate(a, b)
print("After calculation")
print("total:", total, "sum:", sum)