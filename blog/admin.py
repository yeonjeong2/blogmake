from django.contrib import admin
from .models import Blog
from .models import comment

admin.site.register(Blog)
admin.site.register(comment)