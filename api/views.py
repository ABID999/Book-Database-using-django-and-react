<<<<<<< HEAD
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from author.models import CustomUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import JsonResponse
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
import json


from .serializers import BookSerializer,BookDetailSerializer, ReviewSerializer, UserSerializer, AuthorDetailSerializer
from .models import Book , Review
# Create your views here.



class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer



class BookListView(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('book_title')
    serializer_class = BookSerializer


# class BookListView(APIView):
#     def get(self, request, pk, format=None):
#         books = Book.objects.all().order_by('book_title')
#         for book in books: 
#             review = Review.objects.filter(book = book.id).aggregate(Avg('user_rating'))
#             print(review)
#             book.rating = review 


class BookDetailView(APIView):
    def get_obj(self, pk):
        try: 
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404
    def get_author(self, pk):
        book = self.get_obj(pk)
        return Author.objects.get(pk=book.author)
    def get(self, request, pk, format=None):
        book = self.get_obj(pk)
        serializer = BookDetailSerializer(book)
        return Response(serializer.data)

@api_view(["GET"])
@permission_classes([AllowAny])
def author_detail(request, pk, format=None):
    author = CustomUser.objects.get(pk=pk)
    print(author)
    if(not author.is_author):
        return Response(status=status.HTTP_404_NOT_FOUND)
    author_serializer = AuthorDetailSerializer(author)
    author_books = Book.objects.filter(author = author.id)
    print(author_books)
    print(author_serializer)
    book_serializer = BookSerializer(author_books, many = True)
    print(book_serializer)
    return Response({
        'author': author_serializer.data,
        'books': book_serializer.data
    })

    
    
    


@api_view(["GET"])
@permission_classes([AllowAny])
def get_reviews(request, fk , format=None):
    reviews = Review.objects.filter(book__id = fk)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)

class ReviewsViewSet(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, fk , format=None):
        try:
            review = Review.objects.get(book__id = fk, user = request.user.id)
            serializer = ReviewSerializer(review)
            return Response(serializer.data)
        except:
            return Response(json.loads('[]'))
        


    def post(self, request, fk, format=None):
        if(Review.objects.filter(book__id = fk, user = request.user.id).exists()):
            return Response(json.loads('{"error": "Review already exists"}'))
        
        review = request.data 
        review._mutable = True
        review['user'] = request.user.id
        review['book'] = Book.objects.get(id = fk).id
        review._mutable = False
        print(review)
        serializer = ReviewSerializer(data = review)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, fk, format=None):
        review = Review.objects.get(book__id = fk, user= request.user.id)
        new_data = request.data
        new_data._mutable = True
        new_data['user'] = review.user.id
        new_data['book'] = review.book.id
        new_data._mutable = False
        serializer = ReviewSerializer(review, data =new_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, fk, format=None):
        review = Review.objects.get(book__id = fk, user = request.user.id)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




=======
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from author.models import CustomUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import JsonResponse
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
import json


from .serializers import BookSerializer,BookDetailSerializer, ReviewSerializer, UserSerializer, AuthorDetailSerializer
from .models import Book , Review
# Create your views here.



class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer



class BookListView(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('book_title')
    serializer_class = BookSerializer


# class BookListView(APIView):
#     def get(self, request, pk, format=None):
#         books = Book.objects.all().order_by('book_title')
#         for book in books: 
#             review = Review.objects.filter(book = book.id).aggregate(Avg('user_rating'))
#             print(review)
#             book.rating = review 


class BookDetailView(APIView):
    def get_obj(self, pk):
        try: 
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404
    def get_author(self, pk):
        book = self.get_obj(pk)
        return Author.objects.get(pk=book.author)
    def get(self, request, pk, format=None):
        book = self.get_obj(pk)
        serializer = BookDetailSerializer(book)
        return Response(serializer.data)

@api_view(["GET"])
@permission_classes([AllowAny])
def author_detail(request, pk, format=None):
    author = CustomUser.objects.get(pk=pk)
    print(author)
    if(not author.is_author):
        return Response(status=status.HTTP_404_NOT_FOUND)
    author_serializer = AuthorDetailSerializer(author)
    author_books = Book.objects.filter(author = author.id)
    print(author_books)
    print(author_serializer)
    book_serializer = BookSerializer(author_books, many = True)
    print(book_serializer)
    return Response({
        'author': author_serializer.data,
        'books': book_serializer.data
    })

    
    
    


@api_view(["GET"])
@permission_classes([AllowAny])
def get_reviews(request, fk , format=None):
    reviews = Review.objects.filter(book__id = fk)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)

class ReviewsViewSet(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, fk , format=None):
        try:
            review = Review.objects.get(book__id = fk, user = request.user.id)
            serializer = ReviewSerializer(review)
            return Response(serializer.data)
        except:
            return Response(json.loads('[]'))
        


    def post(self, request, fk, format=None):
        if(Review.objects.filter(book__id = fk, user = request.user.id).exists()):
            return Response(json.loads('{"error": "Review already exists"}'))
        
        review = request.data 
        review._mutable = True
        review['user'] = request.user.id
        review['book'] = Book.objects.get(id = fk).id
        review._mutable = False
        print(review)
        serializer = ReviewSerializer(data = review)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, fk, format=None):
        review = Review.objects.get(book__id = fk, user= request.user.id)
        new_data = request.data
        new_data._mutable = True
        new_data['user'] = review.user.id
        new_data['book'] = review.book.id
        new_data._mutable = False
        serializer = ReviewSerializer(review, data =new_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, fk, format=None):
        review = Review.objects.get(book__id = fk, user = request.user.id)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




>>>>>>> 74c7a38a5a1aba25a9f431acbd0f004e28279a1a
