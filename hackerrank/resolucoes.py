def is_leap(year):
    leap = False
    resto = year % 4
    resto100 = year % 100
    resto400 = year % 400

    if not resto:
        if not resto400:
            leap = True
        elif resto100:
            leap =  True

    return leap
is_leap(2000)