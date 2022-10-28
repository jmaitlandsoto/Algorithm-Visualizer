import random


def randomizeArray(array):
    for i in range(len(array)):
        temp = random.randrange(1, len(array), 1)
        while temp in array:
            temp += 1
            if temp > len(array):
                while temp in array:
                    temp -= 1
        array[i] = temp
    return array
