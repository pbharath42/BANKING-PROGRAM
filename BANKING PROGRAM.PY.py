def show_balance():
    print(f"your balance is ${balance:.2f}")
def  deposit():
    amount = float(input("Enter an amount to be deposited: "))
    
     
    if amount < 0:
        print("that's not a valid account")
        
    else:
        return amount                   

def withdraw():
    amount= float(input("Enter amount to be withdrawn: "))
    
    if amount > balance:
        print("insufficient funds")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0" )
            
        return 0 
    else:
        return amount        

balance = 0
is_running = True

while is_running:
    print("Banking program")
    print("1.show balance")
    print("2.deposit")
    print("3.withdraw")
    print("4.Exit")
    
    choice = input("enter your choice (1-4):")
    if choice=='1':
        show_balance()    
    elif choice == '2':
        balance += deposit()
    elif choice == '3':
        balance -= withdraw()
    elif choice == '4':
        is_running=False
    else:
        print("that is not a valid choice")
        
print("Thank you!have a nice day")                           
    