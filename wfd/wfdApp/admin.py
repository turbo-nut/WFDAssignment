from django.contrib import admin

# Register your models here.
from .models import StaffMember, ShiftManager, generalManager, Item

admin.site.register(StaffMember)
admin.site.register(ShiftManager)
admin.site.register(generalManager)
admin.site.register(Item)
