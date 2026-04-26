"""
全连接层前向传播实现
"""

import numpy as np


def g(x):
    """激活函数，这里是 sigmoid"""
    return 1/(1 + np.exp(-x))

def dense(a_in, W):
    # 添加偏置项
    a_in = np.concatenate(([1], a_in))

    # 显式循环实现计算
    # units = W.shape[1]
    # a_out = np.zeros(units)
    # for j in range(units):
    #     w = W[:, j]
    #     a_out[j] = g(w @ a_in)

    # 向量化完成计算
    a_out = g(a_in @ W)

    return a_out



def main():
    W = np.array([
        [-1,  1,  2],  # 把偏置放到 W 里

        [ 1, -3,  5],
        [ 2,  4, -6],
    ])
    a_in = np.array([-2, 4])

    print(dense(a_in, W))

if __name__ == "__main__":
    main()
