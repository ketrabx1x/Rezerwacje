from django.contrib import admin
from .models import Sale, Cateringi, Rezerwacje, Wyposazenie

# Register your models here.
admin.site.register(Sale)
admin.site.register(Rezerwacje)
admin.site.register(Cateringi)
admin.site.register(Wyposazenie)