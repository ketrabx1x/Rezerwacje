from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Sale(models.Model):
    nazwa = models.CharField(max_length=100)
    pojemnosc = models.IntegerField()
    cena = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        verbose_name = "Sala"
        verbose_name_plural = "Sale"

    def __str__(self):
        return self.nazwa
    
class Cateringi(models.Model):
    def __str__(self):
        return self.nazwa
    
    nazwa = models.CharField(max_length=50)
    opis = models.TextField(blank=True)
    cena = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        verbose_name = "Catering"
        verbose_name_plural = "Cateringi"

class Wyposazenie(models.Model):
    def __str__(self):
        return self.nazwa
    
    nazwa = models.CharField(max_length=50)
    opis = models.TextField(blank=False)
    cena = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        verbose_name = "Wypozażenie"
        verbose_name_plural = "Wypozażenia"
    
class Rezerwacje(models.Model):
    sala = models.ForeignKey(Sale, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    catering = models.ForeignKey(Cateringi, on_delete=models.CASCADE, null=True, blank=True)
    wyposazenie = models.ForeignKey(Wyposazenie, on_delete=models.CASCADE, null=True, blank=True)
    poczatek_wynajmu = models.DateTimeField()
    koniec_wynajmu = models.DateTimeField()

    def __str__(self):
        return f"{self.sala} - {self.catering} - {self.wyposazenie} - {self.poczatek_wynajmu} - {self.koniec_wynajmu}"
    
    class Meta:
        verbose_name = "Rezerwacja"
        verbose_name_plural = "Rezerwacje"