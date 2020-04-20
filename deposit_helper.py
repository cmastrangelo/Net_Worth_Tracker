from decimal import Decimal

current_savings = {
  "permanent savings": 140.09,
  "bills emergency": 25,
  "other investments": 0,
  "stocks": 286.83,
  "crypto": 55,
  "vacation": 121.10,
  "laptop": 32.90,
  "tesla": 154.99,
  "tattoo": 69.60,
  "plastic surgery": 16.16,
  "laser hair removal": 32.40,
  "NAS": 10
}

amount_to_save = 252.56

to_add = {
  "permanent savings": 20,
  "bills emergency": 10,
  "other investments": 0,
  "stocks": 57,
  "crypto": 50,
  "vacation": 20,
  "laptop": 10,
  "tesla": 30,
  "tattoo": 20,
  "plastic surgery": 20,
  "laser hair removal": 0,
  "NAS": 15.56
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