#name = input("What is your name? ")
#age = input("How old are you? ")

#print(name)
#print(int(age))


#age = int(input("Enter your age"))
#print("You'll be", age+5, " years old in the next five years")
try:
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
except:
    print("invalid input")
    exit()
print("sum:", first_number+second_number)
print("Difference:", first_number-second_number)
print("Product:", first_number*second_number)
if second_number > 0:
    print("Quotient:", first_number/second_number)
else:
    print("cannot be divided by zero")

