#course: Object-oriented programming, year 2, semester 1
#academic year: 201920
#author: B. Schoen-Phelan
#date: 29-09-2019
#purpose: Lab 2

class Types_and_Strings:
    def __init__(self):
        pass

    def play_with_strings(self):
        # working with strings
        message = input("Enter your noun: ")
        print("Originally entered: " + message)

        # print only first and last of the sentence
        print("First char: " + message[0])
        print("Last char: " + message[-1])

        # use slice notation
        print(message[:])
        print(message[:4])
        print(message[2:])
        print(message[1:2])
        print(message[1:5:3])
        print(message[1:4:2])
        print(message[1:4:2])

        # escaping a character
        print("He said \"that's fantastic\"!")

        # find all a's in the input word and count how many there are
        x = str(message.find("a"))
        y = str(message.count("a"))
        print("The number of a's in the input is: " + x + "\nThere are " + y + " of a's")
        print("Total number of characters: " + str(len(message)))

        # replace all occurences of the character a with the - sign
        # try this first by assignment of a location in a string and
        # observe what happens, then use replace()
        message = message.replace("a", "-")
        print(message)

        # printing only characters at even index positions
        for i in range(0, 20, 2):
            print("index" + "[" + str(i) + "] " + message[i])

        length = len(message)
        for i in range(0, length, 2):
            print("index" + "[" + str(i) + "] " + message[i])

        length = len(message)
        for i in range(0, length, 2):
            print("index" + "[" + str(i) + "] " + message[i])


    def play_with_lists(self):
        message = input("Please enter a whole sentence: ")
        print("Originally entered: "+ message)

        # hand the input string to a list and print it out
        thislist = message.split()
        print(thislist)

        # append a new element to the list and print
        thislist.append("boom")
        thislist.append("bello")
        print(thislist)

        # remove from the list in 3 ways
        # if not in list returns error
        thislist.remove("boom")
        del thislist[:1]
        test = thislist.pop()
        print(thislist)
        print(test)

        # check if the word cake is in your input list
        word = "cake"
        try:
            thislist.remove(word)
        except ValueError:
            print("Cake in not in the list")

        # reverse the items in the list and print
        thislist.reverse()
        print(thislist)
        # returns None print(thislist.reverse())

        # reverse the list with the slicing trick
        # but it does not save the list as reversed, only shows reverse during printing
        print(thislist[::-1])

        # print the list 3 times by using multiplication
        print(3 * thislist)


tas = Types_and_Strings()
#tas.play_with_strings()
tas.play_with_lists()
