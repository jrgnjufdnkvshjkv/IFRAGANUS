from django.db import models
# Create your models here.


class Ariza(models.Model):
    ism_familya = models.CharField(max_length=200)
    raqamingiz = models.IntegerField()
    bizgasavollar = models.TextField()

    def __str__(self):
        return self.name

class  Kurslar(models.Model):
    qaysi_dastur_uchun = models.CharField(max_length=200)
    qayerdansiz = models.CharField(max_length=150)

    def __str__(self):
        return self.qayerdansiz


class Konsultatsiya(models.Model):
    ismingiz = models.CharField(max_length=150)
    raqam = models.IntegerField()

    def __str__(self):
        return self.ismingiz














