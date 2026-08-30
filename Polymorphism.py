class Model:
    def predict(self,data):
        pass

class CNN(Model):
    def predict(self,data):
        return "Convolutional Neural Network"

class RNN(Model):
    def predict(self, data):
        return "Recurrent Neural Network"

class RandomForest(Model):
    def predict(self, data):
        return "Random Forest"

a = CNN()
b = RandomForest()
c = RNN()

print(a.predict("Image data"))
print(b.predict("Multiple TREES"))
print(c.predict("Sequential data"))