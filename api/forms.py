from .models import Book
from django import forms

class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('book_title','book_description','cover_image','genres','author')


class PartialBookForm(forms.ModelForm):
    class Meta: 
        model = Book
        exclude = ['author']