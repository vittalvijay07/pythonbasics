from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookSearchForm, BookForm  # Ensure you import your forms


def search_books(request):
    form = BookSearchForm()  # Assuming you have this form defined
    results = []

    if request.method == 'GET':
        form = BookSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Book.objects.filter(title__icontains=query)  # Adjust as necessary

    return render(request, 'searchapp/search_books.html', {'form': form, 'results': results})


def update_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('search_books')  # Redirect back to search results
    else:
        form = BookForm(instance=book)

    return render(request, 'searchapp/update_book.html', {'form': form})

def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        book.delete()
        return redirect('search_books')  # Redirect back to search results

    return render(request, 'searchapp/delete_book.html', {'book': book})


def book_list(request):
    books = Book.objects.all()  # Fetch all books
    return render(request, 'searchapp/book_list.html', {'books': books})
