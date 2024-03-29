"""Opgave "Turtle Hunt":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Spillet:
    Denne øvelse er et spil for 2 spillere.
    3 skildpadder (jægere) forsøger at fange en anden skildpadde (bytte) så hurtigt som muligt.
    Den ene spiller styrer byttet, den anden spiller styrer jægerne. Derefter bytter spillerne roller.
    I hver tur bestemmer spillerne, hvor mange grader deres skildpadde(r) roterer. Dette er spillerens eneste opgave.
    Byttet får et point for hver tur, før det bliver fanget.
    Hvis byttet stadig er på flugt efter MAX_TURNS omgange, fordobles pointene, og jagten slutter.


Koden til spillet er allerede skrevet i S1530_turtle_hunt_main.py og S1520_turtle_hunt_service.py. Du må ikke ændre disse filer.

Din opgave er at få skildpadderne til at rotere smartere.

Kopier alle 3 turtle_hunt-filer til din egen løsningsmappe.
Skriv din løsning ind i din kopi af S1510_turtle_hunt_classes_constants.py.

Filstruktur:
    Koden er opdelt i 3 filer for at gøre det klart, hvilken del af koden
    du skal ændre, og hvilken del af koden du skal lade være uændret.

    S1530_turtle_hunt_main.py:
        Dette er hovedprogrammet.
        Du må ikke foretage ændringer heri.
        Kør det for at starte spillet.

    S1520_turtle_hunt_service.py:
        Indeholder nogle servicefunktioner, som vil være nyttige for dig.
        Du må ikke foretage ændringer heri.

    Denne fil (S1510_turtle_hunt_classes_constants.py):
        Alt din programmering til denne øvelse foregår i denne fil.

Delopgaver:
Trin 1:
    Kig på programkoden.
    Du behøver ikke at forstå alle detaljer i hovedprogrammet.
    Forstå, hvordan de tre filer importerer hinandens kode med "import".
    Forstå, hvornår og hvordan metoderne rotate_prey() og rotate_hunt() bruges.
    Fra nu af foregår al din programmering til denne øvelse i denne fil her.

Trin 2:
    Ændr navnet på klassen PlayerName1 i den første linje i dens klassedefinition til dit personlige klasses navn.
    Nederst i denne fil skal du sætte variablerne class1 og class2 til dit personlige klasses navn.

Trin 3:
    I din personlige klasse skal du gøre metoderne rotate_prey og rotate_hunter smartere.
    Eventuelt vil du også tilføje nogle attributter og/eller metoder til din klasse.
    Du må dog ikke manipulere (f.eks. flytte) skildpadderne med din kode.
    Køretiden for dine metoder rotate_prey og rotate_hunter skal være mindre end 0,1 sekunder pr. iteration.

Trin 4:
    Find en sparringspartner i din studiegruppe.
    Som med alt andet skal du bede din lærer om hjælp, hvis det er nødvendigt.
    I din kode skal du erstatte hele klassen PlayerName2 med din sparringspartners klasse.
    Nederst i denne fil indstiller du variablen class2 til din sparringpartners klasses navn.
    Lad de 2 klasser kæmpe og lær af resultaterne for at forbedre din kode.
    Gentag dette trin indtil du er tilfreds :-)

Trin 5:
    Når dit program er færdigt, skal du skubbe det til dit github-repository.
    Send derefter denne Teams-besked til din lærer: <filename> done
    Derefter fortsætter du med den næste fil.

Senere:
    Når alle er færdige med denne øvelse, afholder vi en turnering
    for at finde ud af, hvem der har programmeret de klogeste skildpadder :)

Kun hvis du er nysgerrig og elsker detaljer:
    Her er den fulde dokumentation for skildpaddegrafikken:
    https://docs.python.org/3.3/library/turtle.html"""
import math
import turtle  # this imports a library called "turtle". A library is (someone else's) python code, that you can use in your own program.
import random
from S1520_turtle_hunt_service import distance, direction  # inports the distance and direction from the sevice script

prey_degree_min = -5
prey_degree_max = 1
prey_comfurt_distance = 100
round_to_new_degree = 2


