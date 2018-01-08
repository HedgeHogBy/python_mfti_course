import sys

steps = int(sys.argv[1])
i = 1

while i <= steps:
    emptySpaceNumber = steps - i
    numberOfSharps = i
    stepToPrint = (" " * emptySpaceNumber) + ("#"*numberOfSharps)
    print(stepToPrint)
    i += 1
