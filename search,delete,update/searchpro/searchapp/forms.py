from django import forms

class BookSearchForm(forms.Form):
    query = forms.CharField(label='Search for a book', max_length=200)



from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']  # Add fields as necessary

# forms.py

from django import forms

class BookSearchForm(forms.Form):
    query = forms.CharField(label='Search for a book', max_length=100)
