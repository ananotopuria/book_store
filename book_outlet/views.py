from django.shortcuts import get_object_or_404, render
from django.http import Http404
from .models import Book
from .forms import UserForm 

def homepage(request):
    return render(request, 'book_outlet/homepage.html')

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'book_outlet/book_detail.html', {'book': book})


def user_form_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            return render(request, 'book_outlet/success.html', {'name': name})
    else:
        form = UserForm()
    
    
    return render(request, 'book_outlet/user_form.html', {'form': form})

