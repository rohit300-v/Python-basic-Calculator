print("Select your operation:")
operation = str(input("a = addition \nb = subtraction \nc = multiplication \nd = division \ninput: "))

def addition(x, y):
    z = x + y
    return z
def subtraction(x, y):
    z = x - y
    return z
def multiplication(x, y):
    z = x * y
    return z
def division(x, y):
    z = x / y
    return z

x = float(input("Enter your number x:"))
y = float(input("Enter your number y:"))

a = addition(x, y)
b = subtraction(x, y)
c = multiplication(x, y)
d = division(x, y)

if a:
    print(round(addition(x, y), 3))
elif b:
    print(round(subtraction(x, y), 3))
elif c:
    print(round(subtraction(x, y), 3))
else d:
    print(round(division(x, y), 3))
