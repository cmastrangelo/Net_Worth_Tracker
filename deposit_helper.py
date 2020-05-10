from decimal import Decimal
import json

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

savings_to_purhcase = {
  "other investments": 600,
  "NAS": 55.56,
  "TV": 20
}

rent_and_bills = {
  []
}

amount_to_save = 2405.03

to_add_savings = {
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

to_add_to_purchase = {
  "other investments": 600,
  "NAS": 55.56,
  "TV": 20
}

to_add_rent_and_bills = {
    []
}

new_savings = {}
new_savings_to_purchase = {}
new_rent_and_bills = []
for saving in current_savings:
    new_savings[saving] = Decimal(str(current_savings[saving]))
for saving in to_add_savings:
    if saving in new_savings:
        new_savings[saving] += to_add_savings[saving]
    else:
        new_savings[saving] = to_add_savings[saving]
for saving in savings_to_purhcase:
    new_savings_to_purchase[saving] = Decimal(str(savings_to_purhcase[saving]))
for saving in to_add_to_purchase:
    if saving in new_savings_to_purchase:
        new_savings_to_purchase[saving] += to_add_to_purchase[saving]
    else:
        new_savings_to_purchase[saving] = to_add_to_purchase[saving]
for saving in rent_and_bills:
    new_rent_and_bills.append(saving)
for saving in to_add_rent_and_bills:
    new_rent_and_bills.append(saving)


total_current_savings = Decimal('0')
for saving in current_savings:
    total_current_savings += Decimal(str(current_savings[saving]))
for saving in savings_to_purhcase:
    total_current_savings += Decimal(str(savings_to_purhcase[saving]))
for saving in rent_and_bills:
    total_current_savings += Decimal(str(saving))


total_new_savings = Decimal('0')
for saving in new_savings:
    total_new_savings += Decimal(str(new_savings[saving]))
for saving in new_savings_to_purchase:
    total_new_savings += Decimal(str(new_savings_to_purchase[saving]))
for saving in new_rent_and_bills:
    total_new_savings += Decimal(str(saving))


total_difference = total_new_savings - total_current_savings
print('Total difference:', total_difference)

print('Missing to add in new savings:', Decimal(str(amount_to_save)) - total_difference, '\n\n')

print(new_savings)
