

print("Addition: 2 + 2 = ",2+2)
print("Subtraction: 2 - 2 = ",2-2)
print("Multiplication: 2 * 2 = ",2*2)
print("Division: 2 / 2 = ",2/2)

def power2(x):
    return x**2

print("Power 2: 2**2 = ", power2(2))

def fact(x):
    if x <= 0:
        return 1
    else:
        return x*fact(x-1)
print("Factorial 2: 2*1 = ", fact(2))
print("This is Factorial!")