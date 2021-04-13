# 激活函数

- [激活函数](#激活函数)
  - [激活函数的使用](#激活函数的使用)
  - [可用激活函数](#可用激活函数)
    - [relu](#relu)
  - [参考](#参考)

## 激活函数的使用

激活函数既可以通过 `Activation` 层使用，也可以通过 `activation` 参数使用：

```py
model.add(layers.Dense(64, activation=activations.relu))
```

等价于：

```py
from tensorflow.keras import layers
from tensorflow.keras import activations

model.add(layers.Dense(64))
model.add(layers.Activation(activations.relu))
```

所有内置的激活函数也可以通过其字符串传递识别：

```py
model.add(layers.Dense(64, activation='relu'))
```

## 可用激活函数

### relu

```py
tf.keras.activations.relu(x, alpha=0.0, max_value=None, threshold=0)
```

## 参考

- https://keras.io/api/layers/activations/