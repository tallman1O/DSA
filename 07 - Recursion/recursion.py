def printNumFive(num):
    if num>0:
        print(num)
        printNumFive(num-1)
    else:
        return

printNumFive(4)