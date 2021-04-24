from django.db import models
from django.core.validators import MinLengthValidator
import datetime

# Create your models here.
class Book(models.Model):
    book_name= models.CharField(max_length=50)
    isbn = models.CharField(max_length=13, validators=[MinLengthValidator(13)])
    desc = models.CharField(max_length=1000)
    author = models.CharField(max_length=50)
    quantity = models.IntegerField(default=5)
    image= models.ImageField(upload_to='librarymanager/images', default="")
    
    def __str__(self):
        return self.book_name

class IssueRequest(models.Model):
    request_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=50)
    student_name = models.CharField(max_length=50)
    student_id = models.CharField(max_length=50, default="")
    email = models.EmailField(max_length=254)
    duration = models.PositiveIntegerField()
    phone = models.CharField(max_length=12)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.student_name

class Approval(models.Model):
    request_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=50)
    student_name = models.CharField(max_length=50)
    student_id = models.CharField(max_length=50, default="")
    email = models.EmailField(max_length=254)
    duration = models.PositiveIntegerField()
    phone = models.CharField(max_length=12)
    approvaldate= models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.student_name