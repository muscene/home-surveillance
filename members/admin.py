from django.contrib import admin
from .models import Member
from .models import Attendance
from .models import UnrecognizedFaceRecord
# Register your models here.
admin.site.register(Member)
admin.site.register(UnrecognizedFaceRecord)


