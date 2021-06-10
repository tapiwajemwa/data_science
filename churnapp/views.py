from django.shortcuts import render
from . import forms
import numpy as np
import pandas as pd
import joblib
Result = 99
# Create your views here.

def modelform(request):
    global Result
    form = forms.form_name_view()
    data = []
    # X = np.array(data)
    Model = joblib.load('finalized_model.sav')
    dictionary = request.POST
    counter = 1
    for k in dictionary.values():
        if counter==13:
            break
        counter+=1
        data.append(int(k))
    print(data)
    newdata = pd.DataFrame(data,index=['SeniorCitizen', 'Partner', 'Dependents', 'tenure', 'OnlineSecurity',
       'OnlineBackup', 'DeviceProtection', 'TechSupport', 'Contract',
       'PaperlessBilling', 'PaymentMethod', 'MonthlyCharges'])

    xgbmodel = Model.predict(newdata.T)
    Result = xgbmodel
    return render(request,'model.html',{'form':form,'xgbmodel':xgbmodel})

def result(request):
    global Result 
    try:
        if Result[0] == 0:
            value = 'The customer did not churn'
        if Result[0] ==1:
            value = "The customer did churn"
    except Exception:
        value ="The prediction is unknown yet. Please fill in some values"
    
    return render(request,'result.html',{'result':value})