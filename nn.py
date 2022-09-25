from math import exp
import numpy as np

train_input = np.random.randint(2, size=(4, 4))

train_output = np.random.randint(2, size=1)

def sigmoid(x):
    return 1 / (1 + exp(-x))

output = sigmoid()



error = output - train_output

print(error)
