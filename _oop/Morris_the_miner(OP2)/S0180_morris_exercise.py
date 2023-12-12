"""
Opgave "Morris the Miner":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Udgangssituation:
Morris har egenskaberne sleepiness, thirst, hunger, whisky, gold.
Alle attributter har startværdien 0.

Regler:
Hvis sleepiness, thirst eller hunger kommer over 100, dør Morris.
Morris kan ikke opbevare mere end 10 flasker whisky.
Ingen attribut kan gå under 0.

Ved hver omgang kan Morris udføre præcis én af disse aktiviteter:
sleep:      sleepiness-=10, thirst+=1,  hunger+=1,  whisky+=0, gold+=0
mine:       sleepiness+=5,  thirst+=5,  hunger+=5,  whisky+=0, gold+=5
eat:        sleepiness+=5,  thirst-=5,  hunger-=20, whisky+=0, gold-=2
buy_whisky: sleepiness+=5,  thirst+=1,  hunger+=1,  whisky+=1, gold-=1
drink:      sleepiness+=5,  thirst-=15, hunger-=1,  whisky-=1, gold+=0

Din opgave:
Skriv et program, der giver Morris så meget guld som muligt på 1000 omgange.

Hvis du ikke har nogen idé om hvordan du skal begynde, så åbn S0185_morris_help.py og start derfra.
Hvis du går i stå, så spørg google, de andre elever eller læreren (i denne rækkefølge).

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil.
"""

"""
Opgave "Morris The Miner" (denne gang objekt orienteret)

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Omskriv din oprindelige Morris-kode til en objektorienteret version.

Definer en klasse Miner med attributter som sleepiness, thirst osv.
og metoder som sleep, drink osv.
Opret Morris og initialiser hans attributter ved at kalde konstruktoren for Miner:
morris = Miner()

Hvis du går i stå, så spørg google, de andre elever eller læreren (i denne rækkefølge).

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil.
"""


class miner():

    def __init__(self, sleepiness, thirst, hunger, whisky, gold):
        self._sleepiness = sleepiness
        self._thirst = thirst
        self._hunger = hunger
        self._whisky = whisky
        self._gold = gold
        self.is_alive = True

    def __repr__(self):
        return f" (sleepiness:{self._sleepiness}) (thirst:{self._thirst}) (hunger:{self._hunger}) (whisky:{self._whisky}) (gold:{self._gold})"

    def what_to_do(self):

        if self._sleepiness >= 95:
            self._sleep()

        elif self._whisky >= 1:
            self._drink()

        elif self._thirst >= 90:
            self._buy_whisky()

        elif self._hunger >= 93:
            self._eat()

        else:
            self._mine()

        # checks if morris is daed
        if self._sleepiness >= 100 or self._thirst >= 100 or self._hunger >= 100 or self._whisky >= 10:
            self._miner_has_died()


    def _miner_has_died(self):
        print("[morris is dead]")
        self.is_alive = False

    def _sleep(self):
        self._sleepiness -= 10
        self._thirst += 1
        self._hunger += 1
        print("[morris has sleeped]")

    def _mine(self):
        self._sleepiness += 5
        self._thirst += 5
        self._hunger += 5
        self._gold += 5
        print("[morris has mined]")

    def _eat(self):
        self._sleepiness += 5
        self._thirst -= 5
        self._hunger -= 20
        self._gold -= 2
        print("[morris has eaten]")

    def _buy_whisky(self):
        self._sleepiness += 5
        self._thirst += 1
        self._hunger += 1
        self._whisky += 1
        self._gold -= 1
        print("[morris has bothe whisky]")

    def _drink(self):
        self._sleepiness += 5
        self._thirst -= 15
        self._hunger -= 1
        self._whisky -= 1
        print("[morris has drint]")


morris = miner(0, 0, 0, 0, 0)

turns = 0
while turns != 1000 and morris.is_alive:
    turns += 1
    print(f" it is trun {turns} {morris} ", end="")
    morris.what_to_do()



print("end total" + str(morris))
# gold = 1470
