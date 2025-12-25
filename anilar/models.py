from django.db import models

class Ani(models.Model):
    baslik = models.CharField(max_length=100)
    resim = models.ImageField(upload_to='fotograflar/')
    aciklama = models.TextField(blank=True)
    tarih = models.DateField()

    def __str__(self):
        return self.baslik