from django import forms
from book.models import BookStoreModel

class bookStoreForm(forms.ModelForm):
  class Meta :
      model=BookStoreModel
      exclude =['first_pub','last_pub']  