# 2. Lottery Number Generator
import random

def roll_lottery_numbers(lottery_list):
"""
gets a random integer from 0 till 9 and adds them to a list
input -> lottery_list (empty)
output -> lottery_list (contains 7 random integers)
"""
    while len(lottery_list) < 7:
        lottery_list.append(random.randint(0, 9))
    else:
        display_lottery_numbers(lottery_list)

def display_lottery_numbers(lottery_list):
"""
Adds all the integers in the lottery_list to a variable and prints them together.
Input -> lottery_list (from roll_lottery_numbers())
output -> prints "The lottery numbers are: " + the 7 random integers.
"""
    numbers = ""
    for i in lottery_list:
        numbers += str(i)

    print("The lottery numbers are: " + numbers)
    
def main():
    number_list = []
    roll_lottery_numbers(number_list)
    
main()

# 4. Number Analysis Program
def enter_numbers(number_list):
    """
    let's the user enter 20 numbers and adds them to a list

    input -> number_list (empty list)
    output -> number_list with the 20 numbers that were entered
    """
    counter = 1
    while counter < 21:
        number = input("Enter number " + str(counter) + ": ")
        number_list.append(number)
        counter += 1

    analyse_numbers(number_list)

def analyse_numbers(number_list):
    """
    calculates the lowest, highest, total and average of all numbers and prints them.

    input -> number_list (enter_numbers())
    output -> lowest number, highest number, total and average. (print)
    """
    number_list.sort()
    number_total = 0
    length = len(number_list)
    print("The lowest number is: " + str(number_list[0]))
    print("The highest number is: " + str(number_list[19]))

    for i in number_list:
        number_total += int(i)

    print("The total of all numbers is: " + str(number_total))
    number_average = number_total / length
    print("The average of all " + str(length) + " numbers is: " + str(number_average))
        
    
def main():
    number_list = []
    enter_numbers(number_list)

main()

# 6. Dice Rolling Function
import random

def roll(number_of_rolls):
    """
    rolls the amount of times given by the main function and returns a list of rolled numbers.
    input -> number_of_rolls
    output -> rolled_numbers_list
    """
    counter = 0
    rolled_numbers_list = []
    while counter < number_of_rolls:
        rolled_num = random.randint(1, 6)
        rolled_numbers_list.append(rolled_num)
        counter += 1

    return rolled_numbers_list

def main():
    number_of_rolls = int(input("Enter an integer for the amount of times you want to roll. "))
    rolled_nums = roll(number_of_rolls)
    print(rolled_nums)

main()
