from django import forms
from .models import Posting

class PostingForm(forms.ModelForm):
    class Meta:
        model = Posting
        fields = ['judul', 'konten', 'image']
        # widgets = {
        #     'judul': forms.TextInput(attrs={'class': 'form-control'}),
        #     'konten': forms.Textarea(attrs={'class': 'form-control'}),
        #     'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        # }
        
class ContactForm(forms.Form):
    nama = forms.CharField(max_length=100, label="Nama Lengkap", widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    pesan = forms.CharField(label="Pesan", widget=forms.Textarea(attrs={'class': 'form-control'}))