class Alexander(turtle.Turtle):

    # ploymores the init of turtel to incklude orientation
    def __init__(self):
        super().__init__()  # Here, this is equivalent to turtle.Turtle.__init__(self)
        self.orientation = 0  # used to keep track of the turtle's current orientation (the direction it is heading)
        self._Previse_oritason = 0

    def rotate_prey(self, positions):  # turtle will be turned right <degree> degrees. Use negative values for left turns.
        # self: the turtle that shall be rotated
        # positions: a list of tuples. Each tuple is a pair of coordinates (x,y).
        # positions[0] is the coordinate tuple of the prey. positions[0][0] is the x-coordinate of the prey.
        # positions[1], positions[2], positions[3] refer to the hunters.
        # for example is positions[3][1] the y-coordinate of the third hunter.
        # i
        # short hand positions[who] [return x or y] 0 = X and 1 = Y

        # Example for use of the service functions distance() and direction
        # print(f'{distance(positions[0], positions[1])=}   {direction(positions[0], positions[1])=}')  # print distance and direction from prey to hunter1

        degree = random.randint(prey_degree_min, prey_degree_max)

        # checks if a hunter is nere. and if it is then prey move ind the opesid deregson of hunter
        for hunt in positions[1:]:
            if distance(positions[0], hunt) <= prey_comfurt_distance:
                degree -= direction(hunt, positions[0])
                break  # brackes the for loop so as not to move ind to many direcsens

        print(f"[{degree}:degree]   [{math.trunc(degree)}:int degree]")

        self.orientation += degree  # adds the degree to orientation
        self.orientation %= 360  # makes orientation + degree a diregsen. aka a orientation
        # print(self.orientation)
        return degree

    def rotate_hunter(self, positions):  # turtle will be turned right <degree> degrees. Use negative values for left turns.
        # Example for use of the service functions distance() and direction
        # print(f'{distance(self.position(), positions[0])=}   {direction(self.position(), positions[0])=}')  # print distance and direction from the current hunter to the prey

        direction_to_prey = direction(self.position(), positions[0])

        # get it so it reamberes previes oriantason and the does mathe to acount four the new posin. and does not just spin
        degree = 0

        # get it so it reamberes previes oriantason and the does mathe to acount four the new posin. and does not just spin
        if 0 <= self._Previse_oritason:
            degree = direction_to_prey - self._Previse_oritason
        elif 0 > self._Previse_oritason:
            degree = direction_to_prey + self._Previse_oritason

        print()
        print(f"\n direction [{direction_to_prey}]"
              f"\n previes direction [{self._Previse_oritason}]"
              f"\n degree [{degree}]")

        # degree = -0.5  # When the turtle rotates the same amount each turn,  it will just run in a circle. Make this function smarter!
        self.orientation += degree
        self.orientation %= 360
        self._Previse_oritason = direction_to_prey
        # print(self.orientation)
        return degree


class Uli_1(turtle.Turtle):

    def __init__(self):
        super().__init__()  # Here, this is equivalent to turtle.Turtle.__init__(self)
        self.orientation = 0  # used to keep track of the turtle's current orientation (the direction it is heading)

    def rotate_prey(self, positions):  # turtle will be turned right <degree> degrees. Use negative values for left turns.
        hunter_distance = 99999
        for hunter in [1, 2, 3]:
            if distance(positions[0], positions[hunter]) < hunter_distance:
                hunter_distance = distance(positions[0], positions[hunter])
                closest_hunter = hunter
        new_prey_direction = direction(positions[closest_hunter], positions[0])  # direction from closest hunter to prey
        degree = new_prey_direction - self.orientation
        self.orientation += degree
        self.orientation %= 360
        return degree

    def rotate_hunter(self, positions):  # turtle will be turned right <degree> degrees. Use negative values for left turns.
        prey_direction = direction(self.position(), positions[0])  # direction from current hunter to prey
        degree = prey_direction - self.orientation
        self.orientation += degree
        self.orientation %= 360
        return degree


# change these global constants only for debugging purposes:
MAX_TURNS = 200       # Maximum number of turns in a hunt.                           In competition: probably 200.
ROUNDS = 1            # Each player plays the prey this often.                       In competition: probably 10.
STEP_SIZE = 3         # Distance each turtle moves in one turn.                      In competition: probably 3.
SPEED = 0             # Fastest: 10, slowest: 1, max speed: 0.                       In competition: probably 0.
CAUGHT_DISTANCE = 10  # Hunt is over, when a hunter is nearer to the prey than that. In competition: probably 10.


random.seed(2)  # use seed() if you want reproducible random numbers for debugging purposes. You may change the argument of seed().


class1 = Alexander  # (red prey) Replace PlayerName1 by your own class name here.
class2 = Uli_1  # (green prey) For testing your code, replace PlayerName1 by your own class name here. Later replace this by your sparring partner's class name.