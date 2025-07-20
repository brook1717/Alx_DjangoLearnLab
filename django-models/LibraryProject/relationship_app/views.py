from django.shortcuts import render
from .models import Book
from django.views.generic.detail import DetailView
from .models import Library

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # <-- Required exact pattern
    return render(request, 'relationship_app/list_books.html', {'books': books})



# Class-based view to display a specific library and its books
class LibraryDetailView(DetailView):  # <-- Required pattern
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
