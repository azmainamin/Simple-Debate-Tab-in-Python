#!C:\Python33\python.exe

#Author: Azmain Amin

""" A program that simulates the debate tab. MVP only for BP and WSDC format. Randomly makes
    teams and assign the positions. Writes the information in a file."""

import random
import time as t

def makeList(numOfDebaters):
    debaters = []

    for i in range(numOfDebaters):
        debater = input("Please enter the name of the debater: " )
        
        debaters.append(debater)

    random.shuffle(debaters)

    return debaters

def templateBP(debaters):
    template = "*" * 80 + "\n"
    template += ("Opening Gov: %s, %s" % (debaters[0], debaters[1]) + "\n"
                + "Opening Opp: %s, %s" % (debaters[2], debaters[3])+ "\n"
                + "Closing Gov: %s, %s" % (debaters[4], debaters[5])+ "\n"
                + "Closing Opp: %s, %s" % (debaters[6], debaters[7])+ "\n")
    template += "\n" + "*" * 80 

    return template

def templateWSDC(debaters):
    template = "*" * 80 + "\n"
    template += ("Government: %s, %s, %s" % (debaters[0], debaters[1], debaters[2]) + "\n"
              + "Opposition: %s, %s, %s" % (debaters[3], debaters[4], debaters[5]))
    template += "\n" +  "*" * 80 

    return template

def writeToFile(debaters, numOfDebaters):
    fileName = "winter2015_debates.txt"
    file = open(fileName, "a")
    file.write("\n" + t.asctime(t.gmtime())+ "\n")
    if numOfDebaters == 8:
        file.write(templateBP(debaters))
    else:
        file.write(templateWSDC(debaters))
    file.close()
        

# MAIN #
def main():
    debaters = []
    numOfDebaters = int(input("How many debaters are there? (8 or 6)? " ))
    debaters = makeList(numOfDebaters)
    if numOfDebaters == 8:
        print(templateBP(debaters))
    else:
        print(templateWSDC(debaters))
        
    writeToFile(debaters, numOfDebaters)

if __name__ == "__main__":
    main()
