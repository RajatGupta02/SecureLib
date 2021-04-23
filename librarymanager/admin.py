from django.contrib import admin
from .models import Book,IssueRequest
# Register your models here.
admin.site.register(Book)
admin.site.register(IssueRequest)