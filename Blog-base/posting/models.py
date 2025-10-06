from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Posting(models.Model):
    judul = models.CharField(max_length=200)
    konten = models.TextField()
    image = models.ImageField(upload_to='images', null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    penulis = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.judul
    
    def delete(self, *args, **kwargs):
        if self.image:
            self.image.delete(save=False)
        super().delete(*args, **kwargs)