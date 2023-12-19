"""
Opgave "Animals"

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Alt, hvad du har brug for at vide for at løse denne opgave, finder du i cars_oop-filerne.

Definer en klasse ved navn Animal.
Hvert objekt i denne klasse skal have attributterne name (str), sound (str), height (float),
weight (float), legs (int), female (bool).
I parentes står data typerne, dette attributterne typisk har.

Tilføj til klassen meningsfulde metoder __init__ og __repr__.
Kald disse metoder for at oprette objekter af klassen Animal og for at udskrive dem i hovedprogrammet.

Skriv en klassemetode ved navn make_noise, som udskriver dyrets lyd i konsollen.
Kald denne metode i hovedprogrammet.

Definer en anden klasse Dog, som arver fra Animal.
Hvert objekt af denne klasse skal have attributterne tail_length (int eller float)
og hunts_sheep (typisk bool).



Tilføj til klassen meningsfulde metoder __init__ og __repr__.
Ved skrivning af konstruktoren for Dog skal du forsøge at genbruge kode fra klassen Animal.
Kald disse metoder for at oprette objekter af klassen Hund og for at udskrive dem i hovedprogrammet.

Kald metoden make_noise på Dog-objekter i hovedprogrammet.

Skriv en klassemetode ved navn wag_tail for Dog.
Denne metode udskriver i konsollen noget i stil med
"Hunden Snoopy vifter med sin 32 cm lange hale"
Kald denne metode i hovedprogrammet.

Skriv en funktion mate(mother, father). Begge parametre er af typen Dog.
Denne funktion skal returnere et nyt objekt af typen Dog.
I denne funktion skal du lave meningsfulde regler for den nye hunds attributter.
Hvis du har lyst, brug random numbers så mate() producerer tilfældige hunde.
Sørg for, at denne funktion kun accepterer hunde med det korrekte køn som argumenter.

I hovedprogrammet kalder du denne metode og udskriver den nye hund.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""

import random


class Animal:
    def __init__(self, name, sound, height, weight, legs, female):
        self._name = str(name)
        self._sound = str(sound)
        self._height = float(height)
        self._weight = float(weight)
        self._legs = int(legs)
        self._female = bool(female)

    def __repr__(self):
        return f"the animals name is {self._name}. its {self._height} cm tall and weighs {self._weight} kg. it has {self._legs} legs. is female is {self._female}"

    def is_female(self):
        return self._female

    def make_noise(self):
        print(self._sound)


class Dog(Animal):

    def __init__(self, name, sound="woof", height=110, weight=110, legs=4, female=False, tail_lenght=10, hunts_sheep=False):
        super().__init__(name, sound, height, weight, legs, female)
        self._tail_lenght = tail_lenght
        self._hunts_sheep = bool(hunts_sheep)

    def __repr__(self):
        return f"the dogs name is {self._name}. its {self._height} cm tall and weighs {self._weight} kg. it has {self._legs} legs. is female is {self._female}, and if it hunts sheep is {self._hunts_sheep}"

    def wag_tail(self):
        print(f"Hunden {self._name} vifter med sin {self._tail_lenght} cm lange hale")

    def mate(self, mate, pup_name):

        # uses is_female to check if the to mate is a diffrent gender then the slef.Dog
        if mate.is_female() != self._female:
            mate_dna = mate.return_dna() # makes a list of the mates atrabuts. i do this as the atrubuts are private

            pup = Dog(pup_name, self._inheret_from(self._sound, mate_dna[1]), 110, 100, 4, self._inheret_from(self._female, mate_dna[5]), random.randint(8, 16), self._inheret_from(self._hunts_sheep, mate_dna[7]))
            return pup

        return "the to dogs can not mate"

    # takes to data and returns one of them at random. this is meant to represnt the random chanse of with parent to inheret from
    def _inheret_from(self, dog1, dog2):

        if random.randint(0, 1): # makes a random roll ind betvine 1 and 0, and sinse 0 = False. this is a radom number of False and True
            return dog2

        return dog1

    # is a method that returns the adtrebuts og the dog
    def return_dna(self):
        return [self._name, self._sound, self._height, self._weight, self._legs, self._female, self._tail_lenght, self._hunts_sheep]


# makes multepol objeckts
platapus = Animal("Parry", "hghghgghghghghghg", 106, 116, 4, False)

fluffels = Dog("Fluffels", "woof", 110, 110, 4, False, 16, True)
sasha = Dog("sasha", "bhejff", 100, 95, 4, True, 14, True)
steve = Dog("steve", "berrf", 90, 100, 3, False, 5, False)

# prints platapus stats
print(platapus)
platapus.make_noise()


# trys to make 3 pup objeckts using the mate method. and then prints the pup stats
print()
pup1 = sasha.mate(fluffels, "Fluffer")
pup2 = fluffels.mate(steve, "brom")
pup3 = sasha.mate(steve, "flower")
print(f"{pup1} \n{pup2} \n{pup3}")

print()
pup1.make_noise()
pup3.wag_tail()