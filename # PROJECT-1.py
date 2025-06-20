# PROJECT-1
# BUDGET TRACKER USING PYTHON
print("Enter your Income: ")
income = int(input())
# print(income)
print("Enter your current Expenditure: ")
expend = int(input())
# print(expend)
print("Select the following options: ")
print("- - - - - - - - - - - - - - - ")
print(" 1. Track Balance ")
print(" 2. Add Income ")
print(" 3. Add Expense ")
print(" 4. View Transactions ")
print(" 5. Exit ")
while(True):
    choice = int(input("Enter the choice: "))
    if choice == 1:
            curr_bal = income-expend
            print(f"Current Balance is: {curr_bal}") 
    elif choice == 2:
            print("Add Income with a specified amount:  ")
            add_inc = int(input()) 
            if add_inc>0:
                income += add_inc
                print(income)
            else:
                print("Income must be positive")
    elif choice == 3:
            print("Add your Expense: ")
            add_exp = int(input())
            print("Spent on: ")
            spent_on = input()
            if add_exp>0 and add_exp<=(income-expend): #To reduce overspending
                expend+=add_exp
                print(f"Updated Expense is: {expend}")
            elif add_exp<=0:
                print("Expense must be positive")
            else:
                print("Insufficient balance to add!")
                
    elif choice == 4:
            print("List of Transactions:  ")
            if choice == 2 and choice == 3: 
                print(f"Income : {income}")
                print(f"Expense: {expend}")
                print(f"Spent on: {spent_on}")
            else:
                print(f"Income: {income}")
                print(f"Expense: {expend}")
                print(f"Spent on: {spent_on}")
    elif choice == 5:
            print("Thank You! For choosing us!")
            break
    else:
        print("Invalid choice, please try again.")
    print("Enter (Y/N) to continue: ")
    ch = input()
    if ch.lower() == 'n':
        print("Exited...!")
        break      
