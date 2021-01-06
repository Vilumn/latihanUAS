from django.db import models

# Create your models here.
class Folder(models.Model):
    kategori = (
        ('darat', 'darat'),
        ('air', 'air'),
    )

    nama_binatang = models.CharField(default='', max_length=250)
    kategori = models.CharField(max_length=50, choices=kategori)

    def __str__(self):
        return '{}'.format(self.nama_binatang)
