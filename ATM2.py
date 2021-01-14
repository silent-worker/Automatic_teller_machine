print('WELCOME TO ATM')
restart=('Y')
chances=3
balance=999.12
while chances>=0:
    pin = int(input('Please enter your 4 digit pin:'))
    if pin==(4567):
        print('you entered your pin correctly')
        print('Please Press 1 For Your Balance Enquiry')
        print('Please Press 2 To Make a Withdrawl')
        print('Please Press 3 To Pay in')
        print('Please Press 4 To Return Card\n')
        while restart not in ('n','NO','no','N'):
            print('Please Press 1 For Your Balance Enquiry')
            print('Please Press 2 To Make a withdrawl')
            print('Please Press 3 To Pay in')
            print('Please Press 4 To Return Card')
            option = int(input('What would you like to choose?: '))
            if option == 1:
                print('Your Balance is $', balance)
                restart = input('Would You like to go back? ')
                if restart in ('n','No','no','N'):
                    print('Thank You')
                    break
                elif option == 2:
                    option = ('y')
                    withdrawl = int(input('How Much Would You Like To Withdrawa? 10,20,30,40,50,100 for other enter 1:'))
                    if withdrawl in [10,20,30,40,50,100]:
                        balance = balance-withdrwal
                        print('\nYour Balance is Now $',balance)
                        restart = input('Would You Like To Go Back?')
                    if restart in ('n','No','no','N'):
                        print('Thank You')
                        break
                    elif withdrwal != [10,20,30,40,50,100]:
                        print('Invalid Amount,Please Re-try\n')
                        restart = ('Y')
                    elif withdrawl ==1:
                            withdrawl = float(input('Please Enter Desired amount:'))

                elif option ==3:
                        pay_in = float(input('How Much Would You like to pay in?'))
                        balance = balance + pay_in
                        print('\n Your Balance is now $',balance)
                        restart = input('Would You Like to go back?')
                        if restart in ('n','NO','no','N'):
                            print('Thank You')
                            break
                        elif option == 4:
                            print('Please wait whilst your card is returned.....\n')
                            print('Thank you for your service')
                            break
                        else:
                            print('Please Enter a correct number.\n')
                            restart =('Y')
    elif pin !=('4567'):
            print('Incorrect Password')
            chances = chances-1
            if chances == 0:
                print('\n No more tries')
                break
                                

                                    
                                