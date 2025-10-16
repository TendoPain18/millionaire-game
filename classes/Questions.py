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

    @staticmethod
    def GenerateNumbers(number):
        NumList = []
        for i in range(15):
            random_number = random.randint(0, number-1)
            while random_number in NumList:
                random_number = random.randint(0, number-1)
            NumList.append(random_number)
        return NumList

    def EmptyLists(self):
        self.All_Q = []
        self.All_A = []
        self.All_B = []
        self.All_C = []
        self.All_D = []
        self.All_R = []

    @staticmethod
    def PrepareString(sentence):
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
        lines = file.readlines()
        file.close()

        NumberOfQuestions = len(lines) // 6
        QuestionsLines = self.GenerateNumbers(NumberOfQuestions)
        for i in QuestionsLines:
            ql = i * 6
            self.All_Q.append(self.PrepareString(lines[ql].strip('\n ?؟')))
            self.All_A.append(self.PrepareString(lines[ql+1].strip('\n ?؟')))
            self.All_B.append(self.PrepareString(lines[ql+2].strip('\n ?؟')))
            self.All_C.append(self.PrepareString(lines[ql+3].strip('\n ?؟')))
            self.All_D.append(self.PrepareString(lines[ql+4].strip('\n ?؟')))
            self.All_R.append(self.PrepareString(lines[ql+5].strip('\n ?؟')))
