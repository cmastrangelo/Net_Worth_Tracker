from decimal import Decimal
import json

current_savings = {
    "bills emergency": 1033.11,
    "stocks": 585.83,
    "crypto": 236.0,
    "vacation": 343.1,
    "laptop": 62.9,
    "tesla": 450.03,
    "tattoo": 216.6,
    "plastic surgery": 166.16,
}

savings_to_purhcase = {
    "other investments": 350.0,
    "TV": 420.0
}

rent_and_bills = [774.79]

amount_to_save = 32.4

to_add_savings = {
  "bills emergency": 0,
  "stocks": 4,
  "crypto": 3,
  "vacation": 2,
  "laptop": 1,
  "tesla": 7.4,
  "tattoo": 10,
  "plastic surgery": 5,
}

to_add_to_purchase = {
  "other investments": 0,
  "TV": 0
}

to_add_rent_and_bills = []

new_savings = {}
new_savings_to_purchase = {}
new_rent_and_bills = []
for saving in current_savings:
    new_savings[saving] = Decimal(str(current_savings[saving]))
for saving in to_add_savings:
    if saving in new_savings:
        new_savings[saving] += Decimal(str(to_add_savings[saving]))
    else:
        new_savings[saving] = Decimal(str(to_add_savings[saving]))
for saving in savings_to_purhcase:
    new_savings_to_purchase[saving] = Decimal(str(savings_to_purhcase[saving]))
for saving in to_add_to_purchase:
    if saving in new_savings_to_purchase:
        new_savings_to_purchase[saving] += Decimal(str(to_add_to_purchase[saving]))
    else:
        new_savings_to_purchase[saving] = Decimal(str(to_add_to_purchase[saving]))
for saving in rent_and_bills:
    new_rent_and_bills.append(Decimal(str(saving)))
for saving in to_add_rent_and_bills:
    new_rent_and_bills.append(Decimal(str(saving)))


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


# Prepare for Json dumping (Cannot have Decimal classes

for saving in new_savings:
    new_savings[saving] = float(new_savings[saving])

for saving in new_savings_to_purchase:
    new_savings_to_purchase[saving] = float(new_savings_to_purchase[saving])

for idx, saving in enumerate(new_rent_and_bills):
    new_rent_and_bills[idx] = float(saving)

print(json.dumps(new_savings, indent=4))
print('\n', json.dumps(new_savings_to_purchase, indent=4))
print('\n', new_rent_and_bills)
