import tensorflow as tf
import tensorflow.keras as keras

fashion_mnist = keras.datasets.fashion_mnist

(x_train_full, y_train_full), (x_test, y_test) = fashion_mnist.load_data()

assert x_train_full.shape == (60000, 28, 28)

# 分出一部分作为验证数据集
x_valid, x_train = x_train_full[:5000] / 255.0, x_train_full[5000:] / 255.0
y_valid, y_train = y_train_full[:5000], y_train_full[5000:]

# 不同 y 值对应的类别名称
class_names = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
               "Sandal", "Shirt", "Sneaker", "Bag", "Ankleboot"]

# 创建模型
model = keras.models.Sequential()
model.add(keras.layers.Flatten(input_shape=[28, 28]))
model.add(keras.layers.Dense(300, activation='relu'))
model.add(keras.layers.Dense(100, activation='relu'))
model.add(keras.layers.Dense(10, activation='softmax'))

model.compile(loss='sparse_categorical_crossentropy',  # 等价于 keras.losses.sparse_categorical_crossentropy
              optimizer='sgd',  # 等价于 keras.optimizers.SGD()
              metrics=['accuracy']  # keras.metrics.sparse_categorical_accuracy
              )

print(model.summary())

history = model.fit(x_train, y_train, epochs=30, validation_data=(x_valid, y_valid))

