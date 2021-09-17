from django.shortcuts import render
from django.urls import reverse_lazy

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

#genric views 
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import CustomUser
from api.models import Book
from .forms import RegistrationForm
from api.forms import PartialBookForm



class AuthorBooks(LoginRequiredMixin ,ListView):
    
    model = Book
    template_name ="author/home.html"
    paginate_by = 10
    
    def get_queryset(self):
        return Book.objects.filter(author=self.request.user)

class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    template_name = 'author/create_book.html'
    fields = ['book_title','book_description','cover_image','genres']
    success_url = reverse_lazy('author_books')

    def form_valid(self, form):
        book = Book(author = self.request.user)
        form = PartialBookForm(self.request.POST,self.request.FILES, instance=book)
        # self.object = form.save(commit=False)
        # self.object.author = self.request.user
        # self.object.genres = 
        # self.object.save()
        # form.save_m2m()
        form.save()
        return super(BookCreateView, self).form_valid(form)


class BookUpdate(LoginRequiredMixin, UpdateView):
    model = Book
    fields = ['book_title','book_description','cover_image','genres']
    template_name = 'author/book_update_form.html'
    success_url = reverse_lazy('author_books')

class BookDelete(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'author/book_confirm_delete.html'
    success_url = reverse_lazy('author_books')

class BookDetail(DetailView):
    model = Book
    template_name = 'author/book_detail.html'



















#Authentication views 

class RegistrationView(CreateView):
    template_name = 'registration/register.html'
    form_class = RegistrationForm

    def get_context_data(self, *args, **kwargs):
        context = super(RegistrationView, self).get_context_data(*args, **kwargs)
        context['next'] = self.request.GET.get('next')
        return context

    def get_success_url(self):
        next_url = self.request.POST.get('next')
        success_url = reverse('login')
        if next_url:
            success_url += '?next={}'.format(next_url)

        return success_url


class ProfileView(UpdateView):
    model = CustomUser
    fields = ['name', 'phone','bio', 'date_of_birth', 'picture']
    template_name = 'registration/profile.html'

    def get_success_url(self):
        return reverse('index')

    def get_object(self):
        return self.request.user

def author_logout(request):
    logout(request)
    return redirect('/author/')