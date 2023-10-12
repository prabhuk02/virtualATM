import matplotlib.pyplot as plt
import numpy as np


print('Welcome to GROUP 16 ATM')
acc_nmbr = int(input('Enter your account number: '))

# FIRST USER

while acc_nmbr == 1234:

    print('''
            1.Account Balance
            2.Cash Withdrawl
            3.Change Pin
            4.Transfer Money
            5.Data analysis of withdrawl
            6.Exit
    ''')

    choice = int(input('Enter your choice: '))
    balance_1 = 20000.00
    account_pin = 2003
    
    if choice == 1:
        def balance_enquiry():
            Trials = 3
            while Trials != 0:
                pin = int(input('Enter your pin: '))
                if pin == account_pin:
                    print(f'Your account balance: {balance_1} INR')    #account_balance
                    break
                elif pin != account_pin:                    
                    Trials -= 1         
                    if Trials != 0 :
                        print('Incorrect Pin')           
                    elif Trials == 0:
                       print('   YOUR ACCOUNT IS BLOCKED   ')
                       print('   TRY AFTER 24HRS')
        balance_enquiry()   


    elif choice == 2:
        def cash_withdrawl():  
            print(f'Your current balance is : {balance_1}')    #cash_withdrawl
            amount = int(input('Enter the amount you need: '))
            pin = int(input('Enter your pin: '))
            
            if pin == account_pin:

                current_balance = balance_1 -amount
                if current_balance < 0:
                    print('Insufficient Balance')

                else:
                    current_balance = balance_1 -amount
                    print(f'Now you have sucessfully fetched your {amount} INR')
                    print(f'Current balance is : {current_balance}') 

            else:
                print('Incorrect pin')
        cash_withdrawl()
    

    elif choice == 3:    
        def pin_change():                   #change_pin
            print('To change your pin!')
            present_pin = int(input('Enter your present pin: '))
            

            if present_pin == account_pin:
                new_pin = int(input('Enter your new pin: '))
                new_pin_2 = int(input('Renter your new pin: '))
                if present_pin == new_pin:
                    print('Enter a different pin') 
                   
                elif new_pin == new_pin_2:
                    print('You have successfully changed your pin')
                else:
                    print('Enter the same pin, that you have entered previously.')
            else:
                print('You have entered your pin incorrectly')
        pin_change()

    

    elif choice == 4:                          #tranfer_money
        def tranfer_money():
            print('Transfering money!')
            transfer_acc_no = int(input("Enter the reciepient's acount number: "))  
            transfer_amount = int(input("Enter the amount you need to tranfer: "))
            pin = int(input('Enter your pin: '))
            if pin == account_pin:

                if transfer_amount > balance_1:
                    print('Insufficient balance')
                elif balance_1 >= transfer_amount:

                    print('You have succesfully tranfered money')
                    present_balance = balance_1 - transfer_amount
                    print(f'Now your present balance is : {present_balance} INR')    
                
            else:
                print('Invalid Pin!!')
                print('Please enter correct pin')
        tranfer_money()
        
    elif choice == 5:
        x = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'])
        y = np.array([10, 15, 12, 10, 13, 9, 8, 14, 18, 12, 11, 10])
        plt.xlabel("Months ( in a year )")
        plt.ylabel("Withdrawn amount ( in thousands )")
        pin = int(input('Enter your pin: '))
        if pin == account_pin:

            plt.bar(x,y, color = 'r', width = 0.5)
            plt.show()
            max = y[0]
            for number in y:
                if number > max:
                    max = number
            print(f'The most expensed amount is {max},000')
        
        else:
            print('Incorrect pin')
    elif choice == 6:
        break

    else:
        print('You have entered the number that is not in our range.')

else:
    print(f"We don't have {acc_nmbr} account details")

        # SECOND USER

while acc_nmbr == 4321:
    print('''
            1.Account Balance
            2.Cash Withdrawl
            3.Change Pin
            4.Transfer Money
            5.Data analysis of withdrawl
            6.Exit
    ''')

    choice = int(input('Enter your choice: '))
    balance_2 = 50000.00
    account_pin_2= 2222

    if choice == 1:
        def balance_enquiry():
            Trials = 3
            while Trials != 0:
                pin = int(input('Enter your pin: '))
                if pin == account_pin_2:
                    print(f'Your account balance: {balance_2} INR')    #account_balance
                    break
                elif pin != account_pin_2:                    
                    Trials -= 1         
                    if Trials != 0 :
                        print('Incorrect Pin')           
                    elif Trials == 0:
                       print('Account Blocked.Invalid pin')
                       print('Try after 24 hours')
        balance_enquiry()   

    elif choice == 2:
        def cash_withdrawl():
            print(f'Your current balance is : {balance_2}')    #cash_withdrawl
            amount = int(input('Enter the amount you need: '))
            pin = int(input('Enter your pin: '))
            
            if pin == account_pin_2:

                current_balance = balance_2 -amount
                if current_balance < 0:
                    print('low limit')

                else:
                    current_balance = balance_2 -amount
                    print(f'Now you have sucessfully fetched your {amount} INR')
                    print(f'Current balance is : {current_balance}') 

            else:
                print('Invalid pin')

        cash_withdrawl()
                
    
    elif choice == 3:    
        def pin_change():                   #change_pin
            print('To change your pin!')
            present_pin = int(input('Enter your present pin: '))
            if present_pin == account_pin_2:
                new_pin = int(input('Enter your new pin: '))
                new_pin_2 = int(input('Renter your new pin: '))
                if present_pin == new_pin:
                    print('Enter a different pin') 
                   
                elif new_pin == new_pin_2:
                    print('You have successfully changed your pin')
                else:
                    print('Enter the same pin, that you have entered previously.')
            else:
                print('You have entered your pin incorrectly')
        pin_change()
    

    elif choice == 4:                          #tranfer_money
        def tranfer_money():

            print('Transfering money!')
            transfer_acc_no = int(input("Enter the reciepient's acount number: "))  
            transfer_amount = int(input("Enter the amount you need to tranfer: "))
            pin = int(input('Enter your pin: '))
            if pin == account_pin_2:
                if transfer_amount > balance_2:
                    print('Insufficient balance')
                elif balance_2 >= transfer_amount:

                    print('You have succesfully tranfered money')
                    present_balance = balance_2 - transfer_amount
                    print(f'Now your present balance is : {present_balance} INR')    
                
            else:
                print('Invalid Pin!!')
                print('Please enter correct pin')
        tranfer_money()
    
    elif choice == 5:
        x = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'])
        y = np.array([13, 10, 12, 9, 13, 9, 8, 14, 17, 12, 11, 10])
        plt.xlabel("Months ( in a year )")
        plt.ylabel("Withdrawn amount ( in thousands )")
        pin = int(input('Enter you pin: '))
        if pin == account_pin_2:
          
          plt.bar(x,y, color = 'b', width = 0.4)
          plt.show()
          max = y[0]
          for number in y:
            if number > max:
              max = number
          print(f'The most expensed amount is {max},000 ')
        else:
          print('Incorrect pin')
        
    elif choice == 6:
        break

    else:
        print('You have entered the number that is not in our range.')
