import numpy as np
import math
"""
um Eingangsdaten zu normalisieren werden alle Werte durch den größten des Arrays geteilt.
In diesem Falle: 2,1,3 werden durch 5 geteilt
9,5,6 werden durch 10 geteilt
np.array(([2, 9], [1, 5], [3, 6], [5, 10]) # input data
"""


class Snakework:
    def __init__(self):
        self.num_layers = 4  # Input layer, 2x Hidden Layer, 1 Output layer
        self.input_neurons = 26 # 8 Directions. Distance from food, opponent, wall -> 24 + Health (0-100) + own length
        self.hidden_layer_1_neurons = 16
        self.hidden_layer_2_neurons = 16
        self.output_neurons = 4
        self.fitness = None
        self.z = None

        # Initialize Weights between the layers and print dimensions
        self.weights_IN_H1 = np.random.randn(self.input_neurons, self.hidden_layer_1_neurons)
        self.weights_H1_H2 = np.random.randn(self.hidden_layer_1_neurons, self.hidden_layer_2_neurons)
        self.weights_H2_OU = np.random.randn(self.hidden_layer_2_neurons, self.output_neurons)
        print("initialized input -> hidden_1 weights: {}".format(self.weights_IN_H1.shape))
        print("initialized hidden_1 -> hidden_2 weights: {}".format(self.weights_H1_H2.shape))
        print("initialized hidden_2 -> output weights: {}".format(self.weights_H2_OU.shape))

        #
        print (self.weights_H2_OU)
        #input_vector = np.array([2, 4, 11])
        #input_vector = np.array(input_vector, ndmin=2).T
        #print(input_vector, input_vector.shape)

    def forward(self, input):
        print (input)
        self.z = np.dot(input, self.weights_IN_H1)
        self.z = self.sigmoid(self.z)
        self.z = np.dot(self.z, self.weights_H1_H2)
        self.z = self.sigmoid(self.z)
        self.z = np.dot(self.z, self.weights_H2_OU)
        output = self.z

        print("Snake prediction: {}".format(output))
        return output

    @staticmethod
    def sigmoid(x):
        """
        method to calculate the sigmoid function given input x
        """
        res = 1 / (1 + np.exp(-x))
        print("Sigmoid function on {} => {}".format(x, res))
        return res

    @staticmethod
    def sigmoidPrime(x):
        """
        method to calculate the derivate of the sigmoid function given input x
        """
        return x * (1 - x)

    @staticmethod
    def relu(x):
        # Not yet working on arrays
        """
        method to calculate the relu function given input x
        """
        res = np.all(0.0, x)
        print("Sigmoid function on {} => {}".format(x, res))
        return res
