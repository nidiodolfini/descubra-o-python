# To sum up, there is a list of priorities for all considered operations:
#
# parentheses ()
# power **
# unary minus - ()
# multiplication, division, and remainder * / %
# addition and subtraction + -
duration_in_days = int(input())
food_per_day = int(input())
one_way_flight = int(input())
hotel_cost = int(input())

print((food_per_day * duration_in_days) + (hotel_cost * (duration_in_days - 1) + (one_way_flight * 2)))

