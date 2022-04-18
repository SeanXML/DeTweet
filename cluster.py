import tensorflow as tf
import pandas as pd
import numpy as np
import io
import tf.keras.preprocessing.text.Tokenizer
import tf.keras.preprocessing.sequence.pad_sequences
# Please check your tensorflow and keras version if errors occur


data = pd.read_csv('/filepath', sep=",", na_values=[""], encoding='UTF-8')
raw_text = data['Texts']
raw_label = data['Labels']
# Read .csv file


train_texts = []
train_labels = []
for i in raw_text:
    j = tf.convert_to_tensor(i)
    train_texts.append(str(j))
for i in raw_label:
    train_labels.append(i)

# Convert string objects to tensor
'''
You may need to add a certain token before and after your text, because Tokenizer may confuse the format head and end
Like this: b'(...text...)', which makes your meta file a mess
'''
 

train_texts = np.array(train_texts)
train_labels_final = np.array(train_labels)
# If you have a test set, process it with method above


vocab_size = 2000
embedding_dim = 16
max_length = 200
trunc_type = 'post'
oov_tok = "<OOV>"
# Modify parameters above to suit your case


tokenizer = Tokenizer(num_words = vocab_size, oov_token=oov_tok)
tokenizer.fit_on_texts(train_texts)
word_index = tokenizer.word_index
sequences = tokenizer.texts_to_sequences(train_texts)
padded = pad_sequences(sequences, maxlen=max_length, truncating = trunc_type)
train_labels_final = np.array(train_labels_final)
# Tokenizing and Padding, view detals on https://www.tensorflow.org/tensorboard


model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=max_length),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(16, activation = 'relu'),
    tf.keras.layers.Dense(1, activation = 'sigmoid')
])
# Building Model


model.compile(loss=tf.keras.losses.BinaryCrossentropy(from_logits=True), optimizer='adam',metrics=['accuracy'])
padded = np.array(padded)
# Compiling Model


model.fit(padded,
         train_labels_final,
         epochs = 2)
# Training Model, add test set if you have


reverse_word_index = dict([value, key] for (key, value) in word_index.items())
# Reverse the token and its vector in the dictionary


e = model.layers[0]
weights = e.get_weights()[0]
print(weights.shape)


out_v = io.open('/filepath', 'w', encoding='UTF-8')
out_m = io.open('/filepath', 'w', encoding='UTF-8')
for word_num in range(1, 2000):  
    word = reverse_word_index[word_num]
    embeddings = weights[word_num]
    out_m.write(word + "\n")
    out_v.write('\t'.join([str(x) for x in embeddings]) + "\n")

out_v.close()
out_m.close()