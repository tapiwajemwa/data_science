from django import forms

class form_name_view(forms.Form):
    SeniorCitizen = forms.IntegerField(min_value=0,max_value=1,label='Senior Citizen',widget= forms.NumberInput(attrs={"class": 'form-control','placeholder':"(0: No, 1: Yes)"}))
    Partner = forms.IntegerField(min_value=0,max_value=1,label='Partner',widget= forms.NumberInput(attrs={"class": 'form-control','placeholder':"(0: No, 1: Yes)"}))
    Dependents = forms.IntegerField(min_value=0,max_value=1,label="Any Dependants",widget= forms.NumberInput(attrs={"class": 'form-control','placeholder':"(0: No, 1: Yes)"}))
    Tenure = forms.IntegerField(min_value=0,max_value=100,label='Tenure',widget= forms.NumberInput(attrs={"class": 'form-control','placeholder':"(Period in Months)"}))
    OnlineSecurity = forms.IntegerField(label='Online Security',min_value=0,max_value=1,widget= forms.NumberInput(attrs={"class": 'form-control','placeholder':"(0: No, 1: Yes)"}))
    OnlineBackup = forms.IntegerField(label='Online Backup',min_value=0,max_value=1,widget= forms.NumberInput(attrs={"class": 'form-control','placeholder':"(0: No, 1: Yes)"}))
    DeviceProtection = forms.IntegerField(label='Device Protection',min_value=0,max_value=1,widget= forms.NumberInput(attrs={"class": 'form-control','placeholder':"(0: No, 1: Yes)"}))
    TechSupport = forms.IntegerField(label='Tech Support',min_value=0,max_value=1,widget= forms.NumberInput(attrs={"class": 'form-control','placeholder':"(0: No, 1: Yes)"}))
    Contract = forms.IntegerField(label='Contract',min_value=0,max_value=1,widget= forms.NumberInput(attrs={"class": 'form-control','placeholder':"(0: No, 1: Yes)"}))
    PaperlessBilling = forms.IntegerField(label='Contract',min_value=0,max_value=1,widget= forms.NumberInput(attrs={"class": 'form-control','placeholder':"(0: No, 1: Yes)"}))
    PaymentMethod = forms.IntegerField(label='Paperless Billing',min_value=0,max_value=4,widget= forms.NumberInput(attrs={"class": 'form-control','placeholder':"([0]Electronic check, [1]Mailed Check, [2]BankTransfer)"}))
    MonthlyCharges = forms.DecimalField(label='Monthly Charges',min_value=0,widget= forms.NumberInput(attrs={"class": 'form-control','placeholder':"(Value in $)"}))