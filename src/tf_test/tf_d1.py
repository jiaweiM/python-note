import tensorflow as tf
import numpy as np

inputs = tf.keras.layers.Input(shape=(3,))
d = tf.keras.layers.Dense(2, name='out')
output_1 = d(inputs)
output_2 = d(inputs)
model = tf.keras.models.Model(
    inputs=inputs, outputs=[output_1, output_2])
model.compile(optimizer="Adam", loss="mse", metrics=["mae", "acc"])
x = np.random.random((2, 3))
y = np.random.randint(0, 2, (2, 2))
model.fit(x, (y, y))

print(model.metrics_names)
