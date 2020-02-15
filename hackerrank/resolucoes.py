def swap_case(s):
    a = ''
    for let in s:
        if let.isupper():
            a += let.lower()
        else:
            a += let.upper()
    return a


print(swap_case('HackerRank.com presents "Pythonist 2".'))