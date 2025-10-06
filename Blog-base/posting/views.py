from urllib import request
from django.shortcuts import redirect, render, get_object_or_404
from .models import Posting
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.views import View
from django.core.paginator import Paginator
from django.core.cache import cache
from .forms import *
from django.contrib import messages
from django.core.mail import send_mail



# Create your views here.

#def=function base view  class=class base view

def index(request):
    
    postings = Posting.objects.all().order_by('-id')
    
    paginator = Paginator(postings, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'postings': page_obj}

    return render(request, 'posting/index.html', context)

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
    
# def detail_view(request, id):
#     posting = get_object_or_404(Posting, id=id)
#     context = {'posting': posting}
#     return render(request, 'posting/detail.html', context)

# class DetailPosting(generic.DetailView):
#     model = Posting
#     template_name = 'posting/detail.html'

class PostingView(View):
    def get(self, request, pk):
        posting = get_object_or_404(Posting, pk=pk)
        if cache.get(posting.pk):
            posting = cache.get(posting.pk)
            print("Diambil dari cache")
        else:
            posting = get_object_or_404(Posting, pk=pk)
            cache.set(posting.pk, posting)
            print("Di ambil dari disk database")

        context = {'posting': posting}
        return render(request, 'posting/detail.html', context)


class AddPost(LoginRequiredMixin, generic.CreateView):
    model = Posting
    template_name = 'posting/add_post.html'
    form_class = PostingForm  # gunakan form yang sudah benar

    def form_valid(self, form):
        form.instance.penulis = self.request.user  # set penulis otomatis
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.pk})
    
class UpdatePost(LoginRequiredMixin, generic.UpdateView):
    model = Posting
    template_name = 'posting/edit_post.html'
    form_class = PostingForm

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        if self.request.user != post.penulis and not self.request.user.is_superuser:
            messages.error(self.request, "Kamu bukan penulis dari postingan ini.")
            return redirect('index')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        post = self.get_object()
        if post.penulis and not self.request.user.is_superuser:
            messages.error(self.request, "Kamu bukan penulis dari postingan ini.")
            return redirect('index')
        response = super().form_valid(form)
        # Hapus cache setelah update
        cache.delete(post.pk)
        messages.success(self.request, "Postingan berhasil diupdate.")
        return response

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.pk})
    
class DeletePost(LoginRequiredMixin, generic.DeleteView):
    model = Posting
    template_name = 'posting/delete_post.html'
    success_url = reverse_lazy('index')
    
    def get(self, request, *args, **kwargs):
        post = self.get_object()
        if post.penulis and not self.request.user.is_superuser:
            messages.error(self.request, "Kamu bukan penulis dari postingan ini.")
            return redirect('index')
        return super().get(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        post = self.get_object()
        if post.penulis and not self.request.user.is_superuser:
            messages.error(self.request, "Kamu bukan penulis dari postingan ini.")
            return redirect('index')
        messages.success(self.request, "Postingan berhasil dihapus.")
        return super().delete(request, *args, **kwargs)


class SearchPosting(View):
    def get(self, request):
        query = self.request.GET.get('q', '').strip()
        query_list = Posting.objects.filter(
            Q(judul__icontains=query) |
            Q(konten__icontains=query)
        ) if query else []
        context = {
            'query_list': query_list,
            'query': query
        }
        return render(request, 'posting/search.html', context)
    
def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nama = form.cleaned_data['nama']
            email = form.cleaned_data['email']
            pesan = form.cleaned_data['pesan']
            
            # Kirim email
            send_mail(
                'Contact Form Message',
                f'Pesan dari {nama}:\n{pesan}',
                email,
                ['fiscomaulana@gmail.com'],  # Ganti dengan email penerima yang diinginkan
                reply_to=[email],
            )
            return render(request, 'posting/contact_success.html', {'nama': nama})
    else:
        form = ContactForm()
    return render(request, 'posting/contact.html', {'form': form})