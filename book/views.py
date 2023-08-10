from django.shortcuts import render,redirect
from book.forms import bookStoreForm
from book.models import BookStoreModel


def home(request):
    return render(request, 'home.html')


def store_book(request):
    if request.method == 'POST':
        book = bookStoreForm(request.POST)
        if book.is_valid():
            book.save()
            print(book.cleaned_data)
           
            return redirect('showbook')
        else:

            book = bookStoreForm()
    else:
        book = bookStoreForm()
    return render(request, 'storeBook.html', {'form': book})


def showBook(request):
    book = BookStoreModel.objects.all()
    print(book)
    
    return render(request,'showBook.html',{'data':book})

def editBook(request,id):
    book = BookStoreModel.objects.get(pk = id)
    form = bookStoreForm(instance = book)
    if request.method == 'POST':
        form = bookStoreForm(request.POST,instance = book)
        if form.is_valid():
            form.save()
            return redirect('showbook')
    return render(request,'storeBook.html',{'form':form})

def delateBook(request,id):
    book = BookStoreModel.objects.get(pk = id).delete()
    return redirect('showbook')
    
