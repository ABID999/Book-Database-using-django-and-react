<<<<<<< HEAD
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from django.views.decorators.csrf import csrf_exempt

from .views import BookListView, BookDetailView, ReviewsViewSet, UserViewSet, get_reviews, author_detail

router = routers.DefaultRouter()
router.register(r'books', BookListView)
router.register(r'register', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth', obtain_auth_token),
    path('book/<int:pk>/', BookDetailView.as_view()),
    path('book/review/<int:fk>/', ReviewsViewSet.as_view()),
    path('book/review/all/<int:fk>/', get_reviews),
    path('author/<int:pk>/', author_detail),
]

=======
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from django.views.decorators.csrf import csrf_exempt

from .views import BookListView, BookDetailView, ReviewsViewSet, UserViewSet, get_reviews, author_detail

router = routers.DefaultRouter()
router.register(r'books', BookListView)
router.register(r'register', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth', obtain_auth_token),
    path('book/<int:pk>/', BookDetailView.as_view()),
    path('book/review/<int:fk>/', ReviewsViewSet.as_view()),
    path('book/review/all/<int:fk>/', get_reviews),
    path('author/<int:pk>/', author_detail),
]

>>>>>>> 74c7a38a5a1aba25a9f431acbd0f004e28279a1a
#path('book/review/<int:fk>/', ReviewsViewSet.as_view()),