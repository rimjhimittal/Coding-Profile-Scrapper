from django.contrib import admin
from .models import User, leetcode_acc, codechef_acc
# Register your models here.
admin.site.register(User)
admin.site.register(leetcode_acc)
admin.site.register(codechef_acc)