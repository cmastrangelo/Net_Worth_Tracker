from decimal import Decimal
import json

current_savings = {
    "bills emergency": 1180.11,
    "stocks": 570.83,
    "crypto": 226.0,
    "vacation": 326.1,
    "laptop": 57.9,
    "tesla": 430.03,
    "tattoo": 201.6,
    "plastic surgery": 151.16,
    "laser hair removal": 32.4
}

savings_to_purhcase = {
    "other investments": 350.0,
    "TV": 420.0
}

rent_and_bills = []

amount_to_save = 974.79

to_add_savings = {
  "bills emergency": 53,
  "stocks": 15,
  "crypto": 10,
  "vacation": 17,
  "laptop": 5,
  "tesla": 20,
  "tattoo": 15,
  "plastic surgery": 15,
  "laser hair removal": 0
}

to_add_to_purchase = {
  "other investments": 0,
  "TV": 50
}

to_add_rent_and_bills = [774.79]

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
