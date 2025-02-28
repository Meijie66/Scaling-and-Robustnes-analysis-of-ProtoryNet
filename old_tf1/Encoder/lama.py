import pandas as pd
from transformers import AutoModel, AutoTokenizer
from sklearn.preprocessing import normalize 
import tensorflow as tf
import re




#print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
# 加载数据集
dir = "/home/limei/ProtoryNet/CUB_data/"
with open (dir + 'train_data.csv', 'rb') as fp:
    train = pd.read_csv(fp, nrows=300)
    train_shuffled = train.sample(frac=1, random_state=42).reset_index(drop=True)
    #print('shuffle:',train_shuffled)
with open (dir + 'test_data.csv', 'rb') as fp:
    test = pd.read_csv(fp, nrows=243)
    test_shuffled = test.sample(frac=1, random_state=32).reset_index(drop=True)
    print('shuffle_test:',len(test_shuffled))


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


print('len x_train, x_train[0]:',len(x_train),len(x_train[0]))
print('type y_train[0]:',type(y_train[0]))

def lama_embeddings(sentences):
    model_name = "meta-llama/Llama-3.2-1B" 
    tokenizer = AutoTokenizer.from_pretrained(model_name) 
    model = AutoModel.from_pretrained(model_name)
    embedding = []
    for i in range(len(sentences)):

        inputs = tokenizer(sentences[i], return_tensors="pt")

        with tf.GradientTape(persistent=False, watch_accessed_variables=False) as tape:
    # Get model outputs
            outputs = model(**inputs, training=False)  # Ensure `training=False` for inference

# Compute mean over the last dimension (equivalent to `last_hidden_state.mean(dim=1)`)
            embeddings = tf.reduce_mean(outputs.last_hidden_state, axis=1)  # Pooling for sentence embeddings


        normalized_embeddings = normalize(embeddings.numpy(), axis=1)
        embedding.append(normalized_embeddings)
    return embedding

print("sample_sentences:",x_train[0])

embed_sample = lama_embeddings(x_train[0])
print('embed_sample:',embed_sample)


embeded_test = []
for i in range(len(x_test)):
    test_x = lama_embeddings(x_test[i])
    embeded_test.append(test_x)

with open('embedding_test_lama.pkl', 'wb') as f:
    pickle.dump(embeded_test, f)


embeded_train = []
for i in range(len(x_train)):
    train_x = lama_embeddings(x_train[i])
    embeded_train.append(train_x)

with open('embedding_train_lama.pkl', 'wb') as f:
    pickle.dump(embeded_train, f)
breakpoint()


with open('embedding_train.pkl', 'rb') as f:
    train_vectors = pickle.load(f)
    print('train_vectors:',len(train_vectors),train_vectors[0])

with open('embedding_test.pkl', 'rb') as f:
    test_vectors = pickle.load(f)
    print('test_vectors:',len(test_vectors),test_vectors[0])
