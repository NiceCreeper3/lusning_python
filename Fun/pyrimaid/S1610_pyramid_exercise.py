"""Opgave "Number pyramid"

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Denne øvelse er en valgfri udfordring for de fremragende programmører blandt jer.
Du behøver absolut ikke at løse denne øvelse for at fortsætte med succes.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Se de første 93 sekunder af denne video: https://www.youtube.com/watch?v=NsjsLwYRW8o

Skriv en funktion "pyramid", der producerer de tal, der er vist i videoen.
Funktionen har en parameter "lines", der definerer, hvor mange talrækker der skal produceres.
Funktionen udskriver tallene i hver række og også deres sum.

I hovedprogrammet kalder du funktionen med fx 7 som argument.

Tilføj en mere generel funktion pyramid2.
Denne funktion har som andet parameter "firstline" en liste med pyramidens øverste rækkens tallene.

I hovedprogrammet kalder du pyramid2 med fx 10 som det første argument
og en liste med tal efter eget valg som andet argument.
Afprøv forskellige lister som andet argument.

Hvis du ikke aner, hvordan du skal begynde, kan du åbne S1620_pyramid_help.py og starte derfra

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""


def pyramid(lines_to_make):
    lines_list = [[1, 1]]  # is goving to contain all the (lines lists) of numberes

    for line in range(lines_to_make -1 ):  # runes fruge all the lines. the -1 is there cose we alrede have the [1,1] ind the tulpe
        new_line = []  # saves the list tempearelig here
        prives_number = 0

        for number in lines_list[line]:  # goes fruge the numbers of the prvies list. the reason we are donving range is cos ve need the dreveise nummber to

            if number + prives_number == line + 2:  # if the current number + with the priveis number is the same as line nuber then it apps line to the list
                new_line.append(line + 2)  # need to add +1 cose line starts at 0
                print("extranumber has bean addede", line + 2)

            new_line.append(number)  # adds the current number to the list
            prives_number = number  # reambers what the prives number

        lines_list.append(new_line)  # adds the list to the lines_list
        print(lines_list)

    return lines_list


def triangel_print(line_list, space_lengt = 25):
    spases = " " # maeks spases

    for line in range(len(line_list)):

        for spase in range(space_lengt - len(line_list[line])):
            spases += " "

        print(spases, line_list[line])
        spases = " " # reasets





triangel_list = pyramid(7, )
print()
triangel_print(triangel_list)
