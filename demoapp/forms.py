from django.forms import ModelForm, Form

from .models import Employee

class EmployeeForm(ModelForm):

    class Meta:
        model = Employee
        fields = '__all__'

    def clean_first_name(self):
        data = self.cleaned_data['first_name']
        return data.title()

    def clean_last_name(self):
        data = self.cleaned_data['last_name']
        return data.title()

