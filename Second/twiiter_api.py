"""
MODULE DOCSTRING
"""
import sys
import json
import timeline
import friends

def main():
    """
    MAIN FUNCTION
    """
    # Pick what file you want to open
    while True:
        factor = input("If you have .json file, print 1, \
if you have to generate .json file, print 2: ")
        if factor == "1":
            while True:
                try:
                    source = input("Print the path to your file")
                    with open(source, encoding="utf-8") as file:
                        data = json.load(file)
                    break
                except:
                    print("The wrong file name or path. Try again")
                    pass
            break
        elif factor == "2":
            while True:
                count = input("Print how many tweets or friends you want to show (between 1 and 1000): ")
                try:
                    if int(count) < 1 or int(count) > 1000:
                        print("You printed wrong value. The program will show you default count of tweets.")
                        count = None
                        break
                    else:
                        break
                except ValueError:
                    print("You printed wrong value. The program will show you default count of tweets.")
                    count = None
                    break
            while True:
                generator = input("If you want to generate user timeline, print 1, \
if you want ot generate friends list, print 2: ")
                if generator == "1":
                    data = timeline.search(count)
                    break
                elif generator == "2":
                    data = friends.search(count)
                    break
                else:
                    pass
            break
        else:
            pass

    # Information
    print("That is a program to inspect json files.")
    print("If you want to go to the previous object, type 'BACK'")
    print("If you want to exit the program, type 'EXIT'")
    print("If you want to return to the start of the directories, type '-1'")
    input("To start, press anything")

    # Main function call
    while True:
        try:
            walker(data)
        except ConnectionResetError:
            pass

def walker(file):
    """
    Function that walks through the .json file
    """
    while True:
        if type(file) == dict:
            print("Object is a dictionary. That is its keys: " + str(list(file.keys())))
            keys = list(file.keys())
            for key_index in range(len(keys)):
                print(str(key_index + 1) + " - " + keys[key_index])
            element_index = inputer("Enter what element you want to inspect: ", len(keys))
            if element_index is False:
                return
            walker(file[keys[element_index - 1]])

        elif type(file) == list:
            print("Object is a list. Its length is " + str(len(file)))
            for elem in range(len(file)):
                print(str(elem + 1) + " - " + str(file[elem]))
            element_index = inputer("Enter what element you want to inspect: ", len(file))
            if element_index is False:
                return
            walker(file[element_index - 1])

        else:
            print(file)
            input("Press anything to return to the previous object")
            return None


def inputer(string, max_num):
    """
    Function that checks inputs
    """
    element_index = 0
    while element_index <= 0 or element_index > max_num:
        try:
            element_index = input(string)
            if element_index.upper() == "BACK":
                return False
            if element_index.upper() == "EXIT":
                sys.exit()
            if element_index.upper() == "-1":
                raise ConnectionResetError
            element_index = int(element_index)
            if element_index <= 0 or element_index > max_num:
                raise ValueError
        except ValueError:
            print("Wrong input. Type the integer between 1 and " + str(max_num))
            element_index = 0
    return element_index


if __name__ == "__main__":
    main()
