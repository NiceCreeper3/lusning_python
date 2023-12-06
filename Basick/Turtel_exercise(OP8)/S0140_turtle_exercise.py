"""
Opgave "Tom the Turtle":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Funktionen "demo" introducerer dig til alle de kommandoer, du skal bruge for at interagere med Tom i de følgende øvelser.

Kun hvis du er nysgerrig og elsker detaljer:
    Her er den fulde dokumentation for turtle graphics:
    https://docs.python.org/3.3/library/turtle.html

Del 1:
    Skriv en funktion "square", som accepterer en parameter "length".
    Hvis denne funktion kaldes, får skildpadden til at tegne en firkant med en sidelængde på "længde" pixels.

Del 2:
     Færdiggør funktionen "visible", som skal returnere en boolsk værdi,
     der angiver, om skildpadden befinder sig i det synlige område af skærmen.
     Brug denne funktion i de følgende dele af denne øvelse
     til at få skildpadden tilbage til skærmen, når den er vandret væk.

Del 3:
    Skriv en funktion "many_squares" med en for-loop, som kalder square gentagne gange.
    Brug denne funktion til at tegne flere firkanter af forskellig størrelse i forskellige positioner.
    Funktionen skal have nogle parametre. F.eks:
        antal: hvor mange firkanter skal der tegnes?
        størrelse: hvor store er firkanterne?
        afstand: hvor langt væk fra den sidste firkant er den næste firkant placeret?

Del 4:
    Skriv en funktion, der producerer mønstre, der ligner dette:
    https://pixabay.com/vectors/spiral-square-pattern-black-white-154465/

Del 5:
    Skriv en funktion, der producerer mønstre svarende til dette:
    https://www.101computing.net/2d-shapes-using-python-turtle/star-polygons/
    Funktionen skal have en parameter, som påvirker mønsterets form.

Del 6:
    Opret din egen funktion, der producerer et sejt mønster.
    Senere, hvis du har lyst, kan du præsentere dit mønster på storskærmen for de andre.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil.
"""

import turtle  # this imports a library called "turtle". A library is (someone else's) python code, that you can use in your own program.


# you will need this: x-value: turtle_name.position()[0]
# and this:           y-value: turtle_name.position()[1]
# den(2)
def visible(turtle_name):  # returns true if both the x- and y-value of the turtle's position are between -480 and 480
    # runs fruge the position list. and if X or Y is bigger then 480 or smaller then -480 then it retuns false. but if it findes nothing wrong then it returns true
    for x in turtle_name.position():
        if x > 480 or x < -480:
            return False

    return True



def demo():  # demonstration of basic turtle commands
    tom = turtle.Turtle()  # create an object named tom of type Turtle
    print(type(tom))
    tom.speed(1)  # fastest: 10, slowest: 1
    for x in range(8):  # do the following for x = 0, 1, 2, 3, 4, 5, 6, 7
        tom.forward(50)  # move 50 pixels
        tom.left(45)  # turn 45 degrees left
        print(f'Tom is now at {tom.position()}, x-value: {tom.position()[0]=:.2f}, y-value: {tom.position()[1]=:.2f}')
    tom.penup()  # do not draw while moving from now on
    tom.forward(100)
    tom.pendown()  # draw while moving from now on
    tom.pencolor("red")  # draw in red
    tom.right(90)  # turn 90 degrees right
    tom.forward(120)
    tom.right(-90)  # turning -90 degrees right is the same as turning +90 degrees left
    tom.forward(120)
    tom.home()  # return to the original position in the middle of the window
    turtle.done()  # keeps the turtle window open after the program is done


# makes a turtol using the give aruments. this i a bit more clean then alwas setting its speed
def make_turtel(speed, color = "black", pen_size = 1):
    make_tortes = turtle.Turtle()
    make_tortes.speed(speed)
    make_tortes.color(color)
    make_tortes.width(pen_size)

    return make_tortes

# moves the turtol back to the screan
def return_to_scene(move_back_turtal):
    while (visible() == False):
        move_back_turtal.backwords(1)


# den(1)
def square(length, use_turtel):
    use_turtel.left(90)

    for x in range(4):
        use_turtel.forward(length)
        use_turtel.right(90)
        print(visible(use_turtel))

# den(3)
def many_squares(antal, størrelse, afstand, use_turtel):

    for x in range(antal):
        square(størrelse, use_turtel)
        use_turtel.right(45)
        use_turtel.forward(afstand)

#den(4)
def make_swerel(swerels, line_length, use_turtel):

    use_turtel.right(180)

    for x in range (0, swerels, line_length ):
        use_turtel.forward(x)
        use_turtel.left(90)

#den(5)
def make_star(star_size, star_Points, star_angels, use_turtel):

    for x in range(star_Points):
        use_turtel.right(star_angels)
        use_turtel.forward(star_size)



tom = make_turtel(2, "black",2)


# many_squares(6, 60, 80)
#make_swerel(400, 5, tom)


# numberers 134

# stars
#make_star(100, 5, 144, tom) # 5 points star
#make_star(100, 7, -154, tom) # 7 points star
make_star(100, 11, 164, tom) # 11 points star
#make_star(100, 20, 100, tom) # flower

turtle.done()

