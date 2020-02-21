variable = input()
print(variable.lower().replace("!","").replace(",","").replace("?","").replace(".","").strip())














# To sum up, there is a list of priorities for all considered operations:
#
# parentheses ()
# power **
# unary minus - ()
# multiplication, division, and remainder * / %
# addition and subtraction + -
# from math import ceil
# # Read an integer:
# a = int(input())
# b = int(input())
# c = int(input())
# # Math
#
# classa=ceil(a/2)
# classb=ceil(b/2)
# classc=ceil(c/2)
# classall=(classa+classb+classc)
#
# print("%s" % classall)
#
# a=int(input())
# b=int(input())
# c=int(input())
# print((a//2)+(b//2)+(c//2)+(a%2)+(b%2)+(c%2))