#from app.model import train_model, predict
import sys
import os

# Adiciona o diretório raiz (onde está a pasta app/) ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.model import train_model, predict

def test_model_training():
    model = train_model()
    assert model.coef_[0] == 2.0

def test_model_prediction():
    model = train_model()
    prediction = predict(model, 6)
    assert round(prediction) == 12
