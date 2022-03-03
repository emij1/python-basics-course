# Exercise 1

# Turn a normal equation into an algorithmic expression, to have python calculate the result.

# The example equation is shown in an image, which is not stored on this repository.

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

result = ((c + 5)*(b**2-3*a*c)*a**2)/(4*a)

print(f"The result is {result}")