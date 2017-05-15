#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 14 2017
@author: miyoshidaigo
Practice for Machine Learning !!
"""

#%%

import os
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_graphviz

#ディレクトリ指定
basedir = "/Users/miyoshidaigo/workspace/pyrtc_170514/pyrtc/titanic"

indir = os.path.join(basedir, "input")
outdir = os.path.join(basedir, "output")
test = os.path.join(indir, "test.csv")
train = os.path.join(indir, "train.csv")


#%%
#CSV読み込み
test_df = pd.read_csv(test)
train_df = pd.read_csv(train)


#%%
#決定木
clf = DecisionTreeClassifier(max_depth=2, criterion="entropy")
# clf.fit(train_df, train_df["Survived"])


#%%
#データ加工
#Pclass, sex->toInt, Age, SibSp, Parch, Fare

def toint(sex):
    if sex == "male": 
        return 0
    elif sex == "female":
        return 1

train_df["SexNum"] = train_df["Sex"].apply(toint)
# train_df["SecNum"] = train_df["Sex"].apply(lambda x: 0 if x=="male" else 1)

train_df["Age"] = train_df["Age"].fillna(train_df["Age"].mean())

predictor = ["Pclass","Age", "SexNum", "SibSp", "Parch", "Fare"]
target = ["Survived"]

#%%
#分析
clf.fit(train_df[predictor], train_df[target])
export_graphviz(clf, os.path.join(outdir, "tree.dot"))

