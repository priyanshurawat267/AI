# Conditional Statements if, else, elif

print("Hello World")
x = int(input("Enter a age:"))
print("Your age is :", x)
print(x>=18)
print(x<=18)
print(x==18)
print(x!=18)
print(x>18)
print(x<18)
print(x>=18 and x<=18)
print(x>=18 or x<=18)
print(not(x>=18 and x<=18))
print(not(x>=18 or x<=18))  
print(x>=18 and x<=18 or x>=18 and x<=18)
print(x>=18 or x<=18 and x>=18 or x<=18)

if x>=18:
    print("You are eligible for voting")
else:
    print("You are not eligible for voting")
    print("hi")
print(str.capitalize("hello"))

# if, else

budget= 200
apple = 20
if (budget - apple > 50):
    print("You, add 1 kg apple")
else:
    print("You, not add 1 kg apple")

## if,elif, else

num = int(input("Enter a number :"))
if (num < 0):
    print("Number is Negative")
elif (num == 0):
    print("Number is Zero")
else:
    print("Number is Positibve")

## Nested if statement

n = int(input("Enter anumber :"))
if (n < 0):
    print("Number is negative ")
elif (n > 0):
    if (n <= 10):
        print("Number is beteween 1-10")
    elif(n > 10 and n <= 20):
        print("Number is between 11-20")
    else:
        print("Number is grather than 20")
else:
    print("Number is Zero")