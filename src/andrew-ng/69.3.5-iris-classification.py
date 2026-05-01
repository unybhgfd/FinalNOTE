"""
鸢尾花分类
"""

import tensorflow as tf
import keras
from sklearn.datasets import load_iris
import numpy as np


_data_x: np.ndarray = load_iris().data  # shape: (150,4)
_data_y: np.ndarray = load_iris().target  # shape: (150,)
_perm = np.random.permutation(len(_data_x))
_data_x = _data_x[_perm]
_data_y = _data_y[_perm]

x_train = _data_x[:-30]
y_train = _data_y[:-30]
x_test = _data_x[-30:]
y_test = _data_y[-30:]

del _perm, _data_x, _data_y

model = keras.Sequential([
    keras.layers.Dense(units=20, activation="relu"),
    keras.layers.Dense(units=15, activation="relu"),
    keras.layers.Dense(units=3),  # 数据集有三个标签
])
model.compile(
    loss=keras.losses.SparseCategoricalCrossentropy(
        from_logits=True),  # 加上 from_logits=True 合并多个操作以减小浮点数误差
    optimizer=keras.optimizers.Adam(),
)
model.fit(x_train, y_train, epochs=512, validation_split=0.2)
model.summary()

losses: np.ndarray = keras.losses.sparse_categorical_crossentropy(
    y_test,
    model.predict(x_test),
    from_logits=True
).numpy()

print("loss:", losses.mean())
