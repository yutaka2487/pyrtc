#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 7 2017
@author: miyoshidaigo
practice for 'machine learning'
手書き数字の認識
"""

#%%
import os, sys, math
from sklearn import datasets, svm
from sklearn.externals import joblib


#%%
#モデルデータファイル名
DIGITS_PKL = "digit-clf.pkl"

#%%
#予測モデルを作成
def train_digits():
    #手書きデータ読み込み
    digits = datasets.load_digits()
    #訓練する
    data_train = digits.data
    label_train = digits.target
    clf = svm.SVC(gamma = 0.001)
    clf.fit(data_train, label_train)
    #予測モデルを保存
    joblib.dump(clf, DIGITS_PKL)
    print("予測モデルを保存 =", DIGITS_PKL)
    return clf
    
#%%
#手書き画像を8*8グレイスケールのデータ配列に変換
def image_to_data(imagefile):
    import numpy as np
    from PIL import Image
    image = Image.open(imagefile).convert('L')
    image = image.resize((8,8), Image.ANTIALIAS)
    img = np.asarray(image, dtype=float)
    img = np.floor(16 - 16*(img/256))
    img = img.flatten()
    print(img)
    return img


#%%
#データから数字を予測
def predict_digits(data):
    #モデルファイルの読み込み
    if not os.path.exists(DIGITS_PKL):
        clf = train_digits()
    clf = joblib.load(DIGITS_PKL)
    #予測
    n = clf.predict([data])
    print("判定結果 =", n)


#%%
def main():
    #コマンドライン引数を得る
    if len(sys.argv)<=1:
        print("USAGE:")
        print("python3 practice_machine_learning1.py imagefile")
        return
    imagefile = sys.argv[1]
    data = image_to_data(imagefile)
    predict_digits(data)
    
#%%
if __name__ == '__main__':
    main()