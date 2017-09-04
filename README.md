# Text Classification
I use the pretrained glove.6B.100d dictionary for the word embedding, the file could be downloaded from https://nlp.stanford.edu/projects/glove/, the current problem is this pretrained dictionary just has few Chinese characters, so the accuracy is very low about 75%. I will focus on training the chinese_based word embedding dictionary because the word embedding is upmost for the deep learning approach.

# Setup
The program is based on python 2.7 and Jupyter notebook, remember to download the glove.6B and put it in the same directory

# Approach
I adopt the textCNN as the benchmark

# Result
The prediction result is stored in prediction.csv

# Reference
TextCNN network: https://arxiv.org/pdf/1408.5882.pdf
