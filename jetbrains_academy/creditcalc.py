import math


def enter_value(some_list):
    return_list = []
    for value in some_list:
        print(value)
        return_list.append(float(input('> ')) if len(return_list) < 2 else (float(input('> ')) / 1200))
    return return_list


a_list = ['Enter credit principal:', 'Enter count of period:', 'Enter credit interest:']
n_list = ['Enter credit principal:', 'Enter monthly payment:', 'Enter credit interest:']
p_list = ['Enter monthly payment:', 'Enter count of period:', 'Enter credit interest:']
print('What do you want to calculate?\n'
      'type "n" - for count of months,\n'
      'type "a" - for annuity monthly payment,\n'
      'type "p" - for monthly payment:')
calculate_option = input('> ')

if calculate_option == 'p':
    monthly_payment, periods, interest = enter_value(p_list)
    pow_i_n = math.pow(1 + interest, periods)
    principal = math.floor(monthly_payment / ((interest * pow_i_n) / (pow_i_n - 1)))
    print(f'Your credit principal = {principal}')

if calculate_option == 'a':
    principal, periods, interest = enter_value(a_list)
    pow_i_n = math.pow(1 + interest, periods)
    annuity_payment = math.ceil(principal * ((interest * pow_i_n) / (pow_i_n - 1)))
    print(f'Your annuity payment = {annuity_payment}')

if calculate_option == 'n':
    principal, monthly_payment, interest = enter_value(n_list)
    month_count = math.ceil(math.log(monthly_payment / (monthly_payment - interest * principal), (1 + interest)))
    months = month_count % 12
    years = month_count // 12
    text = f'{months} month{"s" if months != 1 else ""} to replay the credit'
    if years > 0:
        text = f'{years} year{"s" if years != 1 else ""} and ' + text
    print(f'It takes ' + text)


# from math import log
#
# teste = 10 / (12 * 100)
# credit = 1000000
# mon = 15000
# print(log(1, teste + (15000 - teste) * credit))
# # print((mon - teste * credit) / 15000)
#
#
#
# # credit_principal = 0
# #
# #
# # def monthly_payment():
# #     teste = int(input('Enter monthly payment:\n'))
# #     pay = round(credit_principal / teste)
# #     if pay == 1:
# #         print(f'It takes {pay} month to repay the credit')
# #     else:
# #         print(f'It takes {pay} months to repay the credit')
# #
# #
# # def count_month():
# #     count = int(input('Enter count of months:\n'))
# #     month_payment = round((credit_principal / count) + 0.5)
# #     last_payment = month_payment - ((month_payment * count) - credit_principal)
# #     if credit_principal % count == 0:
# #         print(f'Your monthly payment = {month_payment}')
# #     else:
# #         print(f'Your monthly payment = {month_payment} with last month payment = {last_payment}.')
# #
# #
# # def calculate(type_calculate):
# #     if type_calculate.lower() == 'm':
# #         monthly_payment()
# #     elif type_calculate.lower() == 'p':
# #         count_month()
# #
# #
# # credit_principal = int(input('Credit principal: \n'))
# # print('What do you want to calculate?')
# # print('type "m" - for count of months,')
# # print('type "p" - for monthly payment:')
# # calculate(input())
#
#
# # write your code here
