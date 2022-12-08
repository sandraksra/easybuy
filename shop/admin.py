from django.contrib import admin
from . models import *

# Register your models here.
class catagadmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
admin.site.register(catag,catagadmin)

class proadmin(admin.ModelAdmin):
    list_display=['name','slug','priice','img','stock','available','category']
    list_editable=['priice','stock','img','available','category']
    prepopulated_fields={'slug':('name',)}
admin.site.register(product,proadmin)
