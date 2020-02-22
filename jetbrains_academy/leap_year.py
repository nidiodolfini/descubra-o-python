year = int(input())

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('Leap')
        else:
            print('Ordinary')
    else:
        print('Leap')
else:
    print('Ordinary')

# A year is considered leap if it is divisible by 4 and NOT divisible by 100,
# or if it is divisible by 400. So, 2000 is leap and 2100 isn't.
#
# 2017 is not a leap year
# 1900 is a not leap year
# 2012 is a leap year
# 2000 is a leap year