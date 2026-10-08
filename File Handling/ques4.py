with open("newtextfile.txt", "r") as f:
    listoflines = f.readlines()
    print("Number of lines are: ", len(listoflines))
    