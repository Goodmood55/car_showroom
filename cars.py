# sort() մեթոդի օգնությամ դասավորությունը լինմ է այբենական կարգով
'''cars = ['bmw', 'audi',  'toyota', 'subaru', ]
cars.sort()
print(cars)'''

# sort(reverse=True) հակառակ
'''cars = ['bmw', 'audi',  'toyota', 'subaru', ]
cars.sort(reverse=True)
print(cars)'''

# sorted() ժամանակաոր սոռտավորում։ Պահապնում է նախնական հաջորդականությունը
'''cars = ['bmw', 'audi',  'toyota', 'subaru' ]
print('Here is the original list:')
print(cars)

print("\nHere is the list of cars:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)'''
# sorted(reverse=True) այս կերպով նույն պես կարելի է սոռտավորել հակառակ այբենական կարգի ժամանակաորապես

# այս դեպքում ցուցակի երկարությունը len()
cars = ['bmw', 'audi',  'toyota', 'subaru' ]
print(len(cars))