"""Opgave: Objektorienteret rollespil, del 1 :

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Definer en klasse "Character" med attributterne "name", "max_health", "_current_health", "attackpower".
_current_health skal være en protected attribut, det er ikke meningen at den skal kunne ændres udefra i klassen.

Tilføj en konstruktor (__init__), der accepterer klassens attributter som parametre.
Tilføj en metode til udskrivning af klasseobjekter (__repr__).

Tilføj en metode "hit", som reducerer _current_health af en anden karakter med attackpower.
Eksempel: _current_health=80 og attackpower=10: et hit reducerer _current_health til 70.

Metoden hit må ikke ændre den private attribut _current_health i en (potentielt) fremmed klasse.
Derfor definerer vi en anden metode get_hit, som reducerer _current_health for det objekt, som den tilhører, med attackpower.

Tilføj en klasse "Healer", som arver fra klassen Character.
En healer har attackpower=0 men den har en ekstra attribut "healpower".

Tilføj en metode "heal" til "Healer", som fungerer som "hit" men forbedrer sundheden med healpower.
For at undgå at "heal" forandrer den protected attribut "_current_health" direkte,
tilføj en metode get_healed til klassen Character, som fungerer lige som get_hit.

Hvis du er gået i stå, kan du spørge google, de andre elever eller læreren (i denne rækkefølge).
Hvis du ikke aner, hvordan du skal begynde, kan du åbne S0720_rpg1_help.py og starte derfra.

Når dit program er færdigt, skal du skubbe det til dit github-repository
og sammenlign det med lærerens løsning i S0730_rpg1_solution.py

Send derefter denne Teams-besked til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""

"""opgave: Objektorienteret rollespil, del 2 :

Som altid skal du læse hele øvelsesbeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Byg videre på din løsning af del 1.

Opfind to nye klasser, som arver fra klassen Character. For eksempel Hunter og Magician.
Dine nye klasser skal have deres egne ekstra metoder og/eller attributter.
Måske overskriver de også metoder eller attributter fra klassen Character.

Lad i hovedprogrammet objekter af dine nye klasser (dvs. rollespilfigurer) kæmpe mod hinanden,
indtil den ene figur er død. Udskriv, hvad der sker under kampen.

I hver omgang bruger en figur en af sine evner (metoder). Derefter er det den anden figurs tur.
Det er op til dig, hvordan dit program i hver tur beslutter, hvilken evne der skal bruges.
Beslutningen kan f.eks. være baseret på tilfældighed eller på en smart strategi

Opgradering 1:
Hver gang en figur bruger en af sine evner, skal du tilføje noget tilfældighed til den anvendte evne.

Opgradering 2:
Lad dine figurer kæmpe mod hinanden 100 gange.
Hold styr på resultaterne.
Prøv at afbalancere dine figurers evner på en sådan måde, at hver figur vinder ca. halvdelen af kampene.

Hvis du går i stå, kan du spørge google, de andre elever eller læreren (i denne rækkefølge).

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-besked til din lærer: <filename> done
Fortsæt derefter med den næste fil."""

import random


class Character:

    def __init__(self, name, max_health, attack_power):
        self.name = name
        self._max_health = max_health
        self._current_heath = max_health
        self._attack_power = attack_power
        self._is_alive = True

    def __repr__(self):
        return f"chareture name:({self.name}) health:({self._max_health})/({self._current_heath}) attack:({self._attack_power})"

    def AI_target(self, list_of_targetes):
        return random.choice(list_of_targetes)

    def AI_atteck(self, target):  # this method existes to be overriden. but makes it so i can call atteck method and know the class does what it does with the attck
        self.hit(target)

    def hit(self, target_to_damige):
        print(f"Character {self.name} is attacking {target_to_damige}")
        target_to_damige.get_hit(self._attack_power)

    def check_healt(self):
        return self._is_alive

    # damiges chareture
    def get_hit(self, damige_delt):
        self._current_heath -= damige_delt

        if self._current_heath <= 0:
            self._is_alive = False
            print(self.name + " has died")

    # heals hareture
    def get_healed(self, heal):
        self._current_heath += heal

        # makes sure the character does not have more hp then the character max hp
        if self._current_heath >= self._max_health:
            self._current_heath = self._max_health  # sets Character hp to its hp max


class Healer(Character):

    def __init__(self, name, max_health, healpower):
        super().__init__(name, max_health, 0)
        self._heal_power = healpower

    def AI_atteck(self, target):
        self.heal(target)

    def heal(self, target_to_heal):
        print(f"healer {self.name} is healing {target_to_heal}")
        target_to_heal.get_healed(self._heal_power)


# has a radom chanse to heal or damige
class Mage(Character):

    def __init__(self, name, max_health, attack_power, magic_power):
        super().__init__(name, max_health, attack_power)
        self._magic_power = magic_power

    def __repr__(self):
        return f"the mage name:({self.name}) health:({self._max_health})/({self._current_heath}) attack:({self._attack_power}) magic power({self._magic_power})"

    def AI_atteck(self, target):
        self.magic(target)

    def magic(self, target):

        print(f"mage {self.name} is casting a spell at {target}")
        wild_magic = random.randint(1, 3)

        if wild_magic == 1:  # does attack damige
            target.get_hit(self._attack_power + self._magic_power)

        elif wild_magic == 2:
            target.get_hit(1)

        elif wild_magic == 3:
            self.buff_up_magic()

    def buff_up_magic(self, buff_size=1.25):
        self._magic_power *= buff_size


karen = Character("Karen", 60, 15)
inploig = Character("denis", 80, 1)
manegure = Healer("steve", 100, 10)
povel = Mage("povel", 60, 5, 10)
print(karen)

print()
# karen hits inploig
karen.hit(inploig)
print(inploig)

print()
# manegure heals inploig
manegure.hit(karen)
manegure.heal(inploig)  # notes that inploig only get hp op to his max
print(str(karen) + "\n" + str(inploig))

Character_list = [karen, inploig, manegure, povel]

turns = 0
while turns <= 100:  # runs the game ontil only one or less Characters are left

    chareture_turn = random.choice(Character_list)

    # checks if the Character is alive
    if chareture_turn.check_healt():  # if the Character is alive then the Character gets to atteck
        print(f"Turn:({turns})")
        chareture_turn.AI_atteck(chareture_turn.AI_target(Character_list))
    else:  # if the character is not alive then there are removed from the list
        Character_list.remove(chareture_turn)

    turns += 1

print(f"{Character_list} the game took ({turns - 1}) turns")
