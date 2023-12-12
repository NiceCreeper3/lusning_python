"""
Opgave "Reading from a file":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Opret en tekstfil med en editor efter eget valg (pycharm, notepad, notepad++ osv.)
Hver række skal bestå af en persons navn efterfulgt af et mellemrum og et tal, der repræsenterer personens alder.
gem filen i din løsningsmappe

Skriv et program, der læser filen til en liste af strings.
Derefter brug indholdet af hver string til at udskrive en række som f.eks:
    <navn> er <alder> år gammel.

Hvis du går i stå, så spørg google, de andre elever eller læreren (i denne rækkefølge).

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil.
"""

# ((( Values )))
data_to_write = ["bob", " ", "47", "\n", "steve", " ", "12"]
file_path = "S0165_files_exer.txt"

# ((( fungsens )))
# adds a new line with a name and age
def add_person(name, age, given_file_path):
    with open(given_file_path, "at") as file_open:
        file_open.writelines([ "\n", name, " ", age])

# replases what is ind the fille with the given list
def overwrirt_all(list, given_file_path):
    with open(given_file_path, "w") as file_open:
        file_open.writelines(list)

# writes out the list using spaces to devide name and age
def write_out_file (given_file_path):
    with open(given_file_path) as file_open:
        for x in file_open:
            line = x.split() # divedes the string using space. and then saves it ind a list
            print(f"{line[0]} er {line[1]} år gamel")
        print()

# ((( main program )))
# uses a list
overwrirt_all( data_to_write, file_path)

add_person("hank", "34", file_path)
add_person("steve", "47", file_path)
add_person("bof", "12", file_path)

write_out_file(file_path)
