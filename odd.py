try:
    num = int(input("Enter a number: "))   
    if num %2==0:
        print("Even number")
    else:
        print("Odd number") 
except ValueError:
    print("error:Wrong data type")      
       
