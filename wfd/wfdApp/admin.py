from django.contrib import admin

# Register your models here.
from .models import StaffMember, ShiftManager, generalManager
from .models import Item, Request

admin.site.register(StaffMember)
admin.site.register(ShiftManager)
admin.site.register(generalManager)
admin.site.register(Item)
admin.site.register(Request)
