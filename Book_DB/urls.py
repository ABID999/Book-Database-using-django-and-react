from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

from django.urls import path, include
from django.contrib.auth import views as auth_views

from django.conf.urls import url
from . import settings
from django.views.static import serve

from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



from author.views import RegistrationView, ProfileView, AuthorBooks, author_logout, BookCreateView, BookUpdate, BookDetail, BookDelete

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', include('api.urls')),
    path('author/login/', auth_views.LoginView.as_view(), name='login'),
    path('author/register/', RegistrationView.as_view(), name='author_register'),
    path('author/logout/', author_logout, name='author_logout'),
    path('author/', AuthorBooks.as_view(), name="author_books"),
    path('author/create', BookCreateView.as_view(), name="create_book"),
    path('author/book/<int:pk>', BookDetail.as_view(), name="book_detail"),
    path('author/update/<int:pk>', BookUpdate.as_view(), name="book_update"),
    path('author/delete/<int:pk>/', BookDelete.as_view(), name="book_delete")
]
 
 
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# if settings.DEBUG: 
#     urlpatterns += [
#         url(r'^images/(?P<path>.*)$',serve, {
#             'document_root': settings.MEDIA_ROOT,
#         }),
#     ]


# path('accounts/login/', auth_views.LoginView.as_view()),

#path('', HomeView.as_view(), name='home')