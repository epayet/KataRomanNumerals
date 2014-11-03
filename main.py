from roman_letters import to_roman

__author__ = 'manu'

if __name__ == '__main__':
    print "Welcome to the Roman Number conversion tool (Enter q to exit) \n"
    not_stop = True

    while not_stop:
        number = raw_input("Please enter a number: ")
        if number == "q":
            not_stop = False
            print "Goodbye!"
            break
        roman = to_roman(number)
        print "Roman: " + roman
