def part_two(): # function declaration
    x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"] # list of values  
    for i in x: # loop through the list
        if isinstance(i, int) == True: # check if i is an integer
            print "*" * i # print a star for every int found
        if isinstance(i, str) == True: # check if i is a string
            print i[0].lower() * len(i) # print the first letter of the string for the number of characters
part_two()

