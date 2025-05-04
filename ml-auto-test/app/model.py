from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])  # y = 2x

def train_model():
    model = LinearRegression()
    model.fit(X, y)
    return model

def predict(model, x_input):
    return model.predict(np.array([[x_input]]))[0]
