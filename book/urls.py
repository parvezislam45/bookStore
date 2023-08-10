from django.urls import path
from book.views import home,store_book,showBook,editBook,delateBook

urlpatterns = [
    path('',home),
    path('store_nre_book/',store_book,name='storebook'),
    path('show_book/',showBook,name='showbook'),
    path('edit_book/<int:id>',editBook,name='edit_book'),
    path('delete_book/<int:id>',delateBook,name='delete_book'),
]
