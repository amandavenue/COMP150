def new_line():
    print
    
def three_lines():
    new_line()
    new_line()
    new_line()

def nine_lines():
    three_lines()
    three_lines()
    three_lines()

print "hi"
nine_lines()
print "bye"

def clear_screen():
    nine_lines()
    nine_lines()
    nine_lines()
    nine_lines()
    new_line()
    new_line()
    new_line()
    new_line()

clear_screen()
