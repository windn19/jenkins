import joblib
import numpy as np
import pytest
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error as mae


@pytest.fixture
def y():
    return np.load('y.npy')
    


@pytest.fixture
def y1():
    return np.load('y1.npy')


@pytest.fixture
def x():
    return np.load('x.npy')


def test_dataset(x, y, y1):
    model = joblib.load('model.joblib')
    pred = model.predict(x.reshape(-1, 1))
    assert mae(y, pred) < 3, "Ошибка первого датасета"
    assert mae(y1, pred) < 3, "Ошибка второго датасета"
