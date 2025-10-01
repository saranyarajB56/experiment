# Recursion
# factorial of a number

def rec_factorial(n):
    if n == 1:
        return n
    else: 
        return n*rec_factorial(n-1)
    
n = int(input("Enter a Number : "))
if n < 0:
 print("sorry!factorial does not exist for negative numbers")
elif n==0:
 print("The factorial of 0 is 1")
else:
 print("The factorial of",n,"is",rec_factorial(n))

