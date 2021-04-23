from django.forms import ModelForm
from django.forms import forms
from .models import Book, IssueRequest

class BookForm(ModelForm):
    image = forms.FileField(required=True)
    class Meta:
        model = Book
        fields ='__all__'

class IssueForm(ModelForm):
    class Meta:
        model = IssueRequest
        fields='__all__'