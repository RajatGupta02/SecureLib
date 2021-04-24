from django.contrib import admin
from .models import Book,IssueRequest, Approval
# Register your models here.
admin.site.register(Book)
admin.site.register(IssueRequest)
admin.site.register(Approval)