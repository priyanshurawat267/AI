x = int(input("Enter a number :"))
match x:
    case 0:
        print("the value is zero")
    case 2:
        print("the value is two")
    case 0:
         print("the value is Negative")      
    case _ if x!=90:
          print(x, "is not 90")

          print("No match any value")   
    #case _ :
          print(x)


        