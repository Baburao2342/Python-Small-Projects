import math

def factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        return ValueError("Input cannot be less than 0.")
    else:
        return n * factorial(n-1)

def nCr(n, r):
    if r > n:
        raise ValueError(f"r < n not allowed. r:{r}, n:{n}")
    else:
        return factorial(n) / (factorial(r) * factorial(n-r))

def nPr(n, r):
    return nCr(n, r) * factorial(r)

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multiply(a, b):
    return a * b

def division():
    a = int(input("Enter number to divide: "))
    b = int(input("Enter number to divide by: "))

    if b == 0:
        raise ValueError("You cannot divide by zero!")
    else:
        return (a / b)

def sin(a):
    return math.sin(a)

def cos(a):
    return math.cos(a)

def tan(s):
    return math.tan(s)


print('''
Welcome to the Sigma Calculator! We calculate stuff here!
Choose your operation, input the value and BOOM! Get the result!      
''')

print('''
Alrighty! Choose your operation!
      1. Addition
      2. Subtraction
      3. Multiplication
      4. Division
      5. Combination
      6. Permutation
      7. Factorial
      8. sin()
      9. cos()
      10. tan()

''')

choice = int(input("Enter your choice: "))

for i in range(5, 50):
    print('Boobs niggers!')

choice_dict = {
    1: add,
    2: sub,
    3: multiply,
    4: division,
    5: nCr,
    6: nPr,
    7: factorial,
    8: sin,
    9: cos,
    10: tan
}

if choice in choice_dict.keys():
   if choice in [1, 2, 3, 4, 5, 6]:
       if choice == 4:
           try:
               ans = division()
               print(f"Answer = {ans}")
           except ValueError as e:
               print(f"Error: {e}")
               
       else:
           a = int(input('Enter first number: '))
           b = int(input('Enter second number: '))
           ans = choice_dict[choice](a, b)
           print(f"Answer = {ans}")
   elif choice in [7, 8, 9, 10]:
       a = int(input("Enter input: ")) 
       ans = choice_dict[choice](a)
       print(f"Answer = {ans}")

