import sys

puzzle_input = sys.argv[1]
floor = 0

for char in puzzle_input:
    if(char == '('):
        floor += 1
    elif (char == ')'):
        floor -= 1
    else: 
        print "invalid character %s" %char

print "The floor is %s" %floor
