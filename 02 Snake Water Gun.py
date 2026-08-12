import random
print("Inter your choice!")
print("snak = 0")
print("water = 1")
print("gun = -1")

while True:
    
    user = int(input("Enter user a number:"))
    computer = random.choice([1, 0, -1])
    print("computer choice:", computer)
    if user == 1 and computer == 1:
        print("Draw!")
    elif user == 1 and computer == 0:
        print("computer winn!")
    elif user == 1 and computer == -1:
        print("user winn!")
    elif user == 0 and computer == 0:
        print("Draw!")
    elif user == 0 and computer == 1:
        print("user winn!")
    elif user == 0 and computer == -1:
        print("computer winn!")
    elif user == -1 and computer == -1:
        print("Draw!")
    elif user == -1 and computer == 1:
        print("computer winn!")
    elif user == -1 and computer == 0:
        print("user winn!")
    else:
        print("Invalid Number!")
    






   
   
   