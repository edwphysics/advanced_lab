# Neural Networks Topic

### Findings
#### One Neuron - One Hidden Layer

- Overfitting appears when the number of epochs increases to 100. Training Time ~ 50s.
```
Train accuracy: 0.9862385321100917
Test accuracy: 0.6545454545454545
The model is likely overfitting.
```
The loss function ~ 0 at the end of the training.
- When using n_epoch=50 we don't get overfitting but (of course) a bad prediction of the class. Training Time ~ 22s.
```
Train accuracy: 0.6857798165137615
Test accuracy: 0.5909090909090909
The model is not overfitting.
```
The loss function oscillates around 0.2 at the end of the training.

#### Two Hidden Layers

- I use a two-hidden layer NN; one with 128 neurons and one with 64 neurons. The output is a binary neuron output.

```
input_size = train_images[0].flatten().shape[0]
hidden_layer1_size = 128
hidden_layer2_size = 64
output_size = 1
```
Here, I noted that the result is bad and takes lots of time ~ 5 min for 3 epochs. The final loss is > 0.7

- Reduce to one layer with 32 neurons and the other to 16 neurons. The result slightly improved and took a fraction of time ~ 2 min.
```
Epoch 1, Loss: 0.6890
Epoch 2, Loss: 0.6861
Epoch 3, Loss: 0.6858
```
and the accuracy:
```
Test accuracy with hidden layers: 0.5272727272727272
Train accuracy with hidden layers: 0.5665137614678899
```
It indicates that the NN is not overfitted.

- Increase the n_epoch from 3 to 10. The loss converged to `0.6857` but the accurracy did not improve.
```
Epoch 1, Loss: 0.6895
Epoch 2, Loss: 0.6861
Epoch 3, Loss: 0.6858
Epoch 4, Loss: 0.6857
Epoch 5, Loss: 0.6857
Epoch 6, Loss: 0.6857
Epoch 7, Loss: 0.6857
Epoch 8, Loss: 0.6857
Epoch 9, Loss: 0.6857
Epoch 10, Loss: 0.6857
```
```
Test accuracy with hidden layers: 0.5272727272727272
Train accuracy with hidden layers: 0.5665137614678899
```

- As the result did not improve with the decrese in the learning_rate or increase in the epochs, I will test with the following architechture:
```
input_size = train_images[0].flatten().shape[0]
    hidden_layer1_size = 64
    hidden_layer2_size = 32
    hidden_layer3_size = 16
    output_size = 1
```
