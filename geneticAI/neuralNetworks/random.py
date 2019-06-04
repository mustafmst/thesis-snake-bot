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

    def with_layer(self, layer_type, layer_size):
        if layer_type == 'dense':
            self.with_dense_layer(layer_size)
        pass

    def build(self, genotype=None):
        self.model.add(keras.layers.Dense(4, activation=tf.nn.softmax,
                                          bias_initializer='random_uniform'))
        if genotype is not None:
            self.model.set_weights(genotype)
        self.model.compile(optimizer=tf.train.AdamOptimizer(),
                           loss='sparse_categorical_crossentropy',
                           metrics=['accuracy'])
        return self.model
