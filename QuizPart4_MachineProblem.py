#Machine Problem
print('\n[ Employee Salary Information ]')

employee = True
while employee:
    
    name = input('\nWhat is your name: ')

    rateperHour = float(input('\nWhat is your rate per Hour? '))
    hoursWorked = float(input('How many hours did you work this week? '))

    #formula for monthly salary
    salary = round(rateperHour * hoursWorked * 52 / 12, 2)
    
    loan = input('Do you have any loan? Y/N\n')
    if loan == 'Y':
        totalLoan = float(input('How much loan do you have?\n'))
    else:
        totalLoan = 0
        print('You have no loan.')
        
    #Pag-Ibig monthly compensation        
    if salary <= 1500:
        contribution = round(float(salary) * 0.01, 2)
    else:
        contribution = round(float(salary) * 0.02, 2)
        
    #Net taxable income    
    if salary > 500000:
        tax = float(salary) * 0.32 + 125000
    elif salary > 250000:
        tax = float(salary) * 0.30 + 50000
    elif salary > 140000:
        tax = float(salary) * 0.25 + 22500
    elif salary > 70000:
        tax = float(salary) * 0.20 + 8500
    elif salary > 30000:
        tax = float(salary) * 0.15 + 2500
    elif salary > 10000:
        tax = float(salary) * 0.10 + 500
    else:
        tax = float(salary) * 0.05
    
    #Overall Information    
    print ('\n==============================')
    print(f'Employee Name: {name}\nMonthly Salary: ${salary}\n\nINSURANCE:\nPAG-IBIG/SSS Contributions: ${contribution}\nLoan Deductions: ${totalLoan}\nTax: ${round(tax, 2)}')
    
    #Total Insurance 
    insurance = round(contribution + totalLoan + tax, 2)
    print ('------------------------------')
    print (f'Total Insurance Cost: ${insurance}')

    #Take Home Pay
    thPay = round(salary - insurance, 2)
    print ('\n==============================')
    print (f'Take Home Pay: ${thPay}')
    print ('==============================')

    new_employee = input ('\nAnother Employee? Y/N\n')
    
    if new_employee == 'Y':
        print ('\n========== NEW EMPLOYEE ==========')
        continue
    else:
        print ('Program terminated.')
        break
    



    
  