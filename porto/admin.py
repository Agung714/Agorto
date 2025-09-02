from django.contrib import admin
from .models import Tag, Portofolio

# Register your models here.

class PortofolioAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

admin.site.register(Tag)
admin.site.register(Portofolio, PortofolioAdmin)
