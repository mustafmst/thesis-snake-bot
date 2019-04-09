from tensorflow import keras
import tensorflow as tf


class NeuralNetworkBuilder:
    def __init__(self):
        self.model = keras.Sequential()

    def with_input_shape(self, shape):
        self.model.add(keras.layers.Flatten(input_shape=shape))

    def with_dense_layer(self, size):
        self.model.add(keras.layers.Dense(size,
                                          kernel_initializer='random_uniform',
                                          bias_initializer='random_uniform'))

    def build(self):
        self.model.add(keras.layers.Dense(4, activation=tf.nn.softmax,
                                          bias_initializer='random_uniform'))
        self.model.compile(optimizer=tf.train.AdamOptimizer(),
                           loss='sparse_categorical_crossentropy',
                           metrics=['accuracy'])
        return self.model
