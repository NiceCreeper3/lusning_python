# [ Y = correckt ]  and  [ N = Incorreckt ]

# Udfør de næste celler en ad gangen. Før du udfører en celle, regn resultatet ud på forhånd.
# Når du får et uventet resultat, find ud af hvorfor. Leg gerne med cellerne. Forandre dem og udfør dem igen.
# Du kan også tilføje nye celler.
numbers = [5, -2, 4, 17]

print(type(numbers)) # prints "int". Y

print(len(numbers)) # print "4". Y

print(17 in numbers) # print "true". Y

print(2 in numbers) # print "false". Y

print(numbers[0]) # print "5". Y

print(numbers[3]) # print "17". y

print(numbers[-1]) # print "17". Y

print(numbers[:2]) # print "5, -2". Y

print(numbers[2:]) # print "4, 17". Y

print(numbers.append(9)) # is "None". N (i thot it wode only print the list with 9 ind id it. but not change the list)
# (also i whill not takes it as a misstake ind the otheres as that is a misstake that if i had know i wood have taken indto acount ind the otheres. so a Y now means the intenson was curreckt)

numbers.append(5)
print(numbers) # is "[5, -2, 4, 17, 9, 5]" . Y (my origanal was. print "5, -2, 4, 17, 5")

print(numbers[2:]) # is [4, 17, 9, 5] . Y (my origanal was. print "4, 17, 5")

print(len(numbers)) # is "6". Y. (my origanal was. print "5")

print(sorted(numbers)) # is [-2, 4, 5, 5, 9, 17]. Y (my origanal was. print "-2, 4, 5, 5, 17")

print(numbers) # is [5, -2, 4, 17, 9, 5]. Y (my origanal was. print "5, -2, 4, 17, 5")

numbers.sort()
print(numbers) # is [-2, 4, 5, 5, 9, 17]. Y (my origanal was. print "-2, 4, 5, 5, 17")

print(numbers) # is [-2, 4, 5, 5, 9, 17]. Y (my origanal was. print "-2, 4, 5, 5, 17")

# Tilføj kode til de følgende celler, sådan at resultatet bliver den udtryk i kommentaren.
print()

print(numbers[1]) # 4

print(numbers[-1]) #17

print(numbers[2:4]) # [5, 5]

print(numbers[3:]) # [5, 9, 17]

numbers += [3]
print(numbers) # [-2, 4, 5, 5, 9, 17, 3]

#Udfør de næste celler en ad gangen. Før du udfører en celle, regn resultatet ud på forhånd. Når du får et uventet resultat, find ud af hvorfor.
# Leg gerne med cellerne. Forandre dem og udfør dem igen. Du kan også tilføje nye celler.
print()

tuple_nummbers = (18, 22, 7)
print(tuple_nummbers) # print "(18, 22, 7)". Y

print(type(tuple_nummbers)) # prints "tuple class int". Y

print(len(tuple_nummbers)) # prints "3". Y

x1 = tuple_nummbers[0]
print(x1) # print "18" Y

print(22 in tuple_nummbers) # prints "true". Y

print(type(x1)) # prints "int". Y

x2 = tuple_nummbers[0:1]
print(x2) # print "(18)". Y

new_tuple = tuple_nummbers + tuple_nummbers
print(new_tuple) # print "(18, 22, 7, 18, 22, 7)". Y

# Udfør de næste celler en ad gangen. Før du udfører en celle, regn resultatet ud på forhånd. Når du får et uventet resultat, find ud af hvorfor.
# Leg gerne med cellerne. Forandre dem og udfør dem igen. Du kan også tilføje nye celler.
print()

house = {'street': 'broadway', 'number': 87}
print(house) # prints "{ 'street': 'broadway', 'number': 87}". Y

print(len(house)) # prints "2". Y

house['floors'] = 4
print(house) # prints "{ 'street': 'broadway', 'number': 87, 'floors': 4}". Y

print(house['street']) # prints "broadway". Y

print(len(house)) # prints "3". Y

print(house.keys()) # prints "{'street', 'number', 'floors'}". Y ()

print(house.values()) # prints "{'broadway', 87, 4}". Y ()

house.pop('number')
print(house)
