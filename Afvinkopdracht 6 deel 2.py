# 1. File Display
"""
Opens a file and then reads the content.
"""
def open_and_read_file():
    file = open("numbers.txt", 'r')
    print(file.read())
    file.close()


def main():
    open_and_read_file()

main()

# 5. Sum of Numbers
def read_file(file):
    """
    Reads a file and then returns the total of all numbers in the file.
    input -> file (a file)
    output -> total (the total of all numbers in the file)
    """
    numbers = file.read()
    total = 0
    for number in numbers:
        if number != ' ':
            total += int(number)

    return total

def main():
    file = open("numbers.txt", 'r')
    total_num = read_file(file)
    print(total_num)

main()

# 7. Word List File Writer
def enter_words(amount_of_words, file):
    """
    let's the user enter the word_count amount of words and writes them to a file.
    input -> word_count
    output -> new_file.txt (create file)
    """
    counter = 0
    while counter < amount_of_words:
        word_holder = input("Enter word number: " + str(counter + 1) + " ")
        file.write(word_holder)
        counter += 1


def main():
    word_count = int(input("How many words do you want to enter? "))
    new_file = open("new_file.txt", "x")
    enter_words(word_count, new_file)

main()
