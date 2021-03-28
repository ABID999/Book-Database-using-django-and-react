from django.contrib import admin

from .models import Genres, Book, Review, Bookmark

# Register your models here.

admin.site.register(Genres)
admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Bookmark)
