from django.db import models

# Create your models here.


class ElectronLugatModel(models.Model):
    ru = models.CharField(max_length=150, unique=True)
    uz_kiril = models.CharField(max_length=150, unique=True)
    uz_lotin = models.CharField(max_length=150, unique=True)
    en = models.CharField(max_length=150, unique=True)
    tr = models.CharField(max_length=150, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.en + self.uz_lotin

    class Meta:
        db_table = "Elektron Lug'at"
