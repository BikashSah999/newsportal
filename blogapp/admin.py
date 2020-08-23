from django.contrib import admin
from .models import Blog,Contact,Categorylist

# Register your models here.
admin.site.register(Blog)
admin.site.register(Categorylist)
admin.site.register(Contact)