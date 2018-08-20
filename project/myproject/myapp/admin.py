from django.contrib import admin
from .models import Customer,Book,Rent
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=[f.name  for f in Customer._meta.fields]
admin.site.register(Customer,CustomerAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display=[f.name  for f in Book._meta.fields]
admin.site.register(Book,BookAdmin)

class RentAdmin(admin.ModelAdmin):
    list_display=[f.name  for f in Rent._meta.fields]
admin.site.register(Rent,RentAdmin)