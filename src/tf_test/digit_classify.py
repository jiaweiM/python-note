import os
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import datasets

# 加载 MNIST 数据集
(x, y), (x_test, y_test) = datasets.mnist.load_data()
# 转换为浮点数，并缩放到 -1~1
x = 2 * tf.convert_to_tensor(x, dtype=tf.float32) / 255. - 1
y = tf.convert_to_tensor(y, dtype=tf.int32)
y = tf.one_hot(y, depth=10)
print(x.shape, y.shape)
train_data = tf.data.Dataset.from_tensor_slices((x, y))
train_data = train_data.batch(512)


