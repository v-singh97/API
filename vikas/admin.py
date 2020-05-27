from django.contrib import admin

# Register your models here.
from .models import User, Activity_period

admin.site.register(User)
admin.site.register(Activity_period)