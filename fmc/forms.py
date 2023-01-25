from django import forms
from .models import Work, Appliances

class DateInput(forms.DateInput):
    input_type = 'date'

class WorkOrderForm(forms.ModelForm):

    # To remove the colon from label : <------------ This.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''

    class Meta:
        model = Work
        fields = ('private', 'company', 'address', 'apartment', 'city', 'state', 'zip_code', 'phone','appliance', 'comments', 'requested')
        label_suffix = '-'
        labels = {
            'company': 'Management Company or Name',
            'private': 'Private Job',
            'requested': 'Date requested',
        }

        widgets = {
            'private': forms.RadioSelect(attrs={'class': 'd-flex justify-content-evenly'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'style': 'text-align: center'}),
            'apartment': forms.TextInput(attrs={'class': 'form-control', 'style': 'text-align: center'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'style': 'text-align: center'}),
            'state': forms.Select(attrs={'class': 'form-control', 'style': 'text-align-last: center'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'style': 'text-align: center'}),
            'appliance': forms.TextInput(attrs={'class': 'form-control', 'style': 'text-align: center'}),
            'phone':forms.TextInput(attrs={'class': 'form-control', 'style': 'text-align: center'}),
            'company':forms.TextInput(attrs={'class': 'form-control', 'style': 'text-align: center'}),
            'comments': forms.TextInput(attrs={'class': 'form-control', 'style': 'text-align: center'}),
            'requested': DateInput(attrs={'class': 'form-control', 'style': 'text-align: center'})
        }

class WorkOrderFormUpdate(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''

    class Meta:
        model = Work
        fields = ('private', 'company', 'address', 'apartment', 'city', 'state', 'zip_code', 'phone','appliance', 'comments', 'requested')
        label_suffix = '-'
        labels = {
            'company': 'Management Company or Name',
            'private': 'Private Job'
        }

        widgets = {
            'private': forms.RadioSelect(attrs={'class': 'd-flex justify-content-evenly'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'style': 'text-align: center'}),
            'apartment': forms.TextInput(attrs={'class': 'form-control', 'style': 'text-align: center'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'style': 'text-align: center'}),
            'state': forms.Select(attrs={'class': 'form-control', 'style': 'text-align-last: center'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'style': 'text-align: center'}),
            'appliance': forms.TextInput(attrs={'class': 'form-control', 'style': 'text-align: center'}),
            'phone':forms.TextInput(attrs={'class': 'form-control', 'style': 'text-align: center'}),
            'company':forms.TextInput(attrs={'class': 'form-control', 'style': 'text-align: center'}),
            'status': forms.Select(attrs={'class': 'form-control', 'style': 'text-align-last: center'}),
            'comments': forms.TextInput(attrs={'class': 'form-control', 'style': 'text-align-last: center'}),
            'requested': DateInput(attrs={'class': 'form-control', 'style': 'text-align: center'})
        }

class WorkOrderPartAdd(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''

    class Meta:
        model = Appliances
        fields = ('appliance', 'part_name', 'model_number', 'part_number', 'url',)
        label_suffix = '-'
        labels = {}

        widgets = {
            'appliance': forms.TextInput(attrs={'class': 'form-control', 'style': 'text-align: center'}),
            'part_name': forms.TextInput(attrs={'class': 'form-control', 'style': 'text-align: center'}),
            'model_number': forms.TextInput(attrs={'class': 'form-control', 'style': 'text-align: center'}),
            'part_number': forms.TextInput(attrs={'class': 'form-control', 'style': 'text-align: center'}),
            'url': forms.TextInput(attrs={'class': 'form-control', 'style': 'text-align: center'}),
        }

class WorkOrderPartUpdate(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''

    class Meta:
        model = Appliances
        fields = ('appliance', 'part_name', 'model_number', 'part_number', 'url',)
        label_suffix = '-'
        labels = {}

        widgets = {
            'appliance': forms.TextInput(attrs={'class': 'form-control', 'style': 'text-align: center'}),
            'part_name': forms.TextInput(attrs={'class': 'form-control', 'style': 'text-align: center'}),
            'model_number': forms.TextInput(attrs={'class': 'form-control', 'style': 'text-align: center'}),
            'part_number': forms.TextInput(attrs={'class': 'form-control', 'style': 'text-align: center'}),
            'url': forms.TextInput(attrs={'class': 'form-control', 'style': 'text-align: center'}),
        }