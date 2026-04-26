"""
TensorFlow 官网示例：使用内置方法进行训练和评估
https://tensorflow.google.cn/guide/keras/train_and_evaluate?hl=zh-cn
"""

import numpy as np
import tensorflow as tf
import keras
from keras import layers
from download_data import download_dataset


model = keras.Sequential([
    keras.Input(shape=(784,), name="digits"),  # 显式定义输入层
    layers.Dense(64, activation="relu", name="dense_1"),
    layers.Dense(64, activation="relu", name="dense_2"),
    layers.Dense(10, activation="softmax", name="predictions")
])


# 加载 MNIST 数据集
download_dataset("mnist")
x_train: np.ndarray
y_train: np.ndarray
x_test: np.ndarray
y_test: np.ndarray
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# 预处理
x_train = x_train.reshape(60000, 784).astype("float32") / 255
x_test = x_test.reshape(10000, 784).astype("float32") / 255
y_train = y_train.astype("float32")
y_test = y_test.astype("float32")

# 保留一万个样本用于验证
x_val = x_train[-10000:]
y_val = y_train[-10000:]
x_train = x_train[:-10000]
y_train = y_train[:-10000]

model.compile(
    optimizer=keras.optimizers.RMSprop(),  # Optimizer
    # Loss function to minimize
    loss=keras.losses.SparseCategoricalCrossentropy(),
    # List of metrics to monitor
    metrics=[keras.metrics.SparseCategoricalAccuracy()],
)

print("Fit model on training data")
history = model.fit(
    x_train,
    y_train,
    batch_size=64,
    epochs=5,

    # 一个 epoch 结束后用验证集评估模型
    validation_data=(x_val, y_val),
)

# 用测试机评估模型
print("\nEvaluate on test data")
results = model.evaluate(x_test, y_test, batch_size=128)
print("test loss, test acc:", results)

# Generate predictions (probabilities -- the output of the last layer)
# on new data using `predict`
print("\nGenerate predictions for 3 samples")
predictions = model.predict(x_test[:3])
print("predictions shape:", predictions.shape)

# Evaluate the model on the test data using `evaluate`
print("\nEvaluate on test data")
results = model.evaluate(x_test, y_test, batch_size=128)
print("test loss, test acc:", results)
