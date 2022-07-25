import pickle

with open('/home/user3/ElasticFace/datasets/faces_megafacetrain_112x112/lfw.bin', 'rb') as f:
    data = pickle.load(f, encoding='bytes')

print(data)