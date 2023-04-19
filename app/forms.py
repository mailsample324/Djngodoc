from django import forms
from .models import Contact
from .models import Picture
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone' , 'subject','message']
    


class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ('title', 'image')
