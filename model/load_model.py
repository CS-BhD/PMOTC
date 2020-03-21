import os
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.externals import joblib
from sklearn import preprocessing
import numpy as np
import warnings


def load_model(pkl='model/clf.pkl'):
    return joblib.load(pkl)


def read_features_csv(file, flag):
    x = []
    y = []
    if not os.path.exists(file):
        print('Error: file %s does not exist.' % file)
    with open(file, 'rt') as f:
        for line in f:
            part = line.split(',')
            part = list(map(float, part[1:]))
            x.append(part)
            y.append(flag)
    f.close()
    return x, y


def feature_select(feature):
    warnings.filterwarnings("ignore")
    positive, p_f = read_features_csv('model/data/PFMito-TPC.txt', 1)
    negative, n_f = read_features_csv('model/data/non_mito-TPC.txt', 0)
    train = np.array(positive + negative)
    train_l = np.array(p_f + n_f)
    min_max_scaler = preprocessing.MinMaxScaler()
    train = min_max_scaler.fit_transform(train)
    feature = min_max_scaler.fit_transform(feature)
    SKB = SelectKBest(f_classif, 399)
    SKB.fit(train, train_l)
    return SKB.transform(feature)
