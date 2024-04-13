import random

class InsertionSort:
    def sort(self, inputList):
        for i in range(1, len(inputList)):
            key = inputList[i]
            j = i - 1
            while key < inputList[j] and j >= 0:
                inputList[j + 1], inputList[j] = inputList[j], inputList[j + 1]
                j -= 1
        return inputList
def main():
    o = InsertionSort()

    inputList = []
    randomNum = random.randint(10, 50)
    for i in range(randomNum):
        randomInt = random.randint(-100, 100)
        inputList.append(randomInt)

    print(inputList)
    print(o.sort(inputList))

# Main code
if __name__ == "__main__":
    main()


