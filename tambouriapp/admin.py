from django.contrib import admin
from .models import Tableau, Villa, Voiture, Peintre

# Register your models here.

admin.site.register(Tableau)
admin.site.register(Villa)
admin.site.register(Voiture)
admin.site.register(Peintre)
