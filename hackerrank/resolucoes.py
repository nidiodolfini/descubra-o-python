def solve(meal_cost, tip_percent, tax_percent):
    meal_cost += ((meal_cost * tip_percent) / 100) + ((meal_cost * tax_percent) / 100)
    return round(meal_cost)

print(solve(12.0, 20, 8))