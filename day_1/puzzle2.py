import sys

puzzle_input = sys.argv[1]
floor = 0

for index, char in enumerate(puzzle_input):
    if(char == '('):
        floor += 1
    elif (char == ')'):
        floor -= 1
    else: 
        print "invalid character %s" %char
    #Now, check if we're in the basement
    if(floor == -1):
        print "The index of the first basement entry is %s" % (index+1)
        break
print "The floor is %s" %floor
