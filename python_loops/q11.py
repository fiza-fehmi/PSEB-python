# Q11. Simple ATM
# Start with balance = 10000 and an empty list history = []. Use while True with the options
# Deposit, Withdraw, Check balance and Exit.
# Don’t allow a withdrawal bigger than the balance; print “Insufficient balance”
# Save every deposit and withdrawal in history
# On Exit, print the whole history, then break

# deposit =int(input("Enter amount you want to deposit"))
# deposited_amount = 10000+deposit
# withdraw = int(input("Enter the amount you want to withdraw"))
list_history =[]
saved_balance =10000
while True:
    print("1. Depsosit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice =input("Enter your choice: ")
    if choice=="1":
        deposit =int(input("Enter amount you want to deposit: "))
        saved_balance = saved_balance+deposit
        list_history.append(f"Deposited Amount: {deposit}")
    elif choice=="2":
        withdraw = int(input("Enter the amount you want to withdraw: "))
        if withdraw>saved_balance:
            print("Insufficient Balance")
            break
        else :
            saved_balance = saved_balance-withdraw
            print(f"Amount recieved to your account 03********96 of {withdraw}")
            list_history.append(f"Withdraw Amount: {withdraw}")
    elif choice=="3":
        print(f"Remaining Balance: {saved_balance}")
        # list_history.append()
    elif choice=="4":
        print('Transaction History:')
        print(list_history)
        break





        


