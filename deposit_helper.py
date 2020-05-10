from decimal import Decimal
import json

current_savings = {
  "bills emergency": 1095.09,
  "stocks": 543.83,
  "crypto": 205,
  "vacation": 291.10,
  "laptop": 47.90,
  "tesla": 385.03,
  "tattoo": 189.60,
  "plastic surgery": 136.16,
  "laser hair removal": 32.40
}

savings_to_purhcase = {
  "other investments": 600,
  "NAS": 55.56,
  "TV": 20
}

rent_and_bills = []

amount_to_save = 1324.79

to_add_savings = {
  "bills emergency": 30,
  "stocks": 20,
  "crypto": 18,
  "vacation": 30,
  "laptop": 5,
  "tesla": 30,
  "tattoo": 7,
  "plastic surgery": 10,
  "laser hair removal": 0
}

to_add_to_purchase = {
  "other investments": 0,
  "NAS": 50,
  "TV": 350
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
