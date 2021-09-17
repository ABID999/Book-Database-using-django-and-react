<<<<<<< HEAD
from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL


class Genres(models.Model):
    genre = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.genre


class Book(models.Model):
    book_title = models.CharField(max_length=100)
    book_description = models.TextField()
    cover_image = models.ImageField(upload_to='book_covers', null=True, blank=True)
    release_date = models.DateField(auto_now=False, auto_now_add=True)
    genres = models.ManyToManyField(Genres)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.book_title
    
    def get_absolute_url(self):
        return reverse('books:detail', args=[self.id])
    

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user_rating = models.IntegerField()
    user_review = models.TextField(null=True, blank = True)


class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


    

=======
from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL


class Genres(models.Model):
    genre = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.genre


class Book(models.Model):
    book_title = models.CharField(max_length=100)
    book_description = models.TextField()
    cover_image = models.ImageField(upload_to='book_covers', null=True, blank=True)
    release_date = models.DateField(auto_now=False, auto_now_add=True)
    genres = models.ManyToManyField(Genres)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.book_title
    
    def get_absolute_url(self):
        return reverse('books:detail', args=[self.id])
    

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user_rating = models.IntegerField()
    user_review = models.TextField(null=True, blank = True)


class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


    

>>>>>>> 74c7a38a5a1aba25a9f431acbd0f004e28279a1a
