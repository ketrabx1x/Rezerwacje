from django.shortcuts import render
from django.http import HttpResponse
from .models import Sale, Cateringi, Rezerwacje, Wyposazenie
from .fomrs import RezerwacjaForm

# Create your views here.

def index(request):
    sale = Sale.objects.all()
    cateringi = Cateringi.objects.all()
    rezerwacje = Rezerwacje.objects.all()
    wyposazenie = Wyposazenie.objects.all()
    dane = {'sale' : sale,
            'cateringi' : cateringi,
            'wyposazenie' : wyposazenie,
            'rezerwacje' : rezerwacje}
    return render(request, 'szablon.html', dane)

def sale(request, id):
    sale_user = Sale.objects.get(pk=id)
    sale = Sale.objects.all()
    cateringi = Cateringi.objects.all()
    rezerwacje = Rezerwacje.objects.all()
    wyposazenie = Wyposazenie.objects.all()
    dane = {'sale_user' : sale_user,
            'sale' : sale,
            'cateringi' : cateringi,
            'wyposazenie' : wyposazenie,
            'rezerwacje' : rezerwacje}
    return render(request, 'sala.html', dane)

def cateringi(request, id):
    catering_user = Cateringi.objects.get(pk=id)
    sale = Sale.objects.all()
    cateringi = Cateringi.objects.all()
    rezerwacje = Rezerwacje.objects.all()
    wyposazenie = Wyposazenie.objects.all()
    dane = {'catering_user' : catering_user,
            'sale' : sale,
            'cateringi' : cateringi,
            'wyposazenie' : wyposazenie,
            'rezerwacje' : rezerwacje}
    return render(request, 'catering.html', dane)

def wyposazenie(request, id):
    wyposazenie_user = Wyposazenie.objects.get(pk=id)
    sale = Sale.objects.all()
    cateringi = Cateringi.objects.all()
    rezerwacje = Rezerwacje.objects.all()
    wyposazenie = Wyposazenie.objects.all()
    dane = {'wyposazenie_user' : wyposazenie_user,
            'sale' : sale,
            'cateringi' : cateringi,
            'wyposazenie' : wyposazenie,
            'rezerwacje' : rezerwacje}
    return render(request, 'wyposazenie.html', dane)

def rezerwacje(request, id):
    rezerwacje_user = Rezerwacje.objects.get(pk=id)
    sale = Sale.objects.all()
    cateringi = Cateringi.objects.all()
    rezerwacje = Rezerwacje.objects.all()
    wyposazenie = Wyposazenie.objects.all()
    dane = {'rezerwacje_user' : rezerwacje_user,
            'sale' : sale,
            'cateringi' : cateringi,
            'wyposazenie' : wyposazenie,
            'rezerwacje' : rezerwacje}
    return render(request, 'rezerwacja.html', dane)

def dodaj_rezerwacje(request):
    form = RezerwacjaForm(request.POST or None)
    sale = Sale.objects.all()
    cateringi = Cateringi.objects.all()
    rezerwacje = Rezerwacje.objects.all()
    wyposazenie = Wyposazenie.objects.all()

    if form.is_valid():
        form.save(commit=True)
        form = RezerwacjaForm()

    dane = {'form' : form,
            'sale' : sale,
            'cateringi' : cateringi,
            'wyposazenie' : wyposazenie,
            'rezerwacje' : rezerwacje}
    return render(request, 'dodaj_rezerwacje.html', dane)