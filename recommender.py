# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 21:14:43 2019

@author: KIIT
"""

import numpy as np
import pandas as pd
import random

laptop_data=pd.read_excel(r"C:\Users\KIIT\Desktop\dell\model\laptop_data.xlsx")

laptop_data.shape

#laptop_data.to_csv("data/laptop_data.csv")

laptop_data.head()
laptop_data['Weight'] = laptop_data['Weight'].map(lambda x: x.rstrip('kg'))
laptop_data['Ram'] = laptop_data['Ram'].map(lambda x: x.rstrip('GB'))

laptop_data=laptop_data.drop('ScreenResolution', axis=1)

laptop_data=laptop_data.drop('Weight', axis=1)

laptop_data.dtypes
laptop_data["Ram"] = pd.to_numeric(laptop_data["Ram"])

laptop_data.dtypes
X=laptop_data.values

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()

laptop_data.head()
X[:, 5] = labelencoder_X.fit_transform(X[:, 5])
X[:, 9]=labelencoder_X.fit_transform(X[:,9])
X[:, 7]=labelencoder_X.fit_transform(X[:,7])
X[:, 8]=labelencoder_X.fit_transform(X[:,8])

X

from sklearn.cluster import KMeans
X_fit=X[:,4:11]
print(X_fit)

kmeans = KMeans(init='k-means++', n_clusters=8, n_init=100).fit(X[:,4:11])

classes=pd.DataFrame(kmeans.predict(X_fit))

laptop_data=pd.concat([laptop_data,classes],axis=1)

laptop_data.head()



laptop_data.columns=[   'Id', 'Company',     'Product',    'TypeName',      'Inches',
               'Cpu',         'Ram',      'Memory',         'Gpu',
             'OpSys', 'Price_euros',             'Class']

laptop_data.to_csv(r"C:\Users\KIIT\Desktop\dell\results.xlsx", index=False)

import pickle
pickle.dump(kmeans, open(r"C:\Users\KIIT\Desktop\dell\model\kmeans.pkl", "wb"))
model=pickle.load(open(r"C:\Users\KIIT\Desktop\dell\model\kmeans.pkl","rb"))

item_class=model.predict([[1,1,0,0,0,1,2100]]).tolist().pop()
print(item_class)

laptop_data.head()
laptop_data.shape

result_data=laptop_data.loc[laptop_data['Class'] == item_class]
result_data=result_data.loc[laptop_data['Company']=="Dell" ]
result_data['Id'][0:3].tolist()

result_data[0:3]