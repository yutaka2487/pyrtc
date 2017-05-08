#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 15:16:50 2017
@author: miyoshidaigo
practice for 'machine learning'
Determine the taste of wine
"""

#%%
from sklearn import cross_validation, svm, metrics

#%%
#ワインデータ読み込み
wine_csv = []
with open("winequality-white.csv", "r", encoding="utf-8") as fp:
    for line in fp:
        line = line.strip()
        cols = line.split(";")
        wine_csv.append(cols)
        
#1行目のヘッダーを削除
wine_csv = wine_csv[1:]

#%%
#csv各データを文字列から数値に変換
labels = []
data = []

for cols in wine_csv:
    cols = list(map(lambda n: float(n), cols))
    #ワインのグレードを調整
    grade = int(cols[11])
    if grade == 9: grade = 8
    if grade <  4: grade = 5
    labels.append(grade)
    data.append(cols[0:11])
    
#%%
#データを分ける
data_train, data_test, label_train, label_test = \
cross_validation.train_test_split(data, labels)

#%%
#ランダムフォレストアルゴリズムにより学習
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier()
clf.fit(data_train, label_train)

#%%
#予測
predict = clf.predict(data_test)
total = ok = 0
for idx, pre in enumerate(predict):
    # pre = predict[idx]
    answer = label_test[idx] #正解ラベル
    total += 1
    #ほぼ正解なら、正解とする
    if (pre-1) <= answer <= (pre+1):
        ok += 1
print("正解率 = ", ok, "/", total, "=", ok/total)


#%%
#正確な結果の表示
ac_score = metrics.accuracy_score(label_test,predict)
cl_report = metrics.classification_report(label_test,predict)
print("正解率 = ", ac_score)
print("Report = \n", cl_report)