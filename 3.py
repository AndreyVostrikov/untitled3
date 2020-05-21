import numpy
import scipy.special
import random


def vector_generator():
    result = [random.randint(-1, 1) for i in range(4)]
    return result


class neurons:

    def __init__(self, input, hidden, output, v):
        self.i = input
        self.h = hidden
        self.o = output
        self.lr = v
        self.ik = numpy.random.normal(0.0, pow(self.h, -0.5), (self.h, self.i))
        print(self.ik)
        self.who = numpy.random.normal(0.0, pow(self.o, -0.5), (self.o, self.h))
        print(self.who)
        self.activat = lambda x: scipy.special.expit(x)

    def about(self, inputs_list):
        i = numpy.array(inputs_list, ndmin=2).T
        h_i = numpy.dot(self.ik, i)
        h_o = self.activat(h_i)
        f_i = numpy.dot(self.who, h_o)
        f_o = self.activat(f_i)
        return f_o

    def train(self, i_l):
        i = numpy.array(i_l, ndmin=2).T
        print("1\n", i)
        h_i = numpy.dot(self.ik, i)
        print("2\n", h_i)
        h_o = self.activat(h_i)
        print("3\n", h_o)
        f_i = numpy.dot(self.who, h_o)
        print("4\n", f_i)
        f_o = self.activat(f_i)
        print("5\n", f_o)
        self.who += self.lr * numpy.dot(f_o, numpy.transpose(h_o))
        self.ik += self.lr * numpy.dot(h_o, numpy.transpose(i))
        self.lr -= 0.05


input = 4
hidden = 5
output = 5
v = 0.5
i_d = vector_generator()
neo = neurons(input, hidden, output, v)
series = 5
data_list = [vector_generator() for i in range(0, series)]
for i in data_list:
    neo.train(i)

set1 = [1, -1, 0, 1]
set2 = [1, 0, -1, 1]
set3 = [1, 1, 0, -1]
set4 = [0, 1, 1, -1]
test_data = [set1, set2, set3, set4]
print("\n\nset1\n", neo.about(set1))
print(numpy.argmax(neo.about(set1)) + 1)
print("\n\nset2\n", neo.about(set2))
print(numpy.argmax(neo.about(set2)) + 1)
print("\n\nset3\n", neo.about(set3))
print(numpy.argmax(neo.about(set3)) + 1)
print("\n\nset4\n", neo.about(set4))
print(numpy.argmax(neo.about(set4)) + 1)
