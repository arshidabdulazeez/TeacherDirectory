from django import forms
from .models import Teacher,Subject

from django import forms

class ImportTeachersForm(forms.Form):
    csv_file = forms.FileField(label='CSV File', required=False)  # Allow empty file uploads


class TeacherForm(forms.ModelForm):
    
    class Meta:
        SUBJECT_CHOICES = [
        ('math', 'Mathematics'),
        ('english', 'English'),
        ('cs', 'Computer Science'),
        ('physics', 'Physics'),
        ('chemistry', 'Chemistry'),
        ('biology', 'Biology'),
        ('geography', 'Geography'),
        ('arabic', 'Arabic'),
        ('history', 'History'),
        # Add more subjects as needed
        ]
        model = Teacher
        fields = ('first_name', 'last_name', 'profile_picture', 'email', 'phone_number', 'room_number', 'subjects_taught')
        # subjects_taught = forms.ChoiceField(choices=SUBJECT_CHOICES)
    def clean_subjects_taught(self):
        subjects_taught = self.cleaned_data['subjects_taught']
        if len(subjects_taught) > 5:
            raise forms.ValidationError("A teacher can teach no more than 5 subjects.")
        return subjects_taught
    
class SubjectForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = '__all__'
