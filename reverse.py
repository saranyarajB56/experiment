num = int(input("Enter a Number : "))
reversed_num = 0

while num > 0:
    last_digit = num % 10  # Get the last digit
    reversed_num = reversed_num * 10 + last_digit  # Append the digit to reversed_num
    num = num // 10  # Remove the last digit from the original number

print("Reverse of a number is:")
print(reversed_num)
