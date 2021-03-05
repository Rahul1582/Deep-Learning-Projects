# Quora Question Pair Similarity using Siamese Network

This is a notebook on Quora Question Pair duplication recognition problem.. 

## Approach

Approach is to use Siamese network. Let the embeddings of two questions be passed through the same network and then concatenate them and apply sigmoid at the end to get an output. For embeddings, GloVe embeddings have been used.

A siamese network is when two different inputs go through the exact same neural network and finally the end-feature vectors that come out of them are merged or compared. In face recognition, a siamese network is often used to tell if two face pictures are of the same person or different persons. Here, once we'll have embeddings of the text, we could use a similar approach.


## Technologies Used

1. Siamese Network

2. Bidirectional LSTM's


## Author

Rahul Kumar Patro
