from django.contrib import admin
from .models import Todo
# Register your models here.
 
class TodoModelAdmin(admin.ModelAdmin):
    list_display = ('title','body')


admin.site.register(Todo)