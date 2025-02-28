import tensorflow as tf
from transformers import BertTokenizer
import pandas as pd
import matplotlib.pyplot as plt
import re
from transformers import TFBertForSequenceClassification
#from tensorfloow.keras.callbacks import EarlyStopping

# Load BERT tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
# 加载数据集
dir = "/home/limei/ProtoryNet/CUB_data/"
with open (dir + 'train_data.csv', 'rb') as fp:
    train = pd.read_csv(fp, nrows=1500)
    train_shuffled = train.sample(frac=1, random_state=16).reset_index(drop=True)
    #print('shuffle:',train_shuffled)
with open (dir + 'test_data.csv', 'rb') as fp:
    test = pd.read_csv(fp, nrows=1380)
    test_shuffled = test.sample(frac=1, random_state=16).reset_index(drop=True)
    print('test shuffle:',len(test_shuffled))


train_not_clean = train_shuffled ['description'].tolist()
y_train = train_shuffled ['label'].tolist()
test_not_clean = test_shuffled ['description'].tolist()
y_test= test_shuffled ['label'].tolist()


def gen_sents(para):
    res = []
    for p in para:
        sents = re.split(r'\.\n|\n',p)
        sents = [s.strip() for s in sents if s.strip()]
        res.append(sents)
    return res


x_train = gen_sents(train_not_clean)
x_test = gen_sents(test_not_clean)


concatenated_x_train = [" ".join(sample) for sample in x_train]
concatenated_x_test = [" ".join(sample) for sample in x_test]

# Tokenize the data
def tokenize_data(data, tokenizer, max_length=512):
    return tokenizer(
        text = data,
        max_length=max_length,
        padding='max_length',
        truncation=True,
        return_tensors='tf'
    )

x_train_encoding = tokenize_data(concatenated_x_train, tokenizer)
x_test_encoding = tokenize_data(concatenated_x_test, tokenizer)

train_labels = tf.convert_to_tensor(y_train)
test_labels = tf.convert_to_tensor(y_test)

# Create TensorFlow datasets
train_dataset = tf.data.Dataset.from_tensor_slices((dict(x_train_encoding), train_labels)).batch(1)
test_dataset = tf.data.Dataset.from_tensor_slices((dict(x_test_encoding), test_labels)).batch(1)

# Load BERT model with 3 output classes
model = TFBertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=50)

model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=2e-5),
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=['accuracy']
)

#early_stopping = EarlyStopping(monitor='val_loss', patience=7, restore_best_weights=True)
#callbacks=[early_stopping]

#Train the BERT mode
history = model.fit(
    train_dataset,
    epochs=50,  # Adjust based on your needs
    validation_data=test_dataset
)

results = model.evaluate(test_dataset)
print(f"Test Loss: {results[0]}")
print(f"Test Accuracy: {results[1]}")


# Plot training & validation loss values
plt.figure(figsize=(10, 6))
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Model Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend(loc='upper right')
plt.savefig('loss_plot_5.png') 
plt.show()

# Plot training & validation accuracy values
plt.figure(figsize=(10, 6))
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Model Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(loc='lower right')
plt.savefig('accuracy_plot_50.png')
plt.show()