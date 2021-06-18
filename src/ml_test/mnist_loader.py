"""
加载 MNIST 图像数据。
"""

import pickle
import gzip
import numpy as np

def load_data():
    """
    以元组的形式返回 MNIST 数据，包含训练数据，验证数据和测试数据。

    返回的 training_data 有两项元组，
    """
