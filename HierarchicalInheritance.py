class Model:
    def train(self):
        print("Training Model")

class CNN(Model):
    print("Convolutional Neural Network")

class RNN(Model):
    print("Recurrent Neural Network")

class Transformer(Model):
    print("Transformer")

a = CNN()
a.train()
b = RNN()
b.train()
c = Transformer()
c.train()