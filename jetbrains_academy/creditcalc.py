credit_principal = 0


def monthly_payment():
    teste = int(input('Enter monthly payment:\n'))
    pay = round(credit_principal / teste)
    if pay == 1:
        print(f'It takes {pay} month to repay the credit')
    else:
        print(f'It takes {pay} months to repay the credit')


def count_month():
    count = int(input('Enter count of months:\n'))
    month_payment = round((credit_principal / count) + 0.5)
    last_payment = month_payment - ((month_payment * count) - credit_principal)
    if credit_principal % count == 0:
        print(f'Your monthly payment = {month_payment}')
    else:
        print(f'Your monthly payment = {month_payment} with last month payment = {last_payment}.')


def calculate(type_calculate):
    if type_calculate.lower() == 'm':
        monthly_payment()
    elif type_calculate.lower() == 'p':
        count_month()


credit_principal = int(input('Credit principal: \n'))
print('What do you want to calculate?')
print('type "m" - for count of months,')
print('type "p" - for monthly payment:')
calculate(input())


# write your code here
