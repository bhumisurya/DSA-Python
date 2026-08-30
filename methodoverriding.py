class Model:
    def predict(self):
        print("Model Prediction")

class CNN(Model):
    def predict(self):
        print("Convolutional Neural Network")

a = CNN()
b = Model()
a.predict()
b.predict()