"""Opgave "The inventory sequence"

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Denne øvelse er en valgfri udfordring for de fremragende programmører blandt jer.
Du behøver absolut ikke at løse denne øvelse for at fortsætte med succes.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Del 1:
    Se de første 3 minutter af denne video:
    https://www.youtube.com/watch?v=rBU9E-ZOZAI

Del 2:
    Skriv en funktion inventory(), som producerer de tal, der er vist i videoen.
    Funktionen accepterer en parameter, der definerer, hvor mange talrækker der skal produceres.
    Funktionen udskriver tallene i hver række.

    Du vil sandsynligvis ønske at definere en funktion count_number(), som tæller, hvor ofte
    et bestemt antal optræder i den aktuelle talrække.

Del 3:
    I hovedprogrammet kalder du inventory() med fx 6 som argument.

Hvis du ikke har nogen idé om, hvordan du skal begynde, kan du kigge på løsningen
i S1720_inventory_solution.py

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""


# to fix it dobeles the intendet input
# addes a new list indside the count_number

# can be optemised so it does,t need to run fruge the hol inventory ithe time
def inventory_unoptemised(rows_to_make):
    inv_lines = []

    for inv in range(rows_to_make):

        new_line = []

        has_found_zero = False  # as found a new 0 and can stop the while
        num_to_check = 0  # represends the nummber we are checking like 1|2|3|4|5

        while not has_found_zero:

            num_gattered = 0  # represends the amout of times the same nummber has ben found

            for row in inv_lines:
                for line in row:
                    if line == num_to_check:
                        num_gattered += 1

            # checkes its oven line
            for self_check in new_line:
                if self_check == num_to_check:
                    num_gattered += 1

            if num_gattered == 0:
                has_found_zero = True

            num_to_check += 1 # goes up by one ind what number we are checking after
            new_line.append(num_gattered)

        inv_lines.append(new_line)  # addes the new line of numbers to the inventory

    return inv_lines


def right_out_inventory(inventory_list):
    number_represent = "|"

    # first right numberes ex 1|2|3|4|5|
    last_row = len(inventory_list[-1]) # gets the lengt of the fist row. as its goving to be the longest
    for n in range(last_row):
        number_represent += f"{n} |"

    print(number_represent) # prints the inv list.

    for inv in inventory_list: # prints
        print(inv)


inv_list = inventory_unoptemised(10)
right_out_inventory(inv_list)
