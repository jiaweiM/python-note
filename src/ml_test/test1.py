import tensorflow as tf

# 载入 MNIST 数字图像数据
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Building a Deep Learning Model
model = tf.keras.models.Sequential([
    tf.keras.layers.InputLayer(input_shape=(784,)),
    tf.keras.layers.Dense(256, activation="relu"),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(256, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compilation and overview of the model
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

print(model.summary())

# Preprocessing of MNIST data (flatten 28 x 28 pixel to 784 for input)
x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)

# Casting to a float32 type because of a true divide error when dividing by itself
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

# Normalizes data to a float32 type in the range of 0 to 1
x_train /= 255
x_test /= 255

# Covert to categorical data (1 => [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
y_train = tf.keras.utils.to_categorical(y_train, 10)
y_test = tf.keras.utils.to_categorical(y_test, 10)

model.fit(x_train, y_train, epochs=20, validation_split=0.3)

model.evaluate(x_test, y_test, verbose=2)
