from typing import Any

import torch
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
import numpy as np


_data_x: np.ndarray = load_iris().data  # shape: (150,4)
_data_y: np.ndarray = load_iris().target  # shape: (150,)
_perm = np.random.permutation(len(_data_x))
_data_x = _data_x[_perm]
_data_y = _data_y[_perm]

x_train = torch.Tensor(_data_x[:-30])
y_train = torch.LongTensor(_data_y[:-30])
x_test = torch.Tensor(_data_x[-30:])
y_test = torch.LongTensor(_data_y[-30:])

del _perm, _data_x, _data_y


model = torch.nn.Sequential(
    torch.nn.Linear(4, 20),
    torch.nn.ReLU(),
    torch.nn.Linear(20, 15),
    torch.nn.ReLU(),
    torch.nn.Linear(15, 3),
)
criterion = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters())

for epoch in range(4096):
    output = model.forward(x_train)
    loss = criterion.forward(output, y_train)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 64 == 0 and epoch > 0:
        print(f"epoch {epoch+1}, loss {loss.item():.4f}")

with torch.no_grad():
    model.eval()
    output = model.forward(x_test)
    loss = criterion.forward(output, y_test)
    _, predicted = torch.max(output, 1)
    print(f"test loss {loss.item()}, test acc {accuracy_score(y_test, predicted)}")
