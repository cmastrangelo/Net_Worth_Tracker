from decimal import Decimal

current_savings = {
  "permanent savings": 160.09,
  "bills emergency": 35,
  "other investments": 0,
  "stocks": 343.83,
  "crypto": 105,
  "vacation": 141.10,
  "laptop": 42.90,
  "tesla": 185.00,
  "tattoo": 89.60,
  "plastic surgery": 36.16,
  "laser hair removal": 32.40
}

amount_to_save = 2405.03

to_add = {
  "permanent savings": 300,
  "bills emergency": 600,
  "other investments": 600,
  "stocks": 200,
  "crypto": 100,
  "vacation": 150,
  "laptop": 5,
  "tesla": 200.03,
  "tattoo": 100,
  "plastic surgery": 100,
  "laser hair removal": 0,
}

new_savings = {}
for saving in current_savings:
    new_savings[saving] = Decimal(str(current_savings[saving])) + Decimal(str(to_add[saving]))

total_current_savings = Decimal('0')
for saving in current_savings:
    total_current_savings += Decimal(str(current_savings[saving]))
total_new_savings = Decimal('0')
for saving in new_savings:
    total_new_savings += Decimal(str(new_savings[saving]))

total_difference = total_new_savings - total_current_savings
print('Total difference:', total_difference)

print('Missing to add in new savings:', Decimal(str(amount_to_save)) - total_difference, '\n\n')

print(new_savings)
