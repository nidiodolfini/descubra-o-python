import math
import sys
import argparse

args = sys.argv
values_positive = True


def diff(args):
    print('diff', args)


def annuity(principal_arg, periods_arg, interest_arg):
    principal = principal_arg
    periods = periods_arg
    interest = interest_arg
    pow_i_n = math.pow(1 + interest, periods)
    annuity_payment = math.ceil(principal * ((interest * pow_i_n) / (pow_i_n - 1)))
    print(f'Your annuity payment = {annuity_payment}')
    print(f'Overpayment = {(annuity_payment * periods) - principal}')


    print('annuity', args)


def check_positive(value):
    return_value = int(value)
    if return_value <= 0:
        global values_positive
        values_positive = False

    return return_value


def check_positive_float(value):
    return_value = float(value)
    if return_value <= 0:
        global values_positive
        values_positive = False
    return return_value


if len(args) == 5:
    ap = argparse.ArgumentParser()
    ap.add_argument("-t", "--type", required=True)
    ap.add_argument("-p", "--principal", type=check_positive)
    ap.add_argument("-i", "--interest", type=check_positive_float)
    ap.add_argument("-m", "--payment", type=check_positive)
    ap.add_argument("-mo", "--periods", type=check_positive)
    args = vars(ap.parse_args())
    # print(ap)
    # print(len(args))
    if values_positive and not (args['type'] == 'diff' and args['payment'] is not None) and args['interest'] is not None:
        if args['type'] == 'annuity':
            if args['periods'] is None:
                print('periods is None')
            else:
                print(args['principal'], args['periods'], args['interest'])
                # annuity(args['principal'], args['periods'], args['interest'])
        elif args['type'] == 'diff':
            diff(args)
        else:
            print('Incorrect parameters')
    else:
        print('Incorrect parameters')
else:
    print('Incorrect parameters')
