import tensorflow as tf
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# 加载数据集
dir = "/home/limei/ProtoryNet/CUB_data/"

with open (dir + 'train_data.csv', 'rb') as fp:
    train = pd.read_csv(fp)
    train_shuffled = train.sample(frac=1, random_state=16).reset_index(drop=True)
    print('shuffle:',train_shuffled)
with open (dir + 'test_data.csv', 'rb') as fp:
    test = pd.read_csv(fp)
    test_shuffled = test.sample(frac=1, random_state=16).reset_index(drop=True)
    print('shuffle:',test_shuffled)

train_not_clean = train_shuffled ['description'].tolist()
y_train = train_shuffled ['label'].tolist()
test_not_clean = test_shuffled ['description'].tolist()
y_test= test_shuffled ['label'].tolist()

def gen_sents(para):
    res = []
    for p in para:
        sents = re.split(r'\.\n|\n', p)
        sents = [s.strip() for s in sents if s.strip()]
        res.append(sents)
    return res



x_train_p = gen_sents(train_not_clean)
x_test_p = gen_sents(test_not_clean)


X = x_train_p + x_test_p

vectorizer = TfidfVectorizer()

concatenated_X = [" ".join(sample) for sample in X]


X_all = vectorizer.fit_transform(concatenated_X)
X_all_dense = X_all.toarray()
print(X_all_dense.shape)


x_train = X_all_dense[:5994]
x_test = X_all_dense[5994:]

'''
for i in range(90):
    train_sentences  = vectorizer.fit_transform(X_train_p[i])
    X_dense = train_sentences.toarray()
    train_vector = X_dense.flatten()
    positive_train_vector = np.abs(train_vector)
    x_train.append(positive_train_vector)

print("train finish embed")

for i in range(88):   
    test_sentences  = vectorizer.fit_transform(X_test_p[i])
    X_dense_test = test_sentences.toarray()
    test_vector = X_dense_test.flatten()
    positive_test_vector = np.abs(test_vector)
    x_test.append(positive_test_vector)
'''
print(x_train[0].shape)
print(x_train[1].shape)
print(x_test[0].shape)
print(y_train[:10])
print('len x_train:',x_train.shape)#59940, 512
print('type y_train[0]:',type(y_train[0]))

model = MultinomialNB()

model.fit(x_train, y_train)

# Make predictions
y_pred = model.predict(x_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

# Print classification report
print('Classification Report:')
print(classification_report(y_test, y_pred))

# Plot confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(12, 10))
sns.heatmap(conf_matrix, annot=False, cmap='Blues', xticklabels=range(1, 201), yticklabels=range(1, 201))
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()
               