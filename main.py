import math

what_to_calculate = input('What do you want to calculate?\n'
                          'type "n" for number of monthly payments,\n'
                          'type "a" for annuity monthly payment amount,\n'
                          'type "p" for loan principle:\n> ')

if what_to_calculate == 'n':
    loan_principal = int(input('Enter the loan principal:\n> '))
    monthly_payment = int(input('Enter the monthly payment:\n> '))
    loan_interest = float(input('Enter the loan interest:\n> '))
    i = loan_interest / 12 / 100
    formula = (monthly_payment / (monthly_payment - i * loan_principal))
    num_payments = math.ceil(math.log(formula, 1 + i))
    years = num_payments // 12
    months = num_payments % 12
    years_plural = True if years >= 2 else False
    months_plural = True if months >= 2 else False

    if years >= 1 and months >= 1:
        print(f"It will take {years} year{'s' * years_plural} and {months} "
              f"month{'s' * months_plural} to repay this loan!")
    elif years >= 1 and months < 1:
        print(f"It will take {years} year{'s' * years_plural} to repay this loan!")
    elif years < 1 and months > 0:
        print(f"It will take {months} month{'s' * months_plural} to repay this loan!")

elif what_to_calculate == 'a':
    loan_principal = int(input('Enter the loan principal:\n> '))
    number_of_months = int(input('Enter the number of periods:\n> '))
    loan_interest = input('Enter the loan interest:\n> ')
    i = float(loan_interest) / 12 / 100
    monthly_payment = loan_principal * ((i * math.pow(1 + i, number_of_months)) /
                                        (math.pow(1 + i, number_of_months) - 1))
    print(f"Your monthly payment = {math.ceil(monthly_payment)}")

elif what_to_calculate == 'p':
    annuity_payment = input('Enter the annuity payment:\n> ')
    number_of_months = int(input('Enter the number of periods:\n> '))
    loan_interest = input('Enter the loan interest:\n> ')
    i = float(loan_interest) / 12 / 100
    loan_principal = float(annuity_payment) / ((i * math.pow(1 + i, number_of_months)) /
                                               (math.pow(1 + i, number_of_months) - 1))
    print(f'Your loan principal = {math.floor(loan_principal)}!')
