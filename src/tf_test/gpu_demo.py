import tensorflow as tf
import os

os.environ['TF_XLA_FLAGS'] = '--tf_xla_enable_xla_devices'
gpu_a = tf.random.normal([10000, 1000])
gpu_b = tf.random.normal([1000, 2000])
c = tf.matmul(gpu_a, gpu_b)
print(c)
