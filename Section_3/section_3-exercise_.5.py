def value_sequence(number):
    strnumber = str(number)
    sequenceList = list()
    scoreList = list()
    i = 0
    for element in strnumber:
        sequenceList.append(element)
    sequenceList.sort()
    sequenceList.reverse()
    while i < 10:
        scoreList.append(sequenceList[i])
        i += 1
    return scoreList


while True:
    number = str(input("Enter a sequence of numbers greater than 10"
                       " with last number=0: "))
    intNumber = int(number)
    if number[-1] == "0":
        print(value_sequence(intNumber))
        break
    else:
        continue
