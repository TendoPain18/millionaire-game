import random
import arabic_reshaper


class Questions:
    def __init__(self):
        self.All_Q = []
        self.All_A = []
        self.All_B = []
        self.All_C = []
        self.All_D = []
        self.All_R = []

    def GenerateNumbers(self, number):
        NumList = []
        for i in range(15):
            random_number = (random.randint(1, number) * 6) - 4
            while random_number in NumList:
                random_number = (random.randint(1, number) * 6) - 4
            NumList.append(random_number)
        return NumList

    def EmptyLists(self):
        self.All_Q = []
        self.All_A = []
        self.All_B = []
        self.All_C = []
        self.All_D = []
        self.All_R = []

    def PrepareString(self, sentence):
        english = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                   'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7',
                   '8', '9']
        if sentence[0] in english:
            return sentence
        reshaped = arabic_reshaper.reshape(sentence)
        reversed_text = reshaped[::-1]
        return reversed_text

    def readfile(self):
        self.EmptyLists()
        file = open('questions.txt', 'r', encoding='utf-8')
        NumberOfLines = int(file.readline())
        QuestionsLines = self.GenerateNumbers(NumberOfLines)
        for i, line in enumerate(file):
            if i+2 in QuestionsLines:
                self.All_Q.append(self.PrepareString(line.strip('\n ?؟')))
                temp = open('questions.txt', 'r', encoding='utf-8')
                for j, line2 in enumerate(temp):
                    if j == i + 1:
                        self.All_A.append(self.PrepareString(temp.readline().strip('\n ?؟')))
                        self.All_B.append(self.PrepareString(temp.readline().strip('\n ?؟')))
                        self.All_C.append(self.PrepareString(temp.readline().strip('\n ?؟')))
                        self.All_D.append(self.PrepareString(temp.readline().strip('\n ?؟')))
                        self.All_R.append(self.PrepareString(temp.readline().strip('\n ?؟')))
                temp.close()
        file.close()
