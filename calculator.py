try:  
    num = int(input("choose a number:"))    
    num2 = int(input("choose another number:"))
    operator = input("choose an operator:")        
    
        

    if operator =='+':   
        eval = num + num2
        print(f"{eval}")
    elif operator == '-':
        eval = num - num2
        print(f"{eval}")
    elif operator =='/':
        eval = num / num2 
        print(f"{eval}") 
    elif operator == '*':
        eval = num * num2
        print(f"{eval}")
except ValueError:
    print("Error")           
    
    
    
    