"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


# def main():
#     """Display income report for incomes over a given number of months."""
#     incomes = []
#     months = int(input("How many months? "))
#
#     for month in range(1, months + 1):
#         income = float(input("Enter income for month " + str(month) + ": "))
#         incomes.append(income)
#
#     print("\nIncome Report\n-------------")
#     total = 0
#     for month in range(1, months + 1):
#         income = incomes[month - 1]
#         total += income
#         print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))
# Enter income for month 1: 120
# Enter income for month 2: 245.4
# Enter income for month 3: 900
# Enter income for month 4: 1205.56
# Enter income for month 5: 12.35
# Income Report
# -------------
# Month  1 - Income: $    120.00         Total: $    120.00
# Month  2 - Income: $    245.40         Total: $    365.40
# Month  3 - Income: $    900.00         Total: $   1265.40
# Month  4 - Income: $   1205.56         Total: $   2470.96
# Month  5 - Income: $     12.35         Total: $   2483.31

def get_monthly_income(month_number):
    return float(input(f"Enter income for month {month_number}: "))


def print_income_report(months, incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, months + 1):
        income = incomes[month - 1]
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


def main():
    """Display income report for incomes over a given number of months."""
    income_count = int(input("How many months? "))
    monthly_incomes = []

    for month in range(1, income_count + 1):
        income = get_monthly_income(month)
        monthly_incomes.append(income)

    print_income_report(income_count, monthly_incomes)


main()