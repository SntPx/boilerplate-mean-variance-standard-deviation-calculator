import numpy as np

def calculate(l):
    if len(l) < 9:
        raise ValueError("List must contain nine numbers.")
    matrix = np.array(l).reshape(3,3)
    operations = {"mean": np.mean, "variance": np.var, "standard deviation": np.std, "max": np.max, "min": np.min, "sum": np.sum}
    calculations = {}
    for k, v in operations.items():
        calculations[k] = [v(matrix, 0).tolist(), v(matrix,1).tolist(), v(matrix)]

    return calculations
