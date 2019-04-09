from geneticAI.neuralNetworks.random import NeuralNetworkBuilder
import json

builder = NeuralNetworkBuilder()

builder.with_input_shape((2, 2))
builder.with_dense_layer(16)

model = builder.build()

with open('weights.json', 'w') as output:
    weights = []
    for i in range(1, len(model.layers)):
        lw = model.get_layer(index=i).get_weights()
        weights.append([lw[0].tolist(), lw[1].tolist()])
    json.dump(weights, output, indent=4)
