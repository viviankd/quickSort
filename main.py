# Vivian Duong
# CS 450 Fall 2022\
# 10/2/22
# Professor Williams

# This program sorts players' skills in different categories given
# Standard sort is Hoare's quicksort
# Custom sort is a hybrid of counting sort and quicksort
# To run: python3 main.py custom/standard < file.txt

import sys
import time

# puts all the data into a 2D list
def readInput():
    scoresList = []
    for line in sys.stdin:
        scoresList.append([int(i) for i in line.split()])
    return scoresList

# Creates list of the given skill from the 2D array
def getSkills(skill, scoresList):
    skillArray = []
    for row in scoresList:
        skillArray.append(row[skill])
    return skillArray

# Gets the sums of all the players' xp and puts them in a list
def getTotal(scorelist):
    sumArray = []
    for row in scorelist:
        sumArray.append(sum(row))
    return sumArray

# quicksort
def partition(skillArray, low, high):
    pivot = skillArray[(high + low) // 2]
    left = low - 1
    right = high + 1

    while (True):
        left += 1
        while skillArray[left] > pivot: # swapped for descending
            left += 1
        right -= 1
        while skillArray[right] < pivot: # swapped for descending
            right -= 1
        if left >= right:
            return right
        skillArray[left], skillArray[right] = skillArray[right], skillArray[left]

#  quicksort
def standardHoare(scoresList, low, high):
    if (low >= 0 and high >= 0 and low < high ):
        pivot = partition(scoresList, low, high)
        standardHoare(scoresList, low, pivot)
        standardHoare(scoresList, pivot + 1, high)

# counting sort
def customSort(scoresList):
    result = [0] * len(scoresList)
    maximum = max(scoresList)
    minimum = min(scoresList)
    totalRange = maximum - minimum + 1

    counts = [0] * totalRange

    for i in range(0, len(scoresList)):
        counts[scoresList[i] - minimum] += 1

    for i in range(1, len(counts)):
        counts[i] += counts[i-1]

    for i in range(len(scoresList)-1, -1, -1):
        result[counts[scoresList[i] - minimum] - 1] = scoresList[i]
        counts[scoresList[i] - minimum] -= 1

    for i in range(len(scoresList)):
        scoresList[i] = result[i]

    return scoresList.reverse()

# writes the sorted scores to an output file
def printArray(arr):
    for i in range(len(arr)):
        f.write(str(arr[i]) + "\n")

# given the input is standard, execute quicksort on the data
def standardCase(scoresList):
    totalTime = 0
    for x in range(6):
        skillList = []
        if x == 5:
            skillList = getTotal(scoresList)
        else:
            skillList = getSkills(x, scoresList)

        if x == 0:
            f.write("SKILL_BREAKDANCING" + "\n")
        if x == 1:
            f.write("SKILL_APICULTURE" + "\n")
        if x == 2:
            f.write("SKILL_BASKET" + "\n")
        if x == 3:
            f.write("SKILL_XBASKET" + "\n")
        if x == 4:
            f.write("SKILL_SWORD" + "\n")
        if x == 5:
            f.write("TOTAL_XP" + "\n")
        high = len(skillList) - 1
        start_time = time.time_ns()
        standardHoare(skillList, 0, high)
        time_taken_in_microseconds = (time.time_ns() - start_time) / 1000.0
        totalTime += time_taken_in_microseconds
        printArray(skillList)
        f.write("Time taken: " + str(time_taken_in_microseconds) + "\n")
        f.write("\n")

    f.write("total time taken: " + str(totalTime))
    print("total time taken: ", str(totalTime))

#  given the method is custom, execute custom sort on the data
def customCase(scoresList):
    totalTime = 0
    for x in range(6):
        if x == 0:
            f.write("SKILL_BREAKDANCING" + "\n")
        if x == 1:
            f.write("SKILL_APICULTURE" + "\n")
        if x == 2:
            f.write("SKILL_BASKET" + "\n")
        if x == 3:
            f.write("SKILL_XBASKET" + "\n")
        if x == 4:
            f.write("SKILL_SWORD" + "\n")
        if x == 5:
            f.write("TOTAL_XP" + "\n")

        start_time = time.time_ns()
        skillList = []
        if x == 5:
            skillList = getTotal(scoresList)
        else:
            skillList = getSkills(x, scoresList)
        bigList = []
        smallList = []
        for i in range(len(skillList)):
            if skillList[i] > 9999:
                bigList.append(skillList[i])
            else:
                smallList.append(skillList[i])
        high = len(bigList) - 1
        customSort(smallList)
        standardHoare(bigList, 0, high)
        time_taken_in_microseconds = (time.time_ns() - start_time) / 1000.0
        totalTime += time_taken_in_microseconds
        printArray(bigList)
        printArray(smallList)
        f.write("Time taken: " + str(time_taken_in_microseconds) + "\n")
        f.write("\n")

    f.write("total time taken: " + str(totalTime))
    # print("total time taken: ", str(totalTime))


if __name__ == '__main__':
    scoresList = readInput()
    f = open("./output.txt", "w")

    if sys.argv[1] == "standard":
        standardCase(scoresList)

    elif sys.argv[1] == "custom":
        customCase(scoresList)
    else:
        print("please try again with \"standard\" or \"custom\"")

    f.close()
