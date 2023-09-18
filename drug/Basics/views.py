from django.shortcuts import render
import pandas as pd
import sklearn 
from sklearn import tree
import numpy as np
from sklearn.preprocessing import LabelEncoder
def home(request):
     if(request.method=="POST"):
        data=request.POST
        d=int(data.get('age'))
        s=int(data.get('sex'))
        b=int(data.get('bp'))
        c=int(data.get('cholesterol'))
        n=float(data.get('na_to_k'))
        path="C:\\Users\\\mf879\\OneDrive\\Desktop\\naveed\\naveed\\drug200.csv"
        data1=pd.read_csv(path)
        data1['Sex']=data1['Sex'].map({'M':1,'F':0})
        le_BP=LabelEncoder()
        data1['BP']=le_BP.fit_transform(data1['BP'])
        le_C=LabelEncoder()
        data1['Cholesterol']=le_C.fit_transform(data1['Cholesterol'])
        outputs=data1.drop(['Age','Sex','BP','Cholesterol','Na_to_K'],'columns')
        inputs=data1.drop('Drug','columns')
        
        model=tree.DecisionTreeClassifier()
        model.fit(inputs,outputs)
        info=model.predict([[d,s,b,c,n]])
        return render(request,"home.html",context={'info':info})

     return render(request,'home.html')