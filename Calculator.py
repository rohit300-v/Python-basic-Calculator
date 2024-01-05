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

x = int(input("Enter your number a:"))
y = int(input("Enter your number b:"))

a = addition(x, y)
b = subtraction(x, y)
c = multiplication(x, y)
d = division(x, y)

if a:
    print(addition(x, y))
elif b:
    print(subtraction(x, y))
elif c:
    print(subtraction(x, y))
else:
    print(division(x, y))
