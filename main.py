# show_pkl.py

import pickle

path = '2016.04C.multisnr.pkl'  # path='/root/……/aus_openface.pkl'   pkl文件所在路径

f = open(path, 'rb')
data = pickle.load(f,encoding='bytes')

print(data)
print(len(data))