from tensorflow import keras


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
        self.model.add(keras.layers.Dense(4, activation=keras.activations.softmax,
                                          bias_initializer='random_uniform'))
        if genotype is not None:
            self.model.set_weights(genotype)
        return self.model
