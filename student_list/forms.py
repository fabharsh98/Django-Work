from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = {'name', 'phone', 'email', 'subject', 'roll'}
        labels = {
            'name': 'Full Name',
            'phone': 'Mobile No.',
            'email': 'Email ID',
            'subject': 'Subject',
            'roll': 'Roll No.'
        }

        def __init__(self, *args, **kwargs):
            super(StudentForm, self).__init__(*args, **kwargs)
            self.fields['subject'].empty_label = "Select"