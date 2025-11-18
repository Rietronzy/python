balance = 500
pin = 6867
pin = input("Enter your pin  ")

if pin == 6867:
    print("PIN accepted! Access granted")
    print("* ATM Menu *\n1.Check balance\n2.Deposit Money\n3.Withdraw Money\n4.Exit") 
    ch = int(input("Enter Your Choice (1-4):")) 
if ch == 1: 
    print(f"Your balance is {balance}") 
    print("* ATM Menu *\n1.Check balance\n2.Deposit Money\n3.Withdraw Money\n4.Exit") 
ch = int(input("Enter Your Choice (1-4):"))    
if ch == 2:
    deposit = int(input("Enter the amount you want to deposit: ")) 
    eval = deposit + balance
    print(f"Your new balance is {eval}") 
    print("* ATM Menu *\n1.Check balance\n2.Deposit Money\n3.Withdraw Money\n4.Exit") 
ch = int(input("Enter Your Choice (1-4):")) 
if ch == 3:
        withdraw = int(input("Enter the amount to withdraw: "))
        eval = {eval} - withdraw
        print(f"Your new balance is {eval}")