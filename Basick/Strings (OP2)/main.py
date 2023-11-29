
string_1 = "word1"
string_2 = 'word2'
print(string_1 + string_2) # har intet space immel. og derfor setter bare ordne sammen
print(string_1 + " " + string_2) #har "" som laver et space imellem ordne

number1 = 5
number2 = 3
print(number1 + number2)  # this works becose the nummberse are direktil plusing ithet other
print(str(number1) + " is greater than " + str(number2))  # this does not work becose you need to convert the int to sting before it can be ind a line with a string

#Udfør de næste celler en ad gangen. Før du udfører en celle, regn resultatet ud på forhånd. Når du får et uventet resultat,
#find ud af hvorfor. Leg gerne med cellerne. Forandre dem og udfør dem igen. Du kan også tilføje nye celler.
string1 = "hej"
print(string1) # prints hej. y

string1 += ", " # adds ", " to "hej"
print(string1) # prints "hej, ". y

string1 += string1 # adds "hej, " so it becomes "hej, hej, "
print(string1) # prints "hej, hej, ". Y

print(string1.upper()) # is "HEJ, HEj, ". N (i only thot it did the first letter)

print(string1.isupper()) # is false. N (forgot it dident atucelly change the string)

print(string1.replace("e", "ø")) # is "høj, høj, ". N (i only thot it did the first e)

print(string1.split("j")) # is ['he', ', he', ', ']. N (dident know it targetet all j.s and did not know it removed the j)

string2 = "software"
print("h" in string2) # prints "false". Y

print(len(string2)) # prints "8". Y

print(string2 + "\nNy linje!") # is "software" and on a new line "Ny linje!" N (i did not se the string2 at the beginig and only rote. prints "Ny linje!" på en ny line")

print(string2[0]) # prints "s". Y

print(string2[3]) # prints "t". Y

print(string2[-1]) # prints "e". Y

print(string2[-4]) # prints "w". Y

print(string2[2:]) # prints "ftware". Y

print(string2[2:6]) # is ftwa. N (i miss counted. and ansered prints "wa" )

# Skriv et program i den næste celle.
# Når man starter programmet, spørger den "How old are you?".
# Så kan man indtaste et tal.
# Derefter svarer programmet med "In ten years are you x years old." hvor x er det korrekte tal. (Tip: Muligvis har du brug for at google "type casting python".)
#print("How old are you?")
#user_age = int(input())
#print("In ten years are you " + str(user_age + 10) + " years old. \n")


city = "Copenhagen"
latitude = 56
print(f"{city} is located at {latitude} degrees latitude") # prints "Copenhagen is located at 56 degrees latitude". Y

print(f"{city[:3]} is located at {latitude} degrees latitude")  # prints "Cop located at 56 degrees latitude". Y

print(f"{city} is located {90 -latitude} degrees away from the north pole.") # prints "Copenhagen is located at 34 degrees latitude". N (did not see it was {90 -latitude})

print(f"{city} {latitude} {17*3}") # Copanhagen 56 51. Y

print(f"{city=} {latitude=} {17*3=}") # Copanhagen 56 51. Y

# Tilføj kode til de følgende celler, sådan at resultatet bliver den udtryk i kommentaren. Brug variablerne country, continent, population, area.
country = "Norway"
continent = "Europe"
population = 5400000
area = 385000  # square kilometers

print(f"{country} is part of {continent}") # Norway is part of Europe.

print(f"{country} has a population of {population}") # Norway has a population of 5400000.

# Calculate the correct value for x:
print(f"{country} has a population density of {(population / area):.2f} inhabitants per square kilomter. \n ")# Norway has a population density of x inhabitants per square kilomter.

# Udfør og den følgende celle og analyser hvad der sker.
# Forandre programmet sådan at den printer "number3<=number4" når det er sandt.
number3 = 25
number4 = 30
if number3 <= number4:
    print("number3<=number4")  # you can press tab or 4 spaces in order to indent a line

# Udfør den følgende celle og analyser hvad der sker.
# Forandre programmet sådan at en input større end 50 resulterer i output "input is 50 or larger"
number_input = int(input("type a number: "))

# does the same as the code under. but is more efesent and lesh code heavy
# it does this by not needing to check if it is smaller then X nummber. chose other ways the code above whood have bean called insted.
if number_input >= 50:
    print("input is 50 or larger")
elif number_input >= 19:
    print("input is between 18 and 50")
elif number_input > 12:
    print("input is between 12 and 19")
elif number_input > 2:
    print("input is between 2 and 13")
else:
    print("input is 2 or less")


if number_input > 2 and number_input < 13:
    print("input is between 2 and 13")
elif number_input > 12 and number_input < 19:
    print("input is between 12 and 19")
elif number_input >= 19 and number_input < 50:
    print("input is between 18 and 50")
elif number_input >= 50:
    print("input is 50 or larger")
else:
    print("input is 2 or less")

print("this gets always printed")
