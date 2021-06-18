"""
该模块实现针对前馈神经网络的随机梯度下降算法。通过反向传播算法计算梯度。这里着重于让代码简单易读且易于修改，没有进行优化。
"""

import numpy as np
import random


class Network():
    def __init__(self, sizes):
        """
        列表 sizes 包含各层神经元的个数。如果 `sizes` 是 [2, 3, 1]，表示有 3 层神经网络，第一层有 2 个神经元，第二层 3 个，第三层 1 个。
        使用一个均值为 0、标准差为 1 的高斯分布随机初始化神经网络的偏执和权重。这里假设第一层是输入层，一般不会对输入层设置偏置。
        """
        self.num_layers = len(sizes)
        self.sizes = sizes
        rng = np.random.default_rng()
        self.biases = [rng.standard_normal(size=(y, 1))
                       for y in sizes[1:]]  # 输入层不需要参数，隐藏层有几个神经元，对应几个 bias
        self.weights = [rng.standard_normal(size=(y, x))
                        for x, y in zip(sizes[:-1], sizes[1:])]  # 每层 weights 数是前后两层的神经元数的乘积

    def feedforward(self, a):
        """
        a 为输入，返回输出
        """
        for b, w in zip(self.biases, self.weights):
            a = sigmoid(np.dot(w, a) + b)
        return a

    def SGD(self, training_data, epochs, mini_batch_size, eta, test_data=None):
        """
        使用小批量随机梯度下降法训练神经网络。training_data 是由输入和输出的元组（x,y）组成的列表。
        如果提供了 test_data，神经网络会在每轮训练结束后用测试数据进行评估，并输出部分进度信息。这对于追踪进度有用
        eta 为学习率
        """

        if test_data:
            n_test = len(test_data)
        n = len(training_data)

        for j in range(epochs):
            random.shuffle(training_data)
            mini_batches = [training_data[k:k + mini_batch_size]
                            for k in range(0, n, mini_batch_size)]
            for mini_batch in mini_batches:
                self.update_mini_batch(mini_batch, eta)
            if test_data:
                print("Epoch {0}: {1}/{2}".format(j, self.eva))

    def update_mini_batch(self, mini_batch, eta):
        """
        对一个小批量应用梯度下降算法和反向传播算法来更新神经网络的权重和偏置。mini_batch 是由若干元祖（x,y）组成的列表，eta 是学习率
        """
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]

        for x, y in mini_batch:
            delta_nabla_b, delta_nabla_w = self.backprop(x, y)

    def backprop(self, x, y):
        """
        返回一个表示代价函数 C_x 梯度的元组（nabla_b, nabla_w）。nabla_w 和 nabla_b 是一层接一层的 numpy 数组的列表，类似于 self.biases 和 self.weights
        """
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]

        # 前馈
        activation = x
        activations = [x]  # 一层接一层存放所有激活值
        zs = []  # 一层接一层存放所有 z 向量

        pass

    def evaluate(self, test_data):
        """
        返回测试输入中神经网络输出正确结果的数目。注意，这里假设神经网络输出的最后一层有最大激活值的神经元的索引。
        """
        test_results = [(np.argmax(self.feedforward(x)), y)
                        for (x, y) in test_data]
        return sum(int(x == y) for (x, y) in test_results)

    @staticmethod
    def cost_derivative(output_activations, y):
        """返回关于输出激活值 的偏导数的向量"""
        return (output_activations - y)


def sigmoid(z):
    """
    the sigmoid function.
    """
    return 1.0 / (1.0 + np.exp(-z))


def sigmoid_prime(z):
    """
    sigmoid 函数的倒数
    """
    return sigmoid(z) * (1 - sigmoid(z))
