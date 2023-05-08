from math import sqrt

def rmse(y_true, y_pred):
    assert len(y_true) == len(y_pred) , "y_true and y_pred should be same length"
    mean_sqr = sum((tru - pred) ** 2 for tru, pred in zip(y_true, y_pred)) / len(y_true)
    return sqrt(mean_sqr)

print(rmse([1,2,3],[3,2,1]))
