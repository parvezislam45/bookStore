from django.db import models

class BookStoreModel(models.Model):
    CATEGORY = (
        ('Mystery','Mystery'),
        ('Thriller','Thriller'),
        ('Scr-fi','Scr-fi'),
        ('Humor','Humor'),
        ('Horror','Horror'),
        )
    id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    category = models.CharField(max_length=30,choices=CATEGORY)
    first_pub = models.DateTimeField(auto_now_add=True)
    last_pub = models.DateTimeField(auto_now=True)
