import sys

digitString = sys.argv[1]
numSum = 0

for number in digitString:
    numSum += int(number)

print(numSum)
