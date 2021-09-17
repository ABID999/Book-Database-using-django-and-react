<<<<<<< HEAD
from rest_framework import serializers
from .models import Book, Genres, Review, Bookmark
from author.models import CustomUser
from django.db.models import Avg


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'name')
        extra_kwargs = {'password': {'write_only':True, 'required': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = ('genre',)        


class BookSerializer(serializers.ModelSerializer):
    avg_rating = serializers.SerializerMethodField('get_avg_rating')
    genres_list = GenreSerializer(source = "genres", read_only=True, many=True)
    class Meta:
        model = Book
        fields = (
            'id',
            'book_title',
            'cover_image',
            'author',
            'genres_list',
            'avg_rating'
        )
    
    def get_avg_rating(self, book):
        rating = Review.objects.filter(book = book.id).aggregate(Avg('user_rating'))
        return rating['user_rating__avg']

class AuthorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('name', 'phone', 'bio','picture',)





class AuthorNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('name',)

class BookDetailSerializer(serializers.ModelSerializer):
    genres_list = GenreSerializer(source = "genres", read_only=True, many=True)
    author_name = AuthorNameSerializer(source = "author", read_only=True)
    avg_rating = serializers.SerializerMethodField('get_avg_rating')
    class Meta:
        model = Book
        fields = '__all__'
    
    def get_avg_rating(self, book):
        rating = Review.objects.filter(book = book.id).aggregate(Avg('user_rating'))
        return rating['user_rating__avg']




class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'    

=======
from rest_framework import serializers
from .models import Book, Genres, Review, Bookmark
from author.models import CustomUser
from django.db.models import Avg


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'name')
        extra_kwargs = {'password': {'write_only':True, 'required': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = ('genre',)        


class BookSerializer(serializers.ModelSerializer):
    avg_rating = serializers.SerializerMethodField('get_avg_rating')
    genres_list = GenreSerializer(source = "genres", read_only=True, many=True)
    class Meta:
        model = Book
        fields = (
            'id',
            'book_title',
            'cover_image',
            'author',
            'genres_list',
            'avg_rating'
        )
    
    def get_avg_rating(self, book):
        rating = Review.objects.filter(book = book.id).aggregate(Avg('user_rating'))
        return rating['user_rating__avg']

class AuthorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('name', 'phone', 'bio','picture',)





class AuthorNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('name',)

class BookDetailSerializer(serializers.ModelSerializer):
    genres_list = GenreSerializer(source = "genres", read_only=True, many=True)
    author_name = AuthorNameSerializer(source = "author", read_only=True)
    avg_rating = serializers.SerializerMethodField('get_avg_rating')
    class Meta:
        model = Book
        fields = '__all__'
    
    def get_avg_rating(self, book):
        rating = Review.objects.filter(book = book.id).aggregate(Avg('user_rating'))
        return rating['user_rating__avg']




class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'    

>>>>>>> 74c7a38a5a1aba25a9f431acbd0f004e28279a1a
