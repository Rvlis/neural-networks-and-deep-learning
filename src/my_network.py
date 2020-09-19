import random
import numpy as np

class Network(object):

    def __init__(self,sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = 
        self.weights = 

    def feedforward(self,a):
        for b,w in zip(self.biases,self.weights):
            a = sigmoid(np.dot(w,a)+b)
        return a
    
    def sigmoid(z):
        return 1.0/(1.0+np.exp(-z))

    def SGD(self,training_data, epochs, mini_batch_size, eta, test_data = None):

        if test_data:
            n_test = len(test_data)

        n = len(training_data)
        for j in xrange(epochs):
            random.shuffle(training_data)
            mini_batch = 

        for mini_batch in mini_batches:
            self.updata_mini_batch(mini_batch,eta)
        
        if test_data:
            print 
        else :
            print

    def updata_mini_batch(self,mini_batch,eta):
        nabla_b = 
        nabla_e = 
        for x,y in mini_batch:


        self.weights = 
        self.biases = 

    
    def backdrop(self,x,y):

    
    def evaluate(self, test_data):

    def cost_derivative(self, output_activations, y):

    def sigmoid_prime(z):
        return sigmoid(z)*(1-sigmoid(z))