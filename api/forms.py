<<<<<<< HEAD
from .models import Book
from django import forms

class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('book_title','book_description','cover_image','genres','author')


class PartialBookForm(forms.ModelForm):
    class Meta: 
        model = Book
=======
from .models import Book
from django import forms

class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('book_title','book_description','cover_image','genres','author')


class PartialBookForm(forms.ModelForm):
    class Meta: 
        model = Book
>>>>>>> 74c7a38a5a1aba25a9f431acbd0f004e28279a1a
        exclude = ['author']