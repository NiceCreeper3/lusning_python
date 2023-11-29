
def hello():
    print("hello world")


def type_something():
    user_input = input("click into the console window, then type something and press <return>:  ")
    print("You typed: " + user_input)

# Skriv et program i den næste celle, som kalder først funktionen hello og derefter funktionen type_something. Test det.
hello()
type_something()

# Korriger funktionen i den næste celle og test det med hjælp af den næstfølgende celle.
def multiply(number1, number2):  # multiplies number1 and number2
    return number1 * number2

# number1 og number2 i den sidste celle kalder man funktionens parametre.
# 5 og 4 i den næste celle kalder man argumenterne.
# Når man opkalder en funktion, får parametrene argumenternes værdier.
print(multiply(5, 4))

# I den næste celle, skriv en funktion med navnet "sign".
# Funktionen har en parameter "number" og returnerer teksten "positive", "null" eller "negative", afhængig af parameterens fortegn.
print()

def sign(number):
    if not number:
        return "null"
    elif number >= 0:
        return ("positive")
    else:
        return ("negative")

#parament_nummber = int(input())
#sign(parament_nummber)

# Udføre denne celle for at teste din funktion sign() i den forrige celle.
# Funktionen "check" opkalder din funktion "sign".
def check(test_number):
    print(test_number, "is", sign(test_number))

check(-6)
check(44)
check(0)


#Udfør den næste celle. Forstå fejlmeldinger. Udkommenter fejlagtige kodelinjer og udfør cellen igen.
print()

def add(number1, number2=0, number3=0):  # Adds 3 numbers. The second and third parameter is optional and has a default value.
    print(number1 + number2 + number3)

#add() #it does not have a defalt number ready four the first parameter. and there for gives error as it + with null

add(5)

add(3, 7)

add(3, 7, 6)

# add(2, 6, 8, 10)  the add funtuen only suports op to 3 parements. and tying to give more then the 3 will give error

# Kig på programmet i den næste celle. Hvad tror du, gør den? Udfør koden. Forandre koden og prøv igen. Leg med den.
print()

# its goving to fire the code. until i write a nummber bigger then 12
big_enough = False
while not big_enough:
    number = int(input("type a number"))
    big_enough = number > 12

# Forandre koden i den næste celle sådan at bare ulige tal udskrives.
numberlist = [7, 33, 2, 8]
for number in numberlist:
    if (number % 2) == 0:
        continue

    print(number)

print() # Forandre koden i den næste celle sådan at tallene 14, 18, 22, 26, 30 udskrives.

start = 10
stop = 25
step_size = 3
numberrange = range(start, stop, step_size)
for number in numberrange:
    step_size += 1 # got it to work but i don,t think this is what i was meant to do
    print(number + step_size)

print() # Forandre koden i den næste celle sådan at ved siden af hvert tal udskrives også dens kvadrattal.

# Import math Library
import math
print(math.sqrt(5)) # i misse understod what i was suposed to do. but now i have this :D

numberrange = range(5)
for number in numberrange:
    print(f" nummber {number} and its Square number is {number * number}")