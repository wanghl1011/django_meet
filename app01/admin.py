from django.contrib import admin
from app01.models import *
# Register your models here.

admin.site.register(UserInfo)
admin.site.register(MeetingRoom)
admin.site.register(TimeSlot)
admin.site.register(OrderRecord)