# Neural Networks Topic

### Findings
#### One Neuron - Hidden Layer

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