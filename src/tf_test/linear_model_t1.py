import numpy as np

data = []  # 保存样本数据
for i in range(100):
    x = np.random.uniform(-10, 10)  # 随机采样输入 x
    # 采样高斯噪音
    eps = np.random.normal(0., 0.01)  # 均值为 0，方差为 0.01 的高斯分布随机采样噪音
    # 得到模型的输出
    y = 1.477 * x + 0.089 + eps
    data.append((x, y))  # 保存数据点

data = np.array(data)  # 转换为 2D Numpy 数组


# 循环计算在每个点预测值与真实值之间差的平方并累加，从而获得训练集上的均方差
def mse(b, w, points):
    # 根据当前的 w,b 参数计算均方差损失
    totalError = 0
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        # 计算差值平方和
        totalError += (y - (w * x + b)) ** 2

    return totalError / float(len(points))


def step_gradient(b_current, w_current, points, lr):
    b_gradient = 0
    w_gradient = 0
    M = float(len(points))
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        b_gradient += (2 / M) * ((w_current * x + b_current) - y)
        w_gradient += (2 / M) * x * ((w_current * x + b_current) - y)

    new_b = b_current - (lr * b_gradient)
    new_w = w_current - (lr * w_gradient)

    return new_b, new_w


def gradient_descent(points, starting_b, starting_w, lr, num_iterations):
    b = starting_b
    w = starting_w
    for step in range(num_iterations):
        b, w = step_gradient(b, w, np.array(points), lr)
        loss = mse(b, w, points)
        if step % 50 == 0:
            print(f"iteration: {step}, loss: {loss}, w:{w}, b:{b}")
    return b, w


if __name__ == '__main__':
    # 加载训练集数据
    lr = 0.01  # 学习率
    initial_b = 0  # 初始化 b 为 0
    initial_w = 0  # 初始化 w 为 0
    num_iterations = 1000
    # 训练优化 1000 次，返回最优 w*, b* 和训练下降的过程
    b, w = gradient_descent(data, initial_b, initial_w, lr, num_iterations)
    loss = mse(b, w, data)  # 最优解 w,b 上的均方差
    print(f"Final loss: {loss}, w:{w}, b:{b}")
