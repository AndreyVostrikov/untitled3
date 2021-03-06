import math


class Neuron:
    def __init__(self, matrix, numbers, weights, age11, n11):
        self.matr = matrix
        self.number = numbers
        self.weight = weights
        self.age = age11
        self.n = n11

    def pers(self, x):
        return 1 / (1 + math.exp(-x))

    def learn(self):
        while self.age >= 0:
            z = []
            for p in self.matr:
                y = 0
                for i in range(len(self.weight)):
                    y += p[i] * self.weight[i]
                z.append(self.pers(y))

            for j in range(len(self.weight) - 1):
                d = 0
                for i in range(len(z)):
                    d += (z[i] - self.number[i]) * z[i] * (1 - z[i]) * self.matr[i][j]
                d *= 2
                self.weight[j] -= d * self.n
            self.age -= 1

    def final(self, t):
        value = 0
        for j in range(len(t)):
            value += t[j] * self.weight[j]

        return self.pers(value)


matr = [[1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [1, 1, 1, 0, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 1, 1, 1], ]

number = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
weight = [1, 0, 1, 0, 1, 0, 1, 0]
age = 100000
n = 1

designation = {
    0: matr[0], 1: matr[1], 2: matr[2], 3: matr[3], 4: matr[4],
    5: matr[5], 6: matr[6], 7: matr[7], 8: matr[8], 9: matr[9], }

neuron = Neuron(matr, number, weight, age, n)
neuron.learn()

try:
    print("Нейрон видит цифру 3")
    while True:
        number = input("Num = ")
        number.isdigit()
        xx = designation[int(number)]
        print(round(neuron.final(xx), 2))

except:
    print("Введите однозначное число!")
