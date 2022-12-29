from django.forms import ModelForm
from .models import account,assets
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class editForm(ModelForm):
    class Meta:
        model=account
        fields=('date','type','description','cost')
        widgets = {
            'date': DateInput()
        }
    def __init__(self, *args, **kwargs):
        super(editForm,self).__init__(*args, **kwargs)
        self.fields['date'].widget.attrs['class']='form-control'
        self.fields['type'].widget.attrs['class']='form-control'
        self.fields['description'].widget.attrs['class']='form-control'
        self.fields['cost'].widget.attrs['class']='form-control' 

class assetForm(ModelForm):
    class Meta:
        model=assets
        fields=('asset','expectedCost')

    def __init__(self, *args, **kwargs):
        super(assetForm,self).__init__(*args, **kwargs)
        self.fields['asset'].widget.attrs['class']='form-control'
        self.fields['expectedCost'].widget.attrs['class']='form-control'


    



