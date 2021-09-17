# 1. number analyser

number = int(input("Enter an integer"))
if number > 0:
    print("Positive")

if number < 0:
    print("Negative")

if number == 0:
    print("Zero")

if number % 2 == 0:
    print("The number is even")

if number % 2 != 0:
    print("The number is odd")



# 2. areas of Rectangles

first_width = float(input("Enter the width of the first rectangle"))
first_length = float(input("Enter the length of the first rectangle"))
second_width = float(input("Enter the width of the second rectangle"))
second_length = float(input("Enter the length of the second rectangle"))                               

Area_first_rectangle = first_width * first_length
Area_second_rectangle = second_width * second_length

if Area_first_rectangle == Area_second_rectangle:
    print("The rectangles have the same area")

elif Area_first_rectangle > Area_second_rectangle:
    print("The first rectangle has a bigger area")

elif Area_first_rectangle < Area_second_rectangle:
    print("The second rectangle has a bigger area")

else:
    print("error")



# 9. Roulette Wheel Colors

pocket_num = int(input("Enter the pocket number"))

if pocket_num > 36 or pocket_num < 0:
    print("error")

elif pocket_num == 0:
    print("The color is green")

# controleert of het getal tussen de 1 en 10 ligt.
elif pocket_num >= 1 and pocket_num <= 10:
    if pocket_num % 2 == 0:
        print("The color is black")
    elif pocket_num % 2 != 0:
        print("The color is red")

# controleert of het getal tussen de 11 en 18 ligt.
elif pocket_num >= 11 and pocket_num <= 18:
    if pocket_num % 2 == 0:
        print("The color is red")
    elif pocket_num % 2 != 0:
        print("The color is black")

# controleert of het getal tussen de 19 en 28 ligt.
elif pocket_num >= 19 and pocket_num <= 28:
    if pocket_num % 2 == 0:
        print("The color is black")
    elif pocket_num % 2 != 0:
        print("The color is red")

# controleert of het getal tussen de 29 en 36 ligt.
elif pocket_num >= 29 and pocket_num <= 36:
    if pocket_num % 2 == 0:
        print("The color is red")
    elif pocket_num % 2 != 0:
        print("The color is black")

# 17. Wi-Fi Diagnostic Tree

print("Reboot the computer and try to connect.")
if input("Did that fix the problem?") == "no":
    print("Reboot the router and try to connect")
    if input("Did that fix the problem?") == "no":
        print("Make sure the cables between the router & modem are plugged in rmly.")
        if input("Did that fix the problem?") == "no":
            print("Move the router to a new location and try to connect")
            if input("Did that fix the problem?") == "no":
                print("Get a new router.")


# opdracht 18. Restaurant Selector

vegetarian = input("Is anyone in your party a vegetarian?")
vegan = input("Is anyone in your party vegan?")
glutenfree = input("Is anyone in your party gluten-free?")

data = vegetarian + vegan + glutenfree

Joe = "nonono"
main = ["yesnoyes", "nonoyes", "yesnono", "nonono"]
corner = ["yesyesyes", "yesnono", "noyesno", "nonoyes", "yesyesno", "yesnoyes", "noyesyes", "nonono"]
mama = ["yesnono", "nonono"]
chefs = ["yesnono", "yesyesyes", "noyesno", "nonoyes", "yesyesno", "yesnoyes", "noyesyes", "nonono"]


if data in Joe:
    print("Joe’s Gourmet Burgers")
if data in main:
    print("Main Street Pizza Company")
if data in corner:
    print("Corner Café")
if data in mama:
    print("Mama’s Fine Italian")
if data in chefs:
    print("The Chef’s Kitchen")